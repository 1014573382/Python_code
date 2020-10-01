from Common.start_end import *
from Common.element import *
from time import sleep

class Login(StartEnd):

    def testlogin(self):
        """正常登录"""
        print("登录开始")
        login = Element()
        login.login( 'admin', 'admin', 'admin')
        sleep(3)
        print("登录结束")

if __name__ == '__main__':
    unittest.main()

