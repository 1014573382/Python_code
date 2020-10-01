from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()

driver.get("https://www.xdclass.net")

print(driver.title)

sleep(3)

# 根据css属性定位（复制css路径：审查元素-》右键-》复制-》css选择器）
driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)").click()