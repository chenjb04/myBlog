#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2019/10/30 16:24
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019/10/30 16:24
 * @Desc:celery发送邮箱验证码
"""

from celery import Celery
from flask import Flask
from flask_mail import Message, Mail
from config import config, Config
# from app import mail

app = Flask(__name__)
mail = Mail()
app.config.from_object(config['development'])
mail.init_app(app)


def make_celery(app):
    celery = Celery(app.import_name, backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL)
    celery.conf.update(app.config)

    task_base = celery.Task

    class ContextTask(task_base):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task
def send_mail(subject, recipients, body):
    message = Message(subject=subject, recipients=recipients, body=body, sender=Config.MAIL_USERNAME)
    mail.send(message)
# 开启celery方法
# celery -A 应用路径 （.包路径） worker -l info -P eventlet
# celery -A utils.celery_task.tasks.celery worker -l info -P eventlet
# celery -A utils.celery_task.tasks.celery worker --pool=solo -l info
