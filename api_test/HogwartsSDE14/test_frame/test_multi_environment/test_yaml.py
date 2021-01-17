#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/17 18:26
import yaml

# 自动将env字典内容转换为yaml文件

def test_yaml():
    env = {
        "default": "test",
        "url": {
            "dev": "127.0.0.1",
            "test": "127.0.0.3"
        }
    }

    with open("data.yaml","w")as f:
        yaml.safe_dump(data=env, stream=f)
