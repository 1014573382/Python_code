# -*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/14 22:01

# import pytest

# pytest 的执行原则：它会先查找同级目录下是否有conftest文件，
# 如果有的话，会先执行conftest中定义的所有方法、规则等，无需导入

# 以下方法已经放入conftest模块中


# # 方法加上pytest的装饰器，可以将此函数传入想要调用此函数得位置
# @pytest.fixture()
# def login():
#     print("登录方法")
#     # yield 激活fixture teardown方法
#     yield ['username', 'password'] # 相当于return
#     print("teardown")

# 测试用例执行之前，先执行login方法
def test_case1(login):
    print(f"case1 login = {login}")

def test_case2():
    print("case2")

def test_case3(login):
    print("case3")

