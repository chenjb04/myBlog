#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2019/11/5 14:56
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019/11/5 14:56
 * @Desc: 用户认证
"""
import jwt
import datetime
import time
from flask import jsonify

from config import Config
from app.models import User


class Auth(object):
    """
    认证
    """
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证token
        :param user_id:
        :param login_time:
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': "ken",
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证token
        :param auth_token:
        :return:
        """
        try:
            payload = jwt.decode(auth_token, Config.SECRET_KEY, options={'verify_exp': False})
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'token过期'
        except jwt.InvalidTokenError:
            return 'token无效'

    def authenticate(self, username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据
        :param username:
        :param password:
        :return:
        """
        user_info = User.query.filter_by(username=username).first()
        if user_info is None:
            return jsonify({'status': 'fail', 'msg': '用户不存在'})
        else:
            if User.check_password(password):
                login_time = int(time.time())
                user_info.last_login = login_time
                User.update(User)
                token = self.encode_auth_token(user_info.id, login_time)
                return jsonify({'status': 'success', 'msg': '登录成功', 'data': token.decode()})
            else:
                return jsonify({'status': 'fail', 'msg': '密码错误'})

    def identify(self, request):
        """
        用户鉴权
        :param request:
        :return:
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_tokenarr = auth_header.split(" ")
            if not auth_tokenarr or auth_tokenarr[0] != 'JWT' or len(auth_tokenarr) != 2:
                result = jsonify({'status': 'fail', 'msg': '请传递正确的验证头信息'})
            else:
                auth_token = auth_tokenarr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = User.get(User, payload['data']['id'])
                    if user is None:
                        result = jsonify({'status': 'fail', 'msg': '找不到改用户信息'})
                    else:
                        if user.last_login == payload['data']['login_time']:
                            result = jsonify({'status': 'success', 'msg': '请求成功', 'data': user.id})
                        else:
                            result = jsonify({'status': 'fail', 'msg': 'token已更改,找不到用户信息'})
                else:
                    result = jsonify({'status': 'fail', 'msg': '', 'data': payload})
        else:
            result = jsonify({'status': 'fail', 'msg': '没有认证token'})
        return result


if __name__ == '__main__':
    auth = Auth()
    token = auth.encode_auth_token(1, "2019/11/6 10:13:20")
    print(str(token))
    # print(auth.decode_auth_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzMwMDY0NDEsImlhdCI6MTU3MzAwNjQzMSwiaXNzIjoia2VuIiwiZGF0YSI6eyJpZCI6MSwibG9naW5fdGltZSI6IjIwMTkvMTEvNiAxMDoxMzoyMCJ9fQ.t4Cen4f9-QOU6fuKsm-CyYo7SAkZCxviRMyDWENi2J8'))