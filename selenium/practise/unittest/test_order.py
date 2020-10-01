"""
（1）使用pytest测试框架时候，不需要main（）函数，系统可以自动识别测试用例并执行。
（2）即使包含main（）函数，点击它去执行，也不会去执行main（）函数。
（3）具体是使用哪个测试框架执行，不是通过main（）函数设置的，在别的地方。
"""

from caculator import *
import unittest

class TestStartEnd(unittest.TestCase):
    def setUp(self) -> None:
        print("Start test")

    def tearDown(self) -> None:
        print("Test end")


class TestAdd(TestStartEnd):
    def test_add1(self):
        print("Test add1")
        a = Math(5,6)
        self.assertEqual(a.add(),11)

    def test_add2(self):
        print("Test add2")
        a = Math(8,8)
        self.assertEqual(a.add(),16)


class TestSub(TestStartEnd):
    def test_sub2(self):
        print("Test sub2")
        s = Math(9,3)
        self.assertEqual(s.subtraction(),6)

    def test_sub1(self):
        print("Test sub1")
        s = Math(11,1)
        self.assertEqual(s.subtraction(),10)

if __name__ == '__main__':
    # 默认调用顺序按测试类或测试方法的数字与字母顺序 0~9，A-Z
    # unittest.main()
    # 使用TestSuite可调整测试用例执行的顺序
    suite = unittest.TestSuite()
    suite.addTest(TestSub("test_sub1"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestAdd("test_add1"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
