#模块化驱动测试,把重复的操作代码封装为独立的公共模块
from selenium import webdriver
from time import sleep

class Login():

    def user_login(self,driver):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("guoxl")
        sleep(1)

        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("gz091081")

        driver.find_element_by_name("Submit").click()


    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(2)
        driver.switch_to_alert().accept()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://localhost")
    driver.implicitly_wait(12)

    Login().user_login(driver)
    Login().user_logout(driver)
