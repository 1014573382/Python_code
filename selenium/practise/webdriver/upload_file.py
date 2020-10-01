from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.find_element_by_class_name("soutu-btn").click()
sleep(2)
#设置文件路径，r代表路径转义
driver.find_element_by_css_selector(".upload-pic").send_keys(r"C:\Users\hp\Pictures\Camera Roll\photos\1.jpg")

