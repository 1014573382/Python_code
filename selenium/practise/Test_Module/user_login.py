from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://localhost")

driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("guoxl")
sleep(2)

driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("gz091081")
sleep(2)

driver.find_element_by_name("Submit").click()
sleep(5)

driver.find_element_by_link_text('退出').click()
sleep(2)
driver.switch_to_alert().accept()

sleep(2)
driver.quit()


