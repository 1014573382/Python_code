#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/11/01 21:04
import allure
import pytest

# 若需要按重要级别来分别执行用例，如上线前把主流程和重要模块都跑一遍，则可通过allure.severity 来附加标记，
# 级别：Trivial不重要（轻微缺陷）,  Minor不太重要（次要缺陷）, Normal正常问题（普通缺陷）,
#      Critical严重（临界缺陷）, Blocker阻塞（中断缺陷）
# 在函数、方法和类上面加 @allure.severity(allure.severity_level.TRIVIAL)
# 执行时，pytest -s -v 文件名 --allure-severities normal,critical


def test_with_no_severity_label():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.MINOR)
def test_with_minor_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical_severity():
    pass

@allure.severity(allure.severity_level.BLOCKER)
def test_with_blocker_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):
    def test_inside_the_normal_severity_test_class(self):
        pass

    # 类里边用例，按具体方法中标记的执行，即下列用例是CRITICAL级别的
    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass


if __name__ == '__main__':
    pytest.main()


