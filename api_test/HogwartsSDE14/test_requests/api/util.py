#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/12 23:39
import requests


class Util:

    def get_token(self):
        """
        获取token
        请求方式： GET（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        request_param = {
            "corpid": "ww251b76973ac9fac6",
            "corpsecret": "Ccx7iTSoHI9QSySmlbED4T9HP8raNJmYthKlee9kXEE"
        }

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_param)
        # print(r.json()['access_token'])
        return r.json()['access_token']
        # print(r)