import unittest
import logging
from basic_fun.desired_capability import appium_desired
from basic_fun import server_start
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        logging.info("================setUp===============")
        driver = appium_desired()
        self.driver = driver

    def tearDown(self):
        logging.info("================tearDown===============")
        sleep(5)
        self.driver.close_app()

