#-*-coding:UTF-8 -*-
# 使用discover 可以一次调用多个脚本
# test_dir 被测试脚本的路径
# pattern 脚本名称匹配规则

import unittest
#from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time
import os
test_dir = "./"  #表示脚本的当前路径
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # 定义report_dir为文件存放路径
    report_dir = r"D:\Python\Code\selenium3+python\practise\test_report"
    date = time.strftime('%Y-%m-%d %H-%M-%S')
    # 定义报告文件路径和名字，路径为前面定义的report_name，名字为test_report（可自定义），格式为.html
    report_name = report_dir+ '/' + date + 'test_report.html'

    #判断定义的路径目录是否存在，不存在则创建
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    else:
        pass

    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f,
                              title=u"自动化测试报告",
                              description=u"测试用例执行结果" )
        runner.run(discover)
