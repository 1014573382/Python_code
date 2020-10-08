#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/08 15:38
import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(("a","b"),[(10,20),(5,5)])
    def test_a(self,a, b):
        print(a + b)

    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是: ", env['test'])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是: ", env['dev'])


