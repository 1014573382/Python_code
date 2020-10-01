from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)

driver.find_element(By.NAME, 'wd').send_keys("selenuim")
driver.find_element(By.ID, 'su').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, '简书').click()
sleep(2)
driver.quit()