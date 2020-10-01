# 数据驱动测试，装载数据的方式可以是列表、字典或是外部文件（txt、csv、xml、excel），
# 目的就是实现数据和脚本的分离

from selenium import webdriver
from time import sleep

class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("Submit").click()
        sleep(2)

    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(2)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://localhost")
    driver.implicitly_wait(10)

    Login().user_login(driver,"guoxl","gz091081")
    sleep(5)
    Login().user_logout(driver)
