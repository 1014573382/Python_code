from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")

driver.find_element_by_name("wd").send_keys("薛之谦")

driver.find_element_by_id("su").click()