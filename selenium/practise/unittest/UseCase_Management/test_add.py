from caculator import *
from StartEnd import *

#定义测试加法的类继承 TestStartEnd类
class TestAdd(TestStartEnd):
    def test_add(self):
        u"加法测试"
        print("test add")
        a = Mathematics(3,6)
        self.assertEqual(a.add(), 9, msg="结果不相等")

    def test_add1(self):
        u"加法测试1"
        print("test add1")
        a = Mathematics(4,2)
        self.assertNotEqual(a.add(), 7, msg="结果相等")
