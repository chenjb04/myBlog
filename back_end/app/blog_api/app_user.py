from flask import Blueprint, jsonify, current_app, request, abort
from utils.captcha.captcha import captcha
import base64

from app import redis_store, mail
from constants import IMAGE_CODE_REDIS_EXPIRES
from app.models import User
from flask_mail import Message
from utils.celery_task.tasks import send_mail

app = Blueprint(__name__ + 'app', __name__)


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
    6.从redis取邮箱验证码
    7.判断两个验证码是否一致
    :return:
    """
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
    email = User.query.filter_by(email=email).first()
    if email:
        return jsonify({'status': 'fail', 'msg': '邮箱已存在'})
    if password != repeat_password:
        return jsonify({'status': 'fail', 'msg': '两次密码不一致'})


@app.route('/api/user/send_mail', methods=['GET'])
def send_mails():
    send_mail.delay(subject="论坛邮箱验证码",  recipients=['chenjb04@163.com'], body='5555')
    # msg = Message('论坛邮箱验证码python', recipients=['chenjb04@163.com'], body='中国1')
    # mail.send(msg)
    return 'hello'