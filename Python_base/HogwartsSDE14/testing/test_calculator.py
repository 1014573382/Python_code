#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/12 23:18

# 测试文件
# import sys
# print(sys.path.append('..'))
import pytest

from HogwartsSDE14.pythoncode.calculator import Calculator

@pytest.mark.add
def test_add():
    cal = Calculator()
    assert 3 == cal.add(1, 2)

@pytest.mark.add
def test_add1():
    cal = Calculator()
    assert 4 == cal.add(2, 2)

@pytest.mark.div
def test_div():
    cal = Calculator()
    assert 2 == cal.div(4,2)

# class TestCalc:
#     def setup_class(self):
#         self.cal = Calculator()


