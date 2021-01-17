#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/03 16:29
import base64
import json

import requests


def test_encode():
    url = "http://127.0.0.1:9999/data.txt"
    r = requests.get(url)
    print(r.content)
    # 调用base64对内容进行解密
    # res = base64.b64decode(r.content)
    res = json.loads(base64.b64decode(r.content))
    print(res)
