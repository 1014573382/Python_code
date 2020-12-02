#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/02 23:18

import requests


class TestWework:
    def get_token(self):
        """
        获取token
        请求方式： GET（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww251b76973ac9fac6&corpsecret=Ccx7iTSoHI9QSySmlbED4T9HP8raNJmYthKlee9kXEE")
        print(r.json()['access_token'])
        return r.json()['access_token']
        # print(r)

    def creat(self):
        """
        创建成员
        请求方式：POST（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        access_token = self.get_token()
        request_body = {
            "userid": "2020120001",
            "name": "郭靖",
            "alias": "郭大侠",
            "mobile": "13832140344",
            "department": [2],
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}",json=request_body)
