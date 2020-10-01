from common.common_funs import Common
import logging
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):

    # 登录界面元素
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_myself = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    # 个人中心下线警告提醒确定按钮
    commitBtn = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    # 退出操作相关元素
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')


    def login_action(self,username, password):
        self.check_upgradeBtn()
        self.check_skipBtn()

        logging.info("============login_action==============")
        logging.info("input username is: %s" %username)
        self.find_element(*self.username_type).clear()
        self.find_element(*self.username_type).send_keys(username)

        logging.info("input password is: %s" %password)
        self.find_element(*self.password_type).send_keys(password)

        logging.info("click loginBtn")
        self.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    def logout_action(self):
        logging.info('=========logout_action==========')
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()

    def check_account_alert(self):
        '''检测账户登录后是否有账户下线提示'''
        logging.info('====check_account_logout_alert======')
        try:
            element = self.driver.find_element(*self.commitBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info('click commitBtn')
            element.click()

    def check_loginStatus(self):
        logging.info('==========check_loginStatus===========')
        self.check_market_ad()
        self.check_account_alert()

        try:
            self.find_element(*self.button_myself).click()
            self.find_element(*self.username)
        except NoSuchElementException:
            logging.error("+++++++++++++++login fail!++++++++++++++++")
            self.getScreenShot('login fail')
            # 在unittest中做断言处理
            return False
        else:
            logging.info("login success!")
            self.logout_action()
            return True


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('guoxly', 'gz091081')
    l.check_loginStatus()





