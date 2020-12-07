#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/02 23:18
import re
import random

import pytest
import requests


def test_create_data():
    "userid, name, mobile"
    # 可考虑用生成器或迭代器，因为数据量大的时候列表会很占内存
    # data = [(str(random.randint(0, 9999999)),
    #          "薛之谦",
    #          str(random.randint(13800000000, 13899900000))) for x in range(3)]

    # 考虑到可能并发执行，会有重复的情况，对上面随机数进行改造
    # %06d 加上x随机生成6位数，用0补够6位
    data = [("202012xx" + str(x),
             "薛之谦",
             "13834%06d"%x) for x in range(20)]
    # print(data)
    return data


class TestWework:

    # 使用fixture，令scope="session"，只会在整个项目只执行一次获取token的请求，不用每次执行下列方法，都去获取token
    @pytest.fixture(scope="session")
    def token(self):
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

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=request_param)
        # print(r.json()['access_token'])
        return r.json()['access_token']
        # print(r)

    @pytest.mark.run(order=1)
    def test_create(self,token, userid, mobile, name, alias, department=None):
        """
        创建成员
        请求方式：POST（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token = self.get_token()
        if department == None:
            department = [1,2]
        request_body = {
            "userid": userid,
            "name": name,
            "alias": alias,
            "mobile": mobile,
            "department": department,
            "gender": "1",
            "enable": 1,
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
            "main_department": 1
        }
        r = requests.post(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
            json=request_body)
        # print(r.json())
        return r.json()

    @pytest.mark.second
    def test_get(self,token, userid):
        """
        获取成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        # print(r.json())
        return r.json()

    @pytest.mark.run(order=3)
    def test_update(self,token, userid, name="薛之谦", mobile='15200007676'):
        """
        更新成员信息
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name,
            "department": [3],
            "position": "软件开发工程师",
            "mobile": mobile,
            "gender": "2",
            "email": "guoxiang1@gzdev.com",
            "is_leader_in_dept": [1],
            "enable": 1,
            "telephone": "020-123456",
            "alias": "襄儿",
            "address": "广州市海珠区新港中路",
            "main_department": 1
        }

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",json=request_body)
        # print(r.json())
        return r.json()

    @pytest.mark.skip
    @pytest.mark.last
    def test_delete(self,token, userid):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        # print(r.json())
        return r.json()


    @pytest.mark.parametrize("userid, name, mobile", test_create_data())
    def test_wework(self,token, userid, name, mobile):
        """
        整体测试
        :param token:
        :return:
        """
        # userid = 'MaoQin12'
        # name = '毛琴'
        # mobile = '13300001122'
        # try:
        #     assert "created" == self.test_create(token, userid, '薛大谦', '谦谦', '13300001122')['errmsg']
        # except AssertionError as e:
        #     print("异常信息：", e.__str__())
        #     if "mobile existed" in e.__str__():
        #         # 提取以：开头，以'结尾的内容，括号里的是提取的内容，取出第一个内容(提取失败，未解决)
        #         re_userid = re.findall(":(.*)'$", e.__str__())[0]
        #         # print(re_userid)
        #         self.test_delete(token, re_userid)
        #         assert "created" == self.test_create(token, userid, '薛大谦', '谦谦', '13300001122')['errmsg']

        assert "created" == self.test_create(token, userid, mobile, name, '谦谦')['errmsg']
        assert name == self.test_get(token, userid)["name"]
        assert "updated" == self.test_update(token, userid)["errmsg"]
        assert "薛之谦" == self.test_get(token, userid)["name"]
        assert "deleted" == self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]



