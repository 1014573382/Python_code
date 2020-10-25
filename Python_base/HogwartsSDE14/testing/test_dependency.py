#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/25 22:23
import pytest
from pytest_dependency import depends


# 想要用例被别的用例依赖，则必须加pytest.mark.dependency()装饰器
# 所依赖的用例执行失败，则当前用例也失败
@pytest.mark.dependency()
@pytest.mark.xfail(reason='deliberate fail')
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    pass


# 如果test_a 用例成功，test_c用例会被执行
# 如果test_a 用例失败，test_c用例会被跳过，不被执行
# depends=[] 列表里面加入依赖的测试用例名称
@pytest.mark.dependency(depends=["test_a"])
def test_c():
    pass

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass

# 依赖多条测试用例
@pytest.mark.dependency(depends=["test_b","test_c"])
def test_e():
    pass