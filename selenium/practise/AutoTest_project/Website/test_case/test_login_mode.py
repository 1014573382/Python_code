import unittest
from model import function,myunit
from page_object.LoginPage import *
from test_data import *

class TestLogin(myunit.StartEnd):
    def test_login1_normal(self):
        """username and passwd is normal"""
        print('Start test login1_normal')
        po = LoginPage(self.driver)
        po.login_action(username1, passwd1)
        sleep(3)

        self.assertEqual(po.type_loginPass_hint(), '我的空间')
        function.insert_img(self.driver, 'login1success.png')
        print('Test login1_normal end')

    def test_login2_passwdError(self):
        """username is ok,passwd is error"""
        print('Start test login2_passwdError')
        po = LoginPage(self.driver)
        po.login_action(username2, passwd2)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, 'login2passwdError.png')
        print('Test login2_passwdError end')

    def test_login3_empty(self):
        """username and passwd is empty"""
        print('Start test login3_empty ')
        po =LoginPage(self.driver)
        po.login_action(username3, passwd3)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, 'login3empty.png')
        print('Test login3_empty end')

if __name__ == '__main__':
    unittest.main()


