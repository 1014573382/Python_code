#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/01/24 22:24
import yaml

from HogwartsSDE14.test_frame.test_token.api.base_api import BaseApi
from string import Template


class GetToken(BaseApi):
    # 加 _ 设置为私有变量
    _corpid = "ww251b76973ac9fac6"
    _corpsecret = "Ccx7iTSoHI9QSySmlbED4T9HP8raNJmYthKlee9kXEE"


    def template(self):
        # 使用Template类的substitute方法 替换yaml文件中的变量
        with open("../api/get_token.yaml",encoding='utf-8')as f:
            # Template需要string类型，使用f.read() 输出string
            # f.read()
            # print(type(f.read()))
            data = {
                "corpid": self._corpid,
                "corpsecret": self._corpsecret
            }
            # re = Template(f.read()).substitute(corpid= self._corpid, corpsecret= self._corpsecret)
            re = Template(f.read()).substitute(data)
            print(re)
            # 把string转换为字典返回
            return yaml.safe_load(re)

    def get_token(self):
        # 把请求信息转化为一个规范的字典结构体
        #  req = {
        #      "method": "get",
        #      "url": r"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #      "params": {
        #          "corpid": self._corpid,
        #          "corpsecret": self._corpsecret
        #      }
        #  }
        req = self.template()
        r = self.request_http(req)
        return r

if __name__ == '__main__':
    gt = GetToken()
    gt.template()