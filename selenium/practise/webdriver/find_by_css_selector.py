from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("#kw").send_keys("Python")
driver.find_element_by_css_selector("#su").click()
sleep(3)
driver.find_element_by_css_selector(".s_tab_inner > a:nth-child(4)").click()
sleep(2)

size_ele = driver.find_element_by_css_selector("#sizeFilter > div:nth-child(1) > div:nth-child(1)")
ActionChains(driver).move_to_element(size_ele).perform()
sleep(1)
driver.find_element_by_css_selector("ul.filter-item-con > li:nth-child(4)").click()