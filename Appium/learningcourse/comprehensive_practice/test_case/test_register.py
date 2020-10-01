from common.myunit import StartEnd
from businessView.registerView import RegisterView
import logging
import random
import unittest

class TestRegister(StartEnd):

    def test_user_register(self):
        logging.info("=========test_user_register======")
        r = RegisterView(self.driver)

        username = 'guoxl'+ str(random.randint(1000,9000))
        password = 'gxl1512' + str(random.randint(1000, 9000))
        email = 'guoxl' + str(random.randint(1000, 9000)) + '@163.com'
        self.assertTrue(r.register_action(username, password, email))

if __name__ == '__main__':
    unittest.main()