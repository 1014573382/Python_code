#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/12 23:18

# # 测试文件
import sys
print(sys.path.append('D:\Python\Python_code\Python_base\HogwartsSDE14'))
import pytest

from pythoncode.calculator import Calculator

class TestCal():

    def setup_class(self):
        self.cal = Calculator()
        print("测试开始")

    def teardown_class(self):
        print("测试结束")

    @pytest.mark.add
    def test_add(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    # 加上ids参数，表示给测试用例起别名
    @pytest.mark.parametrize('a, b, result',[
        (1,2,3),
        (100,50,150),
        (0.1, 0.1, 0.2),
        (-1,-1,-2)
    ]
        ,ids=['int','bignum','float','fushu'])
    @pytest.mark.add
    def test_add1(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    # 加上@pytest.mark.flaky()装饰器，表示失败重试，
    # reruns=3表示失败重试次数，reruns_delay=2表示两次重试之间的延迟时间
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 2 == self.cal.div(4,2)


    # assume断言，前面的失败后，后面的断言还会继续执行
    # assert 断言，第一条失败后，后面将停止运行
    def test_assume(self):

        print("登录操作")
        pytest.assume(1 == 2)
        print("搜索操作")
        pytest.assume(2 == 2)
        print("加购操作")
        pytest.assume(3 == 3)





