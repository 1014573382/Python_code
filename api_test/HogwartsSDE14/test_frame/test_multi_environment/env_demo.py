#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/17 17:42
import requests
import yaml

"""
    1）需要二次封装的requests,对请求进行定制化。
	2）将请求的结构体的url从一个写死的ip地址改为一个（任意的）域名。
	3）使用一个env 配置文件，存放各个环境的配置信息。
	4）然后将请求结构体中的url替换为‘env’配置文件中个人选择的url。
	5）将env 配置文件使用yaml进行管理。
"""

class Api:

    with open("get_token.yaml", encoding='utf-8')as f:
        env = yaml.safe_load(f)

    def send(self, data:dict):
         # 替换
         # print(self.env["url"][self.env["default"]])
         # 通过default的值控制替换的url内容
         data["url"] = str(data["url"]).replace("test-studio", self.env["url"][self.env["default"]])
         r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
         return r