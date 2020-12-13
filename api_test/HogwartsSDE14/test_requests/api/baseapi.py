#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/13 00:01

# 存放公共的方法
import json
import requests


class BaseApi():
    params = {}

    # get和post方法实际上是调用requests.request(),传入的第一个参数请求方法method：get或post等
    # 下面做一个封装，data参数作为一个整体数据，让用户传入是什么方法和参数
    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}",value)
        data = json.loads(raw_data)
        return requests.request(**data).json()