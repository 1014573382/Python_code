#-*-coding:UTF-8 -*-
import unittest
#定义一个UserTestCase类继承TestCase类
class UserTestCase(unittest.TestCase):

	def tearDown(self):
		print("===tearDown===")

	def setUp(self):
		print("==setUp===")
		self.name = "小D课堂"
		self.age = 28

	def test_name(self):
		print("===调用test_name===")
		print(self.name)
		#断言是否相同, msg是断言错误的提示信息
		self.assertEqual(self.name, "小D课堂", msg="名字不对")

	def test_isupper(self):
		print("===调用test_isupper===")
		#self.assertTrue('xdclass'.isupper(), msg="不是大写")
		self.word = 'sbdjhd'
		self.assertTrue(self.word.isupper(), msg="不是大写")

	def test_age(self):
		print("===调用test_age===")
		self.assertEqual(self.age, 28)



if __name__ == '__main__':
	unittest.main()
