#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/18 12:02
import pytest


def test_cart1(login):
    print(f"购物车用例1 login={login}")

def test_cart2(login):
    print("购物车用例2")

@pytest.fixture()
def fun():
    print("这是另一个fixture")

# @pytest.mark.parametrize(["a", "b"], [(1,2),(3,4)])
# @pytest.mark.parametrize(('a,b'), [(1,2),(3,4)])
# def test_cart3(a, b):
#     print("购物车用例3")

# 参数化结合fixture使用：
# 正常的情况一：传入值和数据
# 情况二：传入一个fixture方法，将数据传入到fixture方法中，
#         fixture方法使用request参数来接收这组数据，在方法体里面使用
#             '''request.param'''来使用这个数据
# indirect默认false，indirect=True 的话，则可以在参数化中传入一个方法的名字，以下传入的是fixture装饰器方法login
# 后面的方法数据是传入到login方法体里面的

# 下面第一个参数化是传入的fixture方法，第二个是传入值和数据，结果会进行笛卡尔积相乘
@pytest.mark.parametrize('login', [
    ('username1','password1'),
    ('username2','password2')
],indirect=True)
@pytest.mark.parametrize('a,b',[(1,2),(3,4)])
def test_cart3(login,fun,a ,b):
    print("购物车用例3")

# 进行笛卡尔积相乘，各种情况组合
@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6])
def test_data(a, b):
    print(a, b)

