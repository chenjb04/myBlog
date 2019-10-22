#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 * @Author: chenjb
 * @Date: 2019-10-22 14:20:20
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019-10-22 14:20:20
 * @Desc: 项目配置信息
'''
import os
from configparser import ConfigParser

import redis


def load_config(path):
    """加载ini文件配置信息"""
    cfg = ConfigParser()
    cfg.read(path)
    sections = cfg.sections()
    conf = {}
    for section in sections:
        conf[section] = {}
        values = cfg.items(section)
        for value in values:
            conf[section][value[0]] = value[1]
    return conf


# 获取ini文件路径
config_ini_path = os.path.join(os.path.dirname(__file__), 'config.ini')
conf = load_config(config_ini_path)


class Config(object):
    """项目基本配置信息"""
    # 秘钥字符串 base64.b32encode(os.urandom(32)) 生成随机秘钥
    SECRET_KEY = 'SHALAES65JA5WDUI3UKM4CKX6XWPHSDGN3ET22VK2HSZZ7HXB5AA===='
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(
        conf.get('MYSQL').get('mysql_user'),
        conf.get('MYSQL').get('mysql_password'),
        conf.get('MYSQL').get('mysql_host'),
        conf.get('MYSQL').get('mysql_port'),
        conf.get('MYSQL').get('mysql_db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动commit
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # redis 配置
    REDIS_HOST = conf.get('REDIS').get('redis_host')
    REDIS_PORT = conf.get('REDIS').get('redis_port')
    REDIS_PASSWORD = conf.get('REDIS').get('redis_pwd')
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_PERMANENT = False  # 设置需要过期
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒
    SESSION_REDIS = redis.StrictRedis(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
