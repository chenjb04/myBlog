#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 * @Author: chenjb
 * @Date: 2019-11-28 14:00:37
 * @Last Modified by:   chenjb
 * @Last Modified time: 2019-11-28 14:00:37
 * @Desc: 七牛云存储图片
'''
from qiniu import Auth, put_data
from qiniu import BucketManager
from config import Config


def storage(data):
    """
    文件上传
    """
    if not data:
        return None
    try:
        q = Auth(Config.QINIU_ACCESS_KEY, Config.QINIU_SECRET_KEY)
        token = q.upload_token(Config.QINIU_BUCKET_NAME)
        ret, info = put_data(token, None, data)
    except Exception as e:
        raise e
    if info and info.status_code != 200:
        raise Exception("上传文件到七牛失败")
    # 返回七牛中保存的图片名，这个图片名也是访问七牛获取图片的路径
    return ret['key']


def delete_img(key):
    """
    删除单个文件
    """
    try:
        q = Auth(Config.QINIU_ACCESS_KEY, Config.QINIU_SECRET_KEY)
        bucket = BucketManager(q)
        ref, info = bucket.delete(Config.QINIU_BUCKET_NAME, key)
    except Exception as e:
        raise e
    return info


if __name__ == '__main__':
    file_name = r'D:\1.jpg'
    with open(file_name, 'rb') as f:
        url = storage(f.read())
    print(url)
