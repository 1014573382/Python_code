#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/12 23:18

# # 测试文件
import sys
sys.path.append('D:\Python\Python_code\Python_base\HogwartsSDE14')

import yaml
import pytest
from pythoncode.calculator import Calculator

print(sys.path.append('D:\Python\Python_code\Python_base\HogwartsSDE14'))


with open('./datas/calc.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    addids = datas['add'].keys()
    adddatas = datas['add'].values()

    subids = datas['sub'].keys()
    subdatas = datas['sub'].values()


def get_steps():
    with open('./datas/steps.yml')as f:
        steps = yaml.safe_load(f)
    return steps

cal = Calculator()

def steps(a, b, result):
    steps1 = get_steps()
    for step in steps1:
        if 'add' == step:
            assert result == cal.add(a, b)
        elif 'add1' == step:
            assert result == cal.add1(a, b)
        elif 'add2' == step:
            assert result == cal.add2(a, b)


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
    # 以下参数使用yaml进行了参数化，已经移到datas/calc.yml中,然后使用参数mydatas和myids进行的替换
    @pytest.mark.parametrize('a, b, result', adddatas
    #                          [
    #     (1,2,3),
    #     (100,50,150),
    #     (0.1, 0.1, 0.2),
    #     (-1,-1,-2)
    # ]
    #     ,ids=['int','bignum','float','fushu']
        ,ids=addids)
    @pytest.mark.add
    def test_add1(self, a, b, result):
        # cal = Calculator()
        # assert result == self.cal.add(a, b)
        # assert result == self.cal.add1(a, b)
        # assert result == self.cal.add2(a, b)
        steps(a, b, result)

    @pytest.mark.parametrize('a, b, result',subdatas,ids=subids)
    def test_sub(self, result, a , b):
        assert result == self.cal.sub(a, b)



    # 加上@pytest.mark.flaky()装饰器，表示失败重试，
    # reruns=3表示失败重试次数，reruns_delay=2表示两次重试之间的延迟时间
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.div
    def test_div1(self):
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





