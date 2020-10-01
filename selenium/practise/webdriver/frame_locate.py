from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("file:///D:/Python/code/selenium3+python/practise/webdriver/Frame.html")

#切换到frame页面内
driver.switch_to.frame("search")

driver.find_element_by_css_selector("#query").send_keys("Python")
sleep(2)

driver.find_element_by_css_selector("#stb").click()
