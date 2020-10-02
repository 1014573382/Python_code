#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/02 22:47
import pytest


def func(x):
    return x+1

# 进行参数化，下面test_answer方法会依次调用以下参数执行
@pytest.mark.parametrize('a, b',[
    (1,2),
    (10,11),
    ('a','a1')

])
def test_answer(a,b):
    assert func(a) == b

def test_add():
    assert func(4) == 5

# 方法加上pytest的装饰器，可以将此函数传入想要调用此函数得位置
@pytest.fixture()
def login():
    print("登录操作")
    username = 'guonian'
    return username

class TestDemo:
    # 调用login函数
    def test_a(self,login):
        print(f'a username= {login}')

    def test_b(self):
        print('b')

# 如果想用unittest框架运行pytest测试用例：
if __name__ == '__main__':
    # 具体的某一文件
    pytest.main(['test_pytest.py'])
    # 具体到只运行某一个类, '-v'打印详细日志
    # pytest.main(['test_pytest.py::TestDemo', '-v'])