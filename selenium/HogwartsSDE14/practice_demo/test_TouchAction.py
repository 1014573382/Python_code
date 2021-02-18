#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/18 17:25
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_touch_action_scrollbottom(self):
        """打开百度，向搜索框中输入‘selenium测试’，通过TouchAction点击搜索框，然后滑动到底部"""
        self.driver.get('http://www.baidu.com')
        ele_input = self.driver.find_element(By.CSS_SELECTOR, '#kw')
        ele_search = self.driver.find_element(By.CSS_SELECTOR, '#su')

        ele_input.send_keys('selenium测试')
        sleep(1)
        action = TouchActions(self.driver)
        # 通过TouchAction点击搜索框，使用tap进行点击
        action.tap(ele_search)
        action.perform()
        # 到搜索结果页后 从搜索输入框开始滑动到底部
        action.scroll_from_element(ele_input, 0, 1300).perform()
        sleep(2)


