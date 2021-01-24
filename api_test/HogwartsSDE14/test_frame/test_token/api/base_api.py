#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/24 22:23
import requests

class BaseApi:



    def request_http(sel, req):
        # r = requests.request(method="get",url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #                      params={"corpid": self._corpid, "corpsecret": self._corpsecret})
        # 下面等价于上面的写法
        r = requests.request(**req)
        # print(r.json())
        return r

