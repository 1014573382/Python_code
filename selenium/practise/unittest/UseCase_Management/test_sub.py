from caculator import *
from StartEnd import *

class TestSub(TestStartEnd):
    def test_sub(self):
        u"减法测试"
        print("test sub")
        s = Mathematics(9,4)
        self.assertEqual(s.sub(), 5, msg="结果不相等")

    def test_sub1(self):
        u"减法测试1"
        print("test sub1")
        s1 = Mathematics(10,5)
        self.assertEqual(s1.sub(), 5, msg="结果不相等")


