#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/11/01 16:12
import yaml

with open('datas/param.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    # myids 和 mydatas要与conftest.py勾子函数里面的
    # metafunc.mudule.mydatas, ids=metafunc.module.myids 保持一致
    myids = datas.keys()
    mydatas = datas.values()

# param 要与conftest.py 里面勾子函数pytest_generate_tests处理的param保持一致
def test_param(param):
    print(f"param = {param}")
    print("动态生成测试用例")