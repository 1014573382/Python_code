from learningcourse.mymoney_test.basic_fun.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from learningcourse.mymoney_test.basic_fun import desired_capability
import logging
import time



class LoginView(Common):


    default_ledger = (By.ID, 'com.mymoney:id/account_book_name_tv')
    immediately_login = (By.ID, 'com.mymoney:id/nickname_tv')
    # 登录一次后，得先选择其他登录方式，然后选择账户密码登录
    other_login_way = (By.ID, 'com.mymoney:id/other_login_ways_tv')
    account_password_login = (By.ID, 'com.mymoney:id/account_password_login')

    username = (By.ID, 'com.mymoney:id/username_eact')
    password = (By.ID, 'com.mymoney:id/password_et')

    # 同意隐私政策和登录按钮
    agreeBtn = (By.ID, 'com.mymoney:id/privacy_cb')
    loginBtn = (By.ID, 'com.mymoney:id/login_and_register_action_btn')

    # 15222186hPx
    personal_nickname = (By.ID,'com.mymoney:id/nickname_tv')




    def login_action(self, username, password):
        self.auth_and_skip_boot()
        # 等待加载主页面。判断是否存在默认账本按钮
        WebDriverWait(self.driver,10).until(lambda x: x.find_element(*self.default_ledger))
        self.find_element(*self.default_ledger).click()
        time.sleep(1)

        # 检查是否登录，未登录的话选择立即登录，已登录的话打印当前登录昵称
        logging.info("========Check if the account is logged in==========")
        try:
            nicknameBtn = self.driver.find_element_by_android_uiautomator('new UiSelector().text("15222186hPx")')

        except NoSuchElementException:
            logging.info('Account not logged in')
            logging.info("============start_login_action==============")
            self.find_element(*self.immediately_login).click()
            time.sleep(1)
            self.find_element(*self.other_login_way).click()
            self.find_element(*self.account_password_login).click()
            time.sleep(1)

            # 输入用户名和密码
            self.find_element(*self.username).clear()
            self.find_element(*self.username).send_keys(username)
            self.find_element(*self.password).clear()
            self.find_element(*self.password).send_keys(password)

            # 勾选授权并点击登录
            self.find_element(*self.agreeBtn).click()
            self.find_element(*self.loginBtn).click()
            logging.info("==========Login successful===========")

        else:
            logging.info('The account has already logged.')
            account_info = nicknameBtn.text
            logging.info('The logged account nickname is: %s' %account_info)
            self.get_screenshot('logined_user')


if __name__ == '__main__':
    driver = desired_capability.appium_desired()
    l = LoginView(driver)
    l.login_action('15222186256', 'gz091081')