import unittest
from model import function
from BSTestRunner import BSTestRunner
import time


usecase_dir = './test_case'
report_dir = './test_report'

#找到usecase_dir 路径下的以test*.py开头的测试用例
discover = unittest.defaultTestLoader.discover(usecase_dir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = report_dir + '/' + now + 'test_report.html'

print("Start run testcase")
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title=u'自动化测试报告', description='登录模块测试详情')
    runner.run(discover)
print("Write report end")

latest_report = function.last_report(report_dir)
function.send_mail(latest_report)
print("test end!")