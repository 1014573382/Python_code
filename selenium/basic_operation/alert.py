from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("file:///D:/Python/Code/selenium3+python/basic_operation/alert.html")

print(driver.title)

sleep(2)

driver.find_element_by_id("alert").click()

#switch_to_alert()切换到弹窗
alert_win = driver.switch_to.alert
sleep(2)
#accept表示接受，即确认
alert_win.accept()

sleep(2)
driver.find_element_by_id("confirm").click()
#切换到弹窗
confirm_ele = driver.switch_to.alert
sleep(2)
#confirm_ele.accept()
#dismiss表示取消按钮
confirm_ele.dismiss()


