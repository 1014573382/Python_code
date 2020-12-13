#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/12/02 23:18
import re
import random
import time

import pytest
import requests


def test_create_data():
    "userid, name, mobile"
    # 可考虑用生成器或迭代器，因为数据量大的时候列表会很占内存
    # data = [(str(random.randint(0, 9999999)),
    #          "薛之谦",
    #          str(random.randint(13800000000, 13899900000))) for x in range(3)]

    # 考虑到可能并发执行，会有重复的情况，对上面随机数进行改造
    # %06d 加上x随机生成6位数，用0补够6位,生成11位手机号
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉"
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # timestamp = int(time.time())
    data = [("20201212aaaa" + str(x),
             # "薛之谦",
             str(firstName[random.choice(range(len(firstName)))] + girl[random.choice(range(len(girl)))] + boy[random.choice(range(len(boy)))]),
             "13952%06d"%x) for x in range(3)]
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
    def test_create(self,token, userid, mobile, name, department=None):
        """
        创建成员
        请求方式：POST（HTTPS）
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token = self.get_token()
        if department == None:
            department = [3]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
            "gender": "1",
            "enable": 1,
            "email": mobile + "@gzdev.com",
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
    def test_update(self,token, userid, name):
        """
        更新成员信息
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name,
            "department": [4],
            "position": "软件开发工程师",
            # "mobile": mobile,
            "gender": "2",
            "is_leader_in_dept": [0],
            "enable": 1,
            "telephone": "020-1234567",
            "address": "成都市锦江区通宝大街",
            "main_department": 4
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
        # 创建成员，如果创建过程中手机号重复，则删除重复的成员
        try:
            assert "created" == self.test_create(token, userid, mobile, name)['errmsg']
        except AssertionError as e:
            # print("异常信息：", e.__str__())
            if "mobile existed" in e.__str__():
                # 提取以：开头，以'结尾的内容，括号里的是提取的内容，取出第一个内容
                re_userid = re.findall(":(.*)'", e.__str__())[0]
                # print(re_userid)
                self.test_delete(token, re_userid)
                assert "created" == self.test_create(token, userid, mobile, name)['errmsg']
        # assert "created" == self.test_create(token, userid, mobile, name)['errmsg']
        assert name == self.test_get(token, userid)["name"]
        assert "updated" == self.test_update(token, userid, name)["errmsg"]
        assert name == self.test_get(token, userid)["name"]
        # assert "deleted" == self.test_delete(token,userid)["errmsg"]
        # assert 60111 == self.test_get(token, userid)["errcode"]




