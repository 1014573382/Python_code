#-*-coding:UTF-8 -*-
import unittest
import HTMLTestRunner
import time

#定义一个类继承TestCase类
class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.name = "GUOGUO"
		self.age = 24
		print("====setUp method====")

	def tearDown(self):
		print("===tearDown method===")

	def test_one(self):
		u"判断年龄是否相等"
		print("testcase one")
		self.assertEqual(self.age, 24)

	def test_two(self):
		u"判断'guoguo'是不是大写"
		print("testcase two")
		# isupper()判断是否是大写,msg是断言错误的提示信息
		self.assertTrue('guoguo'.isupper(), msg="不是大写")

	def test_three(self):
		u"判断'gxl'变为大写后是否等于'GXL'"
		print("testcase three")
		self.assertEqual('gxl'.upper(), 'GXL', msg="不相等")

	def test_four(self):
		u"判断'four'是不是大写，结果是否是false"
		print("testcase four")
		# 判断是否是大写，‘four’不是大写，因此断言返回成功
		self.assertFalse('four'.isupper())


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(MyTestCase("test_one"))
	suite.addTest(MyTestCase("test_two"))
	suite.addTest(MyTestCase("test_three"))
	suite.addTest(MyTestCase("test_four"))


	#verbosity参数可以控制执行结果的输出，0 是简单报告，1 是一般报告（默认），3 是详细报告
	#默认成功会在每个成功的用例前面有个“.” ，每个失败的用例前面有个“F”

	# TextTestRunner() 文本测试用例运行器
	# run()方法是运行测试套件的测试用例，入参为suite测试套件
	#runner = unittest.TextTestRunner(verbosity=1)
	#runner.run(suite)

	#文件名中加了当前时间，为了每次生成不同的测试报告
	file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
	#print(file_prefix)

	# 创建测试报告的result.html文件，此时还是个空文件
	# wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
	#“./”表示当前路径，也可以指定路径
	fp = open("./"+file_prefix+"result.html","wb")
	# stream定义一个测试报告写入的文件，title就是标题，description就是描述
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"我的 测试报告", description=u"测试用例执行情况")
	
	#运行测试容器中的用例，并将结果写入的报告中
	runner.run(suite)

	#关闭文件流，将HTML内容写进测试报告文件
	fp.close()



