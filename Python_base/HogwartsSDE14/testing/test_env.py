#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/31 17:14


# 测试用例通过传入 fixture方法，获取测试数据/开发数据
def test_case(cmdoption):
    print("测试环境验证")
    env,datas = cmdoption
    print(f"环境 ：{env}, 数据：{datas}")
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://' + ip + ':' + str(port)
    print(url)