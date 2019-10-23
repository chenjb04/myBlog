from flask import Blueprint, jsonify, current_app


app = Blueprint(__name__ + 'app', __name__)


@app.route('/api/user/index', methods=['GET'])
def index():
    current_app.logger.debug("eeeeeeeeee")
    return jsonify('hello world')
