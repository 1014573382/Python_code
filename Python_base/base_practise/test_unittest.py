#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/02 21:11
import unittest
from  HTMLTestRunner import HTMLTestRunner

class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def setUpClass(cls) -> None:
        print("所有测试用例执行前一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("所有测试用例执行后执行一次")

    def test_equal(self):
        print('测试相等')
        self.assertEqual(5+4, 9, msg='5+4=9')

    def test_notequal(self):
        print('测试不相等')
        self.assertNotEqual(7*2, 15, msg='7*2不等于15')

    def test_isupper(self):
        print('测试不是大写')
        self.assertFalse('guoguo'.isupper(),msg='不是大写')

    def test_true(self):
        print('测试是大写')
        self.assertTrue('GUGUO'.isupper())


class TestDemo1(unittest.TestCase):

    def setUp(self) -> None:
        print('TestDemo1 setUp')

    def tearDown(self) -> None:
        print('TestDemo1 tearDown')


    def test_equal1(self):
        print('test_equal1 测试相等')
        self.assertEqual(10, 10)

    def test_notequal1(self):
        print('test_notequal1 测试不相等')
        self.assertNotEqual(2*2, 5, msg='2*2不等于5')


if __name__ == '__main__':

    report_file = './report.html'
    report_title = '我的测试报告'
    desc = '一个简单的测试报告'

    # 方法一：执行当前文件所有的unittest测试用例，全部执行
    # unittest.main()

    # 方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件里面，批量执行测试方法
    # 创建一个测试套件，TestSuite()
    # suite = unittest.TestSuite()
    # suite.addTest(TestDemo("test_equal"))
    # suite.addTest(TestDemo("test_isupper"))
    # unittest.TextTestRunner().run(suite)


    # 方法三：执行某个测试类，将测试类添加到测试套件里，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestDemo1)
    suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner().run(suite)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report,title=report_title,description=desc)
        runner.run(suite)


