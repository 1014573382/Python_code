#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/02 23:18
import pytest
import requests


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
        print(r.json()['access_token'])
        return r.json()['access_token']
        # print(r)

    @pytest.mark.run(order=1)
    def test_create(self,token, userid, name, alias, mobile, department=None):
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
        print(r.json())
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
        print(r.json())
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
        print(r.json())
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
        print(r.json())
        return r.json()


    def test_wework(self,token):
        """
        整体测试
        :param token:
        :return:
        """
        userid = '2020120003'
        name = '薛之谦'
        assert "created" == self.test_create(token, userid, '薛大谦', '谦谦', '15200001212')['errmsg']
        assert "薛大谦" == self.test_get(token, userid)["name"]
        assert "updated" == self.test_update(token, userid)["errmsg"]
        assert name == self.test_get(token, userid)["name"]
        assert "deleted" == self.test_delete(token,userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]