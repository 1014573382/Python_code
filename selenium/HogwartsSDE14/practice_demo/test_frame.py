#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/18 18:09
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from HogwartsSDE14.practice_demo.base_operation import Base


class TestFrame(Base):

    def test_frame(self):
        """模拟frame切换"""
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to_frame('iframeResult')
        # self.driver.switch_to.frame('iframeResult')
        drag_ele = self.driver.find_element(By.CSS_SELECTOR, '#draggable')
        drop_ele = self.driver.find_element(By.CSS_SELECTOR, '#droppable')
        ActionChains(self.driver).drag_and_drop(drag_ele,drop_ele).perform()
        sleep(2)

        # 切换回之前的frame  以下两种方式等效
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to_default_content()
        self.driver.find_element(By.CSS_SELECTOR, '#submitBTN').click()
