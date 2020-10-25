#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/25 22:04

import pytest

# 用例默认执行顺序：自上而下执行
# 对于有上下文依赖关系的测试用例，可通过pytest-ordering来解决。
# pip install pytest-ordering
#
# 可用英文first-eighth,对应数字1-8、 last（-1）,second_to_last（-2）-eighth_to_last（-8）表示：

def test_five():
    assert True

@pytest.mark.second_to_last
def test_three():
    assert True

@pytest.mark.run(order=-1)
def test_four():
    assert True


@pytest.mark.run(order=2)
def test_two():
    assert True

@pytest.mark.first
def test_one():
    assert True