#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/18 18:
from selenium import webdriver

class Base():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    def teardowm(self):
        self.driver.quit()
        # pass