#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/14 22:16


import pytest

# fixture的可选参数scope，默认是function级别的
# @pytest.fixture(scope='session')
# scope='session' 整个项目只执行一次
# scope='module' 每个模块，也就是每个.py文件 只执行一次
# 每个情况下，可整体运行testing目录查看test_login 和test_search中的执行情况

# autouse参数：令autouse=True  即@pytest.fixture(autouse=True)，则不用在具体的方法中
#      传入相应函数（ 如：def test_case3(login):），所有用例都会自动去调用装饰器


# 方法加上pytest的装饰器，可以将此函数传入想要调用此函数得位置
@pytest.fixture(params=['user1', 'user2', 'user3'])
def login(request):
    print("登录方法")
    print(request.param)
    # yield 激活fixture teardown方法
    yield ['username', 'password'] # 相当于return
    print("teardown")