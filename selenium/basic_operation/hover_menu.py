from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver = webdriver.Firefox()

#跳转网页
driver.get("https://ai.taobao.com")
print(driver.title)
sleep(6)

#定位到鼠标移动到上面的元素
menu = driver.find_element_by_css_selector(".nav-main > li:nth-child(1) > p:nth-child(1) > a:nth-child(1)")

#对定位到的元素进行鼠标移动到上面的操作
ActionChains(driver).move_to_element(menu).perform()

#选中了菜单
sub_menu = driver.find_element_by_css_selector(".menu-sub > a:nth-child(1)")

sleep(4)
sub_menu.click()
