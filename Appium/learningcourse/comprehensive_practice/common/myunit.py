import unittest
import logging
from common.desired_caps import appium_desired
from  time import sleep

class StartEnd(unittest.TestCase):

    def setUp(self) -> None:
        logging.info('================setUp===============')
        driver = appium_desired()
        self.driver = driver

    def tearDown(self) -> None:
        logging.info('===============tearDown===============')
        sleep(5)
        self.driver.close_app()
