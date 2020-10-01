from appium_advance.page_object.desired_caps import appium_desired
from appium_advance.page_object.common_fun import Common
from selenium.webdriver.common.by import By
import logging
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class LoginView(Common):

    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    # 登录后的弹框"我知道了"
    kownBtn = (By.ID, 'com.tal.kaoyan:id/task_no_task')

    def login_action(self, username, password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("===========start login=============")
        logging.info("input username:%s" %username)
        self.find_element(*self.username_type).clear()
        self.find_element(*self.username_type).send_keys(username)
        sleep(1)
        logging.info('input password:%s' %password)
        self.find_element(*self.password_type).send_keys(password)
        sleep(1)

        logging.info('click loginBtn.')
        self.find_element(*self.loginBtn).click()
        try:
            self.find_element(*self.kownBtn)
        except NoSuchElementException:
            logging.info("----------login error----------")
        else:
            logging.info("login finished")

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('guoxly', 'gz091081')

