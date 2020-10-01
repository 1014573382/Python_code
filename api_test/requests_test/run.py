import unittest
import time
from BSTestRunner import BSTestRunner

# “../”表示当前目录上一级目录的文件或文件夹
testcase_dir = '../test_case'
report_dir = '../reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py')

date = time.strftime('%Y-%m-%d_%H-%M-%S')
report_name = report_dir + '/' + date + ' test_report.html'

# 运行测试用例并生成测试报告
with open(report_name, 'wb') as file:
    runner = BSTestRunner(stream=file, title='Weather API Test Report', description='China city Weather Test Report')
    runner.run(discover)