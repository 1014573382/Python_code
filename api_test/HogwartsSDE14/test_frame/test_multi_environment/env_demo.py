#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/17 17:42
import requests


class Api:

    data:{
        
    }
     def send(self, data:dict):
         r = requests.request(data["method"], data["url"], data["headers"])
