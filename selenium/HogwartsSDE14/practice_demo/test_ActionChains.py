#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/17 22:13
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_action_chains(self):
        """模拟点击、双击、右击操作"""
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_dbclick = self.driver.find_element(By.CSS_SELECTOR, '[value="dbl click me"]')
        element_click = self.driver.find_element(By.CSS_SELECTOR, '[value="click me"]')
        element_rightclick = self.driver.find_element(By.CSS_SELECTOR, '[value="right click me"]')

        actions = ActionChains(self.driver)
        actions.click(element_click).perform()
        sleep(1)
        actions.double_click(element_dbclick)
        actions.context_click(element_rightclick)
        sleep(3)
        # 调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列里，当调用perform()方法时，队列中的事件会依次执行
        actions.perform()

    def test_dragdrop(self):
        """模拟拖拽操作"""
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.ID, 'dragger')
        drop_element = self.driver.find_element(By.XPATH, '//body//div[2]')

        actions = ActionChains(self.driver)
        # 拖拽方法，传入起始点和目的点   以下三种方式等效
        actions.drag_and_drop(drag_element, drop_element).perform()
        # actions.click_and_hold(drag_element).release(drop_element).perform()
        # actions.click_and_hold(drag_element).move_to_element(drop_element).release().perform()


    def test_keys(self):
        """模拟键盘操作 可以使用send_keys(Keys.具体键盘按键)进行任何键盘操作 """
        self.driver.get('http://sahitest.com/demo/label.htm')
        element_username1 = self.driver.find_element(By.XPATH, '//body//label/input')
        element_username2 = self.driver.find_element(By.XPATH, '//body//label[2]//input')
        element_username1.click()

        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("guoxl").pause(1)
        action.send_keys(Keys.BACKSPACE).pause(1)

        action.click(element_username2).send_keys("guonian").perform()


