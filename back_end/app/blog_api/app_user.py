from flask import Blueprint, jsonify


app = Blueprint(__name__ + 'app', __name__)


@app.route('/api/user/index', methods=['GET'])
def index():
    return jsonify('hello world')
