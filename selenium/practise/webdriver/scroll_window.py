from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(driver.title)
sleep(2)
driver.find_element_by_css_selector("a.mnav:nth-child(4)").click()
driver.implicitly_wait(7)

#将滚动条拖到最底部，scrollTop设置滚动条到顶部的距离
js = "var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(3)

#将滚动条拖到最顶部
js1 = "var action=document.documentElement.scrollTop=0"
driver.execute_script(js1)
sleep(2)