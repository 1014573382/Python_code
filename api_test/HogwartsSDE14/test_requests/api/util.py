#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/12 23:39
import requests


class Util:
    # 加 _ 设置为私有变量
    _corpid = "ww251b76973ac9fac6",
    _corpsecret = "Ccx7iTSoHI9QSySmlbED4T9HP8raNJmYthKlee9kXEE"

    def get_token(self):
        """
        获取token
        请求方式： GET（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """

        request_param = {
            "corpid": self._corpid,
            "corpsecret": self._corpsecret
        }

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=request_param)
        # print(r.json()['access_token'])
        return r.json()['access_token']
        # print(r)