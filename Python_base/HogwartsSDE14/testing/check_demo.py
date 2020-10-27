#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/25 22:54

# 测试pytest 配置文件规则，pytest.ini中加上了
# python_files = check_* test_*
# python_classes = Check_* Test_*
# python_functions = aaa_* test_*
# 则以Check_* 开头的类，aaa_开头的函数都可以被执行（命令行运行pytest 即可 或pytest -vs）

class Check_a():

    def aaa_1(self):
        print("用例aaa_1")

    def aaa_2(self):
        print("用例aaa_2")

    def test_1(self):
        print("用例test_1")
