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
import redis
from flask_mail import Mail
from flask_login import LoginManager


from utils.log import setup_log

db = SQLAlchemy()
redis_store = None
mail = Mail()
login_manager = LoginManager()


def create_app(config_name):
    """工厂方法创建app"""
    app = Flask(__name__)
    # 初始化数据库
    db.init_app(app)
    # 加载配置
    app.config.from_object(config[config_name])
    # 初始化邮箱
    mail.init_app(app)
    # 设置日志
    setup_log(config_name)
    # 初始化redis连接
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST,
                                    port=config[config_name].REDIS_PORT,
                                    password=config[config_name].REDIS_PASSWORD,
                                    decode_responses=True)
    # 初始化login_manager
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)

    # 注册蓝图
    from app.blog_api.app_user import app as user_app
    app.register_blueprint(user_app)
    return app

