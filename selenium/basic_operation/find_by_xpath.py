from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()

driver.get("https://www.xdclass.net")

print(driver.title)
# 睡眠时间3秒
sleep(6)

# 超链接内容定位
driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div[2]/div[1]/a[2]/div/img").click()