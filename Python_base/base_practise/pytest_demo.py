import pytest


def func(x):
    return x * 2

# 进行参数化
@pytest.mark.parametrize('a,b',[
    (1,2),
    (2,4),
    (3,5)  #失败的数据
])
def test_answer1(a, b):
    assert func(a) == b

def test_answer2():
    assert func(2) == 4

# 方法加上pytest的装饰器，可以将此函数传入想要调用此函数得位置
@pytest.fixture()
def login():
    username = 'guoguo'
    return username

def test_one(login):
    print(f"one, username = {login}")

class TestDemo():

    # 调用装饰器，运行测试用例前先调用login方法，并调用它的返回结果
    def test_a(self,login):
        # 加f，引用才生效
        print(f"a username = {login}")

    def test_b(self):
        print("b")

    def test_c(self, login):
        print(f"c, username = {login}")

    # 不是以test开头，不会自动执行
    def fun_d(self):
        print("d")
