import unittest

class TestStartEnd(unittest.TestCase):
    def setUp(self):
        print("Test Start")

    def tearDown(self) -> None:
        print("Test End")
        