from BasePage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    """登录页面首页"""

    url = '/'

    # 定位器
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME, 'Submit')

    # 用户名输入框元素
    def username_input(self, username):
        self.find_element(*self.username_loc).click()
        self.find_element(*self.username_loc).send_keys(username)

    # 密码输入框元素
    def password_input(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def submit_button(self):
        self.find_element(*self.submit_loc).click()

    # 登录功能模块封装
    def test_user_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_page.username_input(username)
        login_page.password_input(password)
        login_page.submit_button()