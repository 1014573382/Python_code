from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("#kw").send_keys("Python")
sleep(2)

search_ele = driver.find_element_by_css_selector("#kw")
#双击操作
ActionChains(driver).double_click(search_ele).perform()
sleep(2)

#右击操作
ActionChains(driver).context_click(search_ele).perform()
sleep(2)

#鼠标悬停
setting_ele = driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(setting_ele).perform()
sleep(2)

driver.quit()