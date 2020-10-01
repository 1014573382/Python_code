from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()

driver.get("https://www.xdclass.net")

print(driver.title)
# 睡眠时间3秒
sleep(6)

# 超链接内容定位
driver.find_element_by_link_text("工具").click()

# 超链接内容定位，模糊匹配
# driver.find_element_by_partial_link_text("学习")
