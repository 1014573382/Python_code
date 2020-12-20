#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/12 14:03
import pytest
import requests
import yaml

from HogwartsSDE14.test_requests.api.baseapi import BaseApi
from HogwartsSDE14.test_requests.api.util import Util


class WeWork(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open('../testdata/wework.yaml', encoding='utf-8')as f:
            self.data = yaml.safe_load(f)

    def test_create(self, userid, mobile, name, department=None):
        """
        创建成员
        请求方式：POST（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department is None:
            department = "3"
        # request_body ={}
        # r = requests.post(
        #     f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     json=request_body)
        # print(r.json())

        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department,
        #         "gender": "1",
        #         "enable": 1,
        #         "email": mobile + "@163.com",
        #         "telephone": "020-123456",
        #         "address": "广州市海珠区新港中路",
        #         "main_department": 1
        #     }
        # }

        self.params["userid"] = userid
        self.params["name"] = name
        self.params["mobile"] = mobile
        self.params["department"] = department
        print(self.data)
        return self.send(self.data["create"])


    def test_get(self, userid):
        """
        获取成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        # print(r.json())
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        # }

        self.params['userid'] = userid
        return self.send(self.data['get'])


    def test_update(self, userid):
        """
        更新成员信息
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        # request_body = { }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #                   json=request_body)

        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         # "name": name,
        #         "department": [5],
        #         "position": "产品研发工程师",
        #         # "mobile": mobile,
        #         "gender": "2",
        #         "is_leader_in_dept": [0],
        #         "enable": 1,
        #         "telephone": "020-1234567",
        #         "address": "成都市锦江区通宝大街",
        #         "main_department": 5
        #     }
        # }

        self.params["userid"] = userid
        return self.send(self.data['update'])

    def test_delete(self, userid):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # r = requests.get(
        #     f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        # return r.json()
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}",
        }
        return self.send(data)


