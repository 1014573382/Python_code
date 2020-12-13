#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/12 14:08
import requests

from HogwartsSDE14.test_requests.api.util import Util
from HogwartsSDE14.test_requests.api.wework import WeWork


class TestWework:
    def test_get(self):
        print(WeWork().test_get('20201212aa2'))

    def test_create(self):
        print(WeWork().test_create("20201213aa1", "15222761103", "胡峰"))

    def test_update(self):
        self.result = WeWork().test_update('20201213aa1')['errmsg']
        assert "updated" == self.result

    def test_delete(self):
        assert "deleted" == WeWork().test_delete('20201213aa1')['errmsg']


    # 把获取的token放在session中，就可以在发送请求时不带access_token参数
    def test_session(self):
        s = requests.session()
        s.params = {"access_token": Util().get_token()}
        res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=20201212aa2")
        print(res.json())