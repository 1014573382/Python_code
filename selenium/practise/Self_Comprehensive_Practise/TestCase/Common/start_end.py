from selenium import webdriver
import unittest


class StartEnd(unittest.TestCase):

    def setUp(self) -> None:
        # self.driver = browser()
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        print("test start")

    def tearDown(self) -> None:
        print("test over")
        # self.driver.quit()