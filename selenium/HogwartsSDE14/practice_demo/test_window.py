#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/18 18:09
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from HogwartsSDE14.practice_demo.base_operation import Base


class TestWindows(Base):

    def test_window(self):
        """打开百度首页，点击登录，点击立即注册，跳转到注册页面，
        此时直接输入会报错，因为现在的driver只代表当前的窗口，因此需要进行窗口切换"""
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.CSS_SELECTOR, '#u1>a').click()
        # 打印所有的窗口句柄
        print("点击登录后的所有窗口句柄：", self.driver.window_handles)
        print("当前的窗口句柄：", self.driver.current_window_handle)
        self.driver.find_element(By.CSS_SELECTOR, '[class="pass-reglink pass-link"]').click()
        sleep(1)
        # 点击立即注册打开新页面后，再打印所有窗口句柄
        print("点击立即注册打开新页面后的所有窗口句柄：", self.driver.window_handles)
        print("当前的窗口句柄：", self.driver.current_window_handle)

        # 切换窗口， 取窗口句柄列表中的最后一个值，即当前窗口
        self.driver.switch_to_window(self.driver.window_handles[-1])

        self.driver.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_4__userName').send_keys('guonian')
        self.driver.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_4__phone').send_keys('15222186211')
        sleep(2)

        # 切换回第一个窗口，直接点击‘用户名登录’，并输入用户名和密码
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__userName').send_keys("guonian")
        self.driver.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__password').send_keys("000000")
