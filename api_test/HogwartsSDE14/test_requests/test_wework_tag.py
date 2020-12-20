#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/20 14:48
import pytest
import requests
import json
from HogwartsSDE14.test_requests.api.util import Util


class TestWeworkTag():

    @pytest.fixture(scope='session')
    def token(self):
        self.token = Util().get_token()
        return self.token

    def test_create_tag(self,token):

        """
        创建标签
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {

            "tagname": "产品",
            "tagid": 4
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
                          json=request_body)
        print(r.json())


    def test_update_tag(self,token):
        """
        更新标签名字
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {

            "tagid": 3,
            "tagname": "UI design"

        }

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
                          json=request_body)
        print(r.json())
        return r.json()

    def test_get_taglist(self, token):
        """
        获取标签列表
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=ACCESS_TOKEN
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}")
        print(r.json())


    def test_delete_tag(self, token):
        """
        删除标签
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid=4")
        print(r.json())
        return r.json()


    def test_add_member(self,token):
        """
        添加标签成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "tagid": 1,
            "userlist": ["2020120001", "20201209xxx0","2020080001"],
            "partylist": []
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={token}",
                          json=request_body)
        print(r.json())


    def test_get_tagmember(self,token):
        """
        获取标签成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :param token:
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}&tagid=1")
        print(r.json())

