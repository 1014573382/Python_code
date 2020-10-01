from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Firefox()
# driver.get("http://localhost/e/admin/")

username_loc = (By.NAME, 'username')
password_loc = (By.NAME, 'password')
auth_code = (By.ID, 'loginauth')
submit_loc = (By.CSS_SELECTOR,'body > table:nth-child(2) > tbody:nth-child(3) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(2) > input:nth-child(1)')

logout_loc = (By.LINK_TEXT, '退出')

class LoginOut():

    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://localhost/e/admin/")

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def login(self, username, password, loginauth):
        """登录网站"""
        self.find_element(*username_loc).clear()
        self.find_element(*username_loc).send_keys(username)
        sleep(1)
        self.find_element(*password_loc).clear()
        self.find_element(*password_loc).send_keys(password)
        sleep(1)
        self.find_element(*auth_code).send_keys(loginauth)
        sleep(1)
        self.find_element(*submit_loc).click()


    def logout(self):
        """退出登录"""
        self.find_element(*logout_loc).click()
        sleep(2)
        alert_win = self.driver.switch_to_alert()
        alert_win.accept()
        # dismiss表示取消按钮


if __name__ == '__main__':
    lo = LoginOut()
    lo.login('admin', 'admin', 'admin')
    sleep(5)
    lo.logout()
