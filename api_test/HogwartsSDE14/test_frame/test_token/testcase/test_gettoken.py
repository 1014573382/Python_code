#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/24 22:42
from HogwartsSDE14.test_frame.test_token.api.get_token import GetToken

class TestToken:

    def setup(self):
        self.gettoken = GetToken()

    def test_gettoken(self):
        assert self.gettoken.get_token().json()['errmsg'] == 'ok'
        token = self.gettoken.get_token().json()['access_token']
        print(token)

