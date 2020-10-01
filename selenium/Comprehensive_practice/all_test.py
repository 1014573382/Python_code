import unittest
import HTMLTestRunner
from Comprehensive_practice.login_order import *
from Comprehensive_practice.category import *
import time
from Comprehensive_practice.mail import MailUtils

#创建测试集合
def create_suite():
	print("测试开始")
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(LoginOrderTestCase))
	suite.addTest(unittest.makeSuite(CategoryTestCase))
	return suite


if __name__ == '__main__':
	suite = create_suite()

	#文件名中加了当前时间，为了每次生成不同的测试报告
	#file_prefix = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

	# 创建测试报告的result.html文件，此时还是个空文件
	# wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
	#“./”表示当前路径，也可以指定路径

	#fp = open("D:/Python/"+file_prefix+"_result.html","wb")
	fp = open("D:/Python/result.html","wb")

	# stream定义一个测试报告写入的文件，title就是标题，description就是描述
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"我的 测试报告", description=u"测试用例执行情况")
	runner.run(suite)
	fp.close()
	MailUtils.send_test_report()