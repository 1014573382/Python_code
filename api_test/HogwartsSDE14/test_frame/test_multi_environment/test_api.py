# -*- coding:utf-8 -*-
# @Author : guonian
from unittest import TestCase
from HogwartsSDE14.test_frame.test_multi_environment import env_demo

# @Time : 2021/01/17 17:51
class TestApi(TestCase):
    data = {
        "method": "get",
        "url": "http://test-studio:9999/data.txt",
        "headers": None
    }

    def test_send(self):
        se = env_demo.Api()
        print(se.send(self.data).text)
