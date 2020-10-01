#有验证码时可直接使用cookie登录，进行登录后的操作
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.xdclass.net")
print(driver.title)
sleep(3)

#driver.add_cookie({"name": "head_img", "value": "https%3A//xd-video-pc-img.oss-cn-beijing.aliyuncs.com/xdclass_pro/default/head_img/9.jpeg"})
#driver.add_cookie({"name":"name", "value": "guo"})
driver.add_cookie({"name": "token", "value": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly90aGlyZHd4LnFsb2dvLmNuL21tb3Blbi92aV8zMi8xWWlhY295SmtLZmFQbjliSk5SRHNtZHA0NUZDTGNlMkJmcThlZ1ExNEM0YXBndlluYWNmaWJaUHppYkpma0dwUXRiQmhCdWE4cUo3d0JIY0JpYWg2WVZ1bmcvMTMyIiwiaWQiOjExMTcwLCJuYW1lIjoi6YOt6YOtIiwiaWF0IjoxNTYyNzUzNjE2LCJleHAiOjE1NjMzNTg0MTZ9.W7l236yaZ8_UxXvQuxNaKJNM61exHT2r7zXihP7i26w"})

#查找对应的课程元素并点击
vedio_ele = driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(3) > div:nth-child(1) > img:nth-child(2)")
vedio_ele.click()
sleep(2)

"""
#获取需要鼠标上移的元素
#hover触发
ActionChains(driver).move_to_element(userinfo_ele).perform()

username_ele = driver.find_element_by_css_selector(".username")
name = username_ele.text
if name == "郭郭":
	print("通过cookie登录成功")
else:
	print("登录失败")
"""
try:
	buy_ele = driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)")
	buy_ele.click()
except:
	driver.get_screenshot_as_file("./error.png")
