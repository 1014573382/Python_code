from caculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("Start test.")

    def test_add(self):
        print("加法测试开始")
        j = Math(5,7)
        self.assertNotEqual(j.add(),12,msg="结果相等")

    def test_sub(self):
        print("减法测试开始")
        s = Math(6,2)
        self.assertEqual(s.subtraction(),4,msg="结果不相等")

    def test_assertIn(self):
        # a in b
        self.assertIn("abc","test,abc")

    def test_assertIs(self):
        # 断言成功
        self.assertIs("guoxl","guoxl")
        # 断言失败
        self.assertIs("guoxl","guo")

    def tearDown(self):
        print("Test end.")

if __name__ == '__main__':

    #构造测试类
    suite = unittest.TestSuite()
    suite.addTest(TestMath("test_sub"))
    suite.addTest(TestMath("test_add"))
    suite.addTest(TestMath("test_assertIn"))
    suite.addTest(TestMath("test_assertIs"))

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
