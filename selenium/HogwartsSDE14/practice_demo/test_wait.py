#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2021/02/15 17:35
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_wait(self):
        # self.driver.find_element(By.XPATH, '//*[@class="ember-view"]').click()
        # 点击 所有分类 列表
        self.driver.find_element(By.XPATH, '//*[@id="ember41"]').click()

        # 注意：wait函数后一定要加参数，因为until调用传给它的函数时，会传self._driver参数给这个函数，因此传给until的方法（即此处的wait）一定要有参数来接until传给它的参数
        def wait(x):
            # 查找'//*[@class="table-heading"]' 元素的个数，元素个数 >=1 表示至少出现了一个元素，则返回True,没有此元素则返回False
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        # 传入函数wait，注意不能在wait后加()，加()后wait()表示函数调用
        # 等待10秒内出现‘最新’元素，则点击‘热门’
        WebDriverWait(self.driver, 10).until(wait)

        # 直接使用 expected_conditions模块提供的方法
        WebDriverWait(self.driver, 8).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
