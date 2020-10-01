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

    # 预期直接失败
    @unittest.expectedFailure
    def test_add2(self):
        print("Test add2")
        a = Math(8,8)
        self.assertEqual(a.add(),16)

@unittest.skip("skip TestSub")
class TestSub(TestStartEnd):
    def test_sub2(self):
        print("Test sub2")
        s = Math(9,3)
        self.assertEqual(s.subtraction(),6)

    def test_sub1(self):
        print("Test sub1")
        s = Math(11,1)
        self.assertEqual(s.subtraction(),10)

class TestOrder(TestStartEnd):
    def test_d(self):
        print("test_d")

    # 条件为假，跳过
    @unittest.skipUnless(1>2,"skip test_b")
    def test_b(self):
        print("test_b")

    @unittest.skipIf(8>5,"skip test_c")
    def test_c(self):
        print("test_c")

    def test_a(self):
        print("test_a")

if __name__ == '__main__':
    unittest.main()


