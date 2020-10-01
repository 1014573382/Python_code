# 打开Selenium 课程主页，然后打开1-1课程详情页面，再回到课程主页打开1-5课程详情页面
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.51zxw.net/list.aspx?cid=615")
sleep(3)
# 获取课程主页的窗口句柄
lessions_list_index = driver.current_window_handle

driver.find_element_by_partial_link_text("1-1").click()
sleep(3)
lession1_page = driver.current_window_handle

# 转到课程主页窗口，点击1-5课程
driver.switch_to.window(lessions_list_index)
driver.find_element_by_partial_link_text("1-5").click()
sleep(2)
# 又回到课程1-1页面
driver.switch_to.window(lession1_page)