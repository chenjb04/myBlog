from flask import Blueprint, jsonify, current_app, request, abort, make_response
from utils.captcha.captcha import captcha

from app import redis_store
from constants import IMAGE_CODE_REDIS_EXPIRES


app = Blueprint(__name__ + 'app', __name__)


@app.route('/api/user/image_code', methods=['GET'])
def get_image_code():
    """
    获取图片验证码
    :return:
    """
    image_code_id = request.args.get('image_code_id', None)
    print(image_code_id)
    if not image_code_id:
        return abort(403)
    name, text, image = captcha.generate_captcha()
    try:
        redis_store.set('image_code_id_' + image_code_id, text, IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify({'status': 'fail', 'msg': '存储验证码失败', 'error': str(e)})
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'
    return response


@app.route('/api/user/index', methods=['GET'])
def index():
    current_app.logger.debug("eeeeeeeeee")
    return jsonify('hello world')
