import sys
script_path = r'D:\Python\Code\Appium\LearningCourse\comprehensive_practice'
sys.path.append(script_path)

import unittest
from BSTestRunner import BSTestRunner
from common import common_funs
import logging
import time


# 指定测试用例和测试报告的路径
testcase_dir = '../test_case'
report_dir = '../report'

#定义报告的文件格式
now_time = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now_time + 'test_report.html'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='test_login.py')
# #找到usecase_dir 路径下的以test*.py开头的测试用例
# discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py')

#运行用例并生成测试报告
with open(report_name, 'wb') as file:
    runner = BSTestRunner(stream=file, title='Kyb Test Report', description='Kyb Andriod App Test Report')
    logging.info("start run testcase...")
    runner.run(discover)

latest_report = common_funs.latest_report(report_dir)
common_funs.send_email(latest_report)

