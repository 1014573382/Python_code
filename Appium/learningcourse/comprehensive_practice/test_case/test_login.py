from businessView.loginView import LoginView
from common.myunit import StartEnd
import unittest
import logging

class TestLogin(StartEnd):

    csv_file = '../data/account.csv'

    # 跳过测试此用例
    # @unittest.skip("test_correct_login")
    def test_correct_login(self):
        u'用户名和密码正确登录'
        logging.info("============test_correct_login===========")
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,1)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    @unittest.skip("test_error_username")
    def test_error_username(self):
        u'用户名错误登录'
        logging.info("============test_error_username===========")
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login_action(data[0],data[1])
        self.assertFalse(l.check_loginStatus())

    # @unittest.skipIf(5 > 3,'skip test')
    def test_error_password(self):
        u'密码错误登录'
        logging.info("============test_error_password===========")
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,2)
        l.login_action(data[0],data[1])
        self.assertFalse(l.check_loginStatus(),msg='login fail!')

if __name__ == '__main__':
    unittest.main()