#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2019/10/29 16:21
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019/10/29 16:21
 * @Desc:数据库模型
"""
from datetime import datetime
from . import db


class User(db.Model):
    """
    用户模型类
    """
    __tablename__ = 'user'  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    username = db.Column(db.String(64), unique=True, nullable=False)  # 用户名
    email = db.Column(db.String(120), unique=True)  # 邮箱
    phone = db.Column(db.Integer, unique=True)  # 手机号
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    avatar_url = db.Column(db.String(256))  # 头像url地址
    is_admin = db.Column(db.Boolean, default=False)  # 是否是后台管理员
    ip = db.Column(db.String(50))  # ip地址
    location = db.Column(db.String(50))  # 位置
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间

    def to_dict(self):
        """
        结果转换为dict
        :return:
        """
        resp_dict = {
            "id": self.id,
            "username": self.username,
            "avatar_url": self.avatar_url if self.avatar_url else "",
            "phone": self.phone,
            "email": self.email,
            "ip": self.ip,
            "location": self.location,
            "last_login": self.last_login.strftime("%Y-%m-%d %H:%M:%S")
        }
        return resp_dict
