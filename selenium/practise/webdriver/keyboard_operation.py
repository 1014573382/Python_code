from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("Selenium")
sleep(2)

#键盘全选操作，ctrl+A
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
sleep(1)
#键盘选择复制或剪切操作
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
#driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')

driver.get("https://www.sogou.com")
driver.implicitly_wait(10)

driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL,'v')
#driver.find_element_by_id("stb").click()
driver.find_element_by_xpath("//input[@id='stb']").click()

