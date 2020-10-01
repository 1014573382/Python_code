from LoginPage import *
from selenium import webdriver


driver = webdriver.Firefox()

username = 'guoxl'
password = 'gz091081'
LoginPage(driver).test_user_login(username, password)
sleep(3)
#driver.quit()