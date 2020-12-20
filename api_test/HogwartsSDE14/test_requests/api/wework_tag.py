#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/20 14:48
import pytest
import requests
import json

import yaml

from HogwartsSDE14.test_requests.api.util import Util
from HogwartsSDE14.test_requests.api.baseapi import BaseApi


class WeworkTag(BaseApi):

    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../testdata/wework_tag.yaml", encoding='utf-8')as f:
           self.data = yaml.safe_load(f)


    def test_create_tag(self, tagid, tagname):
        """
        创建标签
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :return:
        """
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
        #     "json": {
        #         "tagname": tagname,
        #         "tagid": tagid
        #     }
        # }

        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data['create_tag'])


    def test_update_tag(self, tagid, tagname):
        """
        更新标签名字
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        :return:
        """
        # data = {
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
        #     "json": {
        #         "tagid": tagid,
        #         "tagname": tagname
        #     }
        # }
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data["update_tag"])


    def test_get_taglist(self):
        """
        获取标签列表
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=ACCESS_TOKEN
        :return:
        """
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        # }
        return self.send(self.data["get_taglist"])



    def test_delete_tag(self, tagid):
        """
        删除标签
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        """
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        # }
        # return self.send(data)
        self.params["tagid"] = tagid
        return self.send(self.data["delete_tag"])


    def test_add_tagmember(self, tagid, userlist=None, partylist=None):
        """
        添加标签成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN
        :return:
        """
        if partylist is None:
            partylist = "5"

        if userlist is None:
            userlist = "20201212aa2"
        # data = {
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}",
        #     "json": {
        #         "tagid": tagid,
        #         "userlist": userlist,
        #         "partylist": partylist
        #     }
        # }
        # return self.send(data)
        self.params["tagid"] = tagid
        self.params["partylist"] = partylist
        self.params["userlist"] = userlist
        return self.send(self.data["add_tagmember"])


    def test_get_tagmember(self, tagid):
        """
        获取标签成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :param token:
        :return:
        """
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}"
        }
        return self.send(data)


