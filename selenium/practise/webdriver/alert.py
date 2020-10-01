from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)

set_ele = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(set_ele).perform()
sleep(1)

driver.find_element_by_link_text("搜索设置").click()
driver.find_element_by_class_name("prefpanelgo").click()
sleep(2)

#切换到弹窗
alert_win = driver.switch_to_alert()
#accept表示接受，即确认
alert_win.accept()
#dismiss表示取消按钮