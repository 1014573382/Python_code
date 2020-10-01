from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title)
driver.refresh()

# driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_xpath("//input[@name='wd']").send_keys("python")
# //表示当前页面
driver.find_element_by_id("su").click()

driver.get("http://www.sogou.com/")
sleep(3)
driver.set_window_size(1200,800)
sleep(3)
driver.back()
sleep(2)

# driver.forward()
# sleep(2)

#超链接内容定位，元素内容
driver.find_element_by_link_text("Python 基础教程 | 菜鸟教程").click()
driver.implicitly_wait(10)
#模糊匹配
# driver.find_element_by_partial_link_text("基础语法").click()

# driver.quit()
