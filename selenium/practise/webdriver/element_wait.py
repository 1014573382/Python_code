# 显示等待是针对某一个元素进行相关判定等待
# 隐式等待不针对某一个元素进行等待，全局元素等待
# WebDriverWait 显示等待 针对元素必用
# expected_conditions 预期条件类（里面包含方法可以调用，用于显示等待）
# NoSuchElementException 用于隐式等待抛出异常
# By 用于元素定位

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
sleep(2)

driver.find_element_by_css_selector("#kw").send_keys("Selenium")

#显式等待，每隔0.5秒检查一次，5秒后返超时
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID, 'su')))
element.click()

sleep(2)

