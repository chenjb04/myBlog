from flask import Blueprint, jsonify, current_app, request, abort, render_template
from utils.captcha.captcha import captcha
import base64
import re
import random
import datetime
import json

from app import redis_store, db
from constants import IMAGE_CODE_REDIS_EXPIRES, SMS_CODE_REDIS_EXPIRES
from app.models import User
from utils.celery_task.tasks import send_mail
from utils.auth import Auth

app = Blueprint(__name__ + 'app', __name__, template_folder='../../utils/templates/')


class MyEncoder(json.JSONEncoder):
    """
    json序列化bytes类型
    """
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


@app.route('/api/user/image_code', methods=['GET'])
def get_image_code():
    """
    获取图片验证码
    :return:
    """
    image_code_id = request.args.get('image_code_id', None)
    if not image_code_id:
        return abort(403)
    name, text, image = captcha.generate_captcha()
    try:
        redis_store.set('image_code_id_' + image_code_id, text, IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify({'status': 'fail', 'msg': '存储验证码失败', 'error': str(e)})
    # response = make_response(image)
    # response.headers['Content-Type'] = 'image/jpg'
    # 二进制图片转换为base64编码
    base64_data = base64.b64encode(image)
    base64_data = 'data:image/bmp;base64,' + base64_data.decode()
    return jsonify({'status': 'success', 'msg': '获取图片验证码成功', 'data': base64_data})


@app.route('/api/user/register', methods=['POST'])
def register():
    """
    注册
    1.获取注册参数
    2.判断参数是否有值
    3.判断用户名是否重复
    4.判断邮箱是否重复
    5.判断两个密码是否一致
    6.发送邮箱验证码
    7.从redis取邮箱验证码
    8.判断两个验证码是否一致
    9.删除redis验证码
    10.注册信息存入数据库
    :return:
    """
    ip = request.remote_addr
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    repeat_password = request.json.get('repeat_password')
    sms_code = request.json.get('sms_code')
    if not all([username, email, password, repeat_password, sms_code]):
        return jsonify({'status': 'fail', 'msg': '参数错误'})
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'status': 'fail', 'msg': '用户名已存在'})
    emails = User.query.filter_by(email=email).first()
    if emails:
        return jsonify({'status': 'fail', 'msg': '邮箱已存在'})
    if password != repeat_password:
        return jsonify({'status': 'fail', 'msg': '两次密码不一致'})
    # 从redis取邮箱验证码
    real_sms_code = redis_store.get('SMS_' + email)
    if not real_sms_code:
        return jsonify({'status': 'fail', 'msg': '验证码已失效'})
    if sms_code != real_sms_code:
        return jsonify({'status': 'fail', 'msg': '验证码错误'})
    # 删除邮箱验证码
    redis_store.delete('SMS_' + email)
    # 注册信息存入数据库
    user = User()
    user.username = username
    user.email = email
    user.password_hash = user.set_password(password)
    user.ip = ip
    user.create_time = datetime.datetime.now()
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        # 数据保存错误
        return jsonify({'status': 'fail', 'msg': "数据库保存错误"})
    return jsonify({'status': 'success', 'msg': "注册成功"})


@app.route('/api/user/send_mail', methods=['POST'])
def send_mails():
    """
    发送邮箱验证码
    1.参数校验
    2.验证邮箱格式
    3.验证邮箱是否被注册过
    4.发送验证码
    5.保存验证码到redis
    :return:
    """
    email = request.json.get('email')
    # 验证参数
    if not email:
        return jsonify({'status': 'fail', 'msg': '参数错误'})
    # 验证邮箱格式
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return jsonify({'status': 'fail', 'msg': '邮箱格式不正确'})
    # 验证邮箱是否注册过
    emails = User.query.filter_by(email=email).first()
    if emails:
        return jsonify({'status': 'fail', 'msg': '邮箱已存在'})
    # 生成随机验证码
    random_code = "%06d" % random.randint(0, 999999)
    # 发送邮箱验证码
    content = render_template("send_sms_code.html", code=random_code)
    send_mail.delay(subject="论坛邮箱验证码", recipients=[email], html=content)
    # 保存邮箱验证码到redis
    redis_store.set('SMS_' + email, random_code, SMS_CODE_REDIS_EXPIRES)
    return jsonify({'status': 'success', 'msg': '发送邮箱验证码成功'})


@app.route('/api/user/login', methods=['POST'])
def login():
    """
    登录
    1.验证用户是否存在
    2.验证密码正确性

    :return:
    """
    username = request.json.get('username')
    password = request.json.get('password')
    image_code = request.json.get('image_code')
    image_code_id = request.json.get('image_code_id')
    if not all([username, password, image_code, image_code_id]):
        return jsonify({'status': 'fail', 'msg': '参数错误'})
    # 验证用户名是否存在
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User.query.filter_by(email=username).first()
        if not user:
            return jsonify({'status': 'fail', 'msg': '用户名不存在'})
    # 验证密码
    if not user.check_password(password):
        return jsonify({'status': 'fail', 'msg': '密码错误'})
    # 验证图片验证码
    real_image_code = redis_store.get('image_code_id_' + image_code_id)
    if not real_image_code:
        return jsonify({'status': 'fail', 'msg': '图片验证码已过期,请刷新重试'})
    if image_code.upper() != real_image_code.upper():
        return jsonify({'status': 'fail', 'msg': '图片验证码错误'})
    # 删除图片验证码
    redis_store.delete('image_code_id_' + image_code_id)
    # 记录用户登录时间和ip
    user.last_login = datetime.datetime.now()
    user.ip = request.remote_addr
    db.session.commit()
    # 生成token
    auth = Auth()
    token = auth.encode_auth_token(user.id, user.last_login.strftime("%Y-%m-%d %H:%M:%S"))
    return json.dumps({'status': 'success', 'msg': '登录成功', 'token': token}, cls=MyEncoder)