# -*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/03 16:54
from unittest import TestCase
from HogwartsSDE14.test_frame.test_decrypt_api import test_decrypt_base64


class TestApiRequest(TestCase):

    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/data.txt",
        "headers": None,
        "encoding": "base64"
    }

    def test_send(self):
        ar = test_decrypt_base64.ApiRequest()
        print(ar.send(self.req_data))
