#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/15 16:56
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_hogwarts(self):
        self.driver.get("http://testerhome.com/")
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        sleep(2)
        self.driver.find_element(By.CLASS_NAME, "team-name").click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)")



