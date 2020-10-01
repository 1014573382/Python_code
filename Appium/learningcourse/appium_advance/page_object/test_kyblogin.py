from learningcourse.appium_advance.page_object.myunit import StartEnd
from learningcourse.appium_advance.page_object.loginView import LoginView
import logging
import unittest

class Test_login(StartEnd):

    def test_login_correct(self):
        logging.info("========test_login_correct=========")
        l = LoginView(self.driver)
        l.login_action('guoxly', 'gz091081')

    def test_login_username_error(self):
        logging.info("======test_login_username_error======")
        l = LoginView(self.driver)
        l.login_action('guoxl', 'gz091081')

    def test_login_password_error(self):
        logging.info("======test_login_password_error======")
        l = LoginView(self.driver)
        l.login_action('guoxly', 'gl1215')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test_login("test_login_correct"))
    suite.addTest(Test_login("test_login_username_error"))
    suite.addTest(Test_login("test_login_password_error"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
