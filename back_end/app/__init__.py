#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 * @Author: chenjb
 * @Date: 2019-10-22 16:31:06
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019-10-22 16:31:06
 * @Desc: 工厂方法创建app
'''
from flask import Flask
from config import config


def create_app(config_name):
    """工厂方法创建app"""
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])
    from app.blog_api.app_user import app as user_app
    app.register_blueprint(user_app)
    return app

