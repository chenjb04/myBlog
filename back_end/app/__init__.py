#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2019-10-22 16:31:06
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019-10-22 16:31:06
 * @Desc: 工厂方法创建app
"""
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


from utils.log import setup_log

db = SQLAlchemy()


def create_app(config_name):
    """工厂方法创建app"""
    # 设置日志
    setup_log(config_name)
    app = Flask(__name__)
    # 初始化数据库
    db.init_app(app)
    # 加载配置
    app.config.from_object(config[config_name])
    # 注册蓝图
    from app.blog_api.app_user import app as user_app
    app.register_blueprint(user_app)
    return app

