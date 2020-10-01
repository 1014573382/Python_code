#-*-coding:UTF-8 -*-
import unittest
#from HTMLTestRunner import HTMLTestRunner
# 稍微美化的报告
from BSTestRunner import BSTestRunner
import time
# 定义测试用例路径
test_dir = "./search_test"
discover = unittest.defaultTestLoader.discover(test_dir,pattern='search*.py')

if __name__ == '__main__':
    # 存放报告的文件夹
    report_dir = r"D:\Python\Code\selenium3+python\practise\test_report"
    # 报告命名时间格式化
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    # 报告文件完整路径
    report_name = report_dir + '/' + now + 'test_report.html'

    with open(report_name,'wb') as f:
        # stream定义一个测试报告写入的文件，title就是标题，description就是描述
        #runner = HTMLTestRunner(stream=f,title=u'搜索结果测试报告',description=u'测试用例执行情况')
        runner = BSTestRunner(stream=f,title=u'搜索结果测试报告',description=u'测试用例执行情况')
        runner.run(discover)