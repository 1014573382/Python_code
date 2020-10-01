#-*-coding:UTF-8 -*-
import unittest
#定义一个类继承TestCase类
class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.name = "GUOGUO"
		self.age = 24
		print("====setUp method====")

	def tearDown(self):
		print("===tearDown method===")

	def test_one(self):
		print("testcase one")
		self.assertEqual(self.age, 24)

	def test_two(self):
		print("testcase two")
		# isupper()判断是否是大写
		self.assertTrue('guoguo'.isupper(), msg="不是大写")

	def test_three(self):
		print("testcase three")
		self.assertEqual('gxl'.upper(), 'GXL', msg="不相等")

	def test_four(self):
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
	runner = unittest.TextTestRunner(verbosity=1)
	runner.run(suite)



