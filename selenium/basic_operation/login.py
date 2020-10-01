from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver = webdriver.Firefox()

#跳转网页
driver.get("https://www.xdclass.net")

print(driver.title)
sleep(3)

#获取登录框
login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")

#触发点击事件
ActionChains(driver).click(login_ele).perform()

sleep(2)
#查找输入框，输入账号，输入框要提前清理默认的数据 
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("15222186256")
sleep(1)

#查找密码输入框，输入密码
driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("gxl10230701")

sleep(1)
#查找登录按钮并点击
driver.find_element_by_class_name("btn").click()

#判断登录是否成功，逻辑：鼠标移到上面，判断弹窗字符

#获取需要鼠标上移的元素
user_info_ele = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[4]/div[3]/img")

sleep(1)
#hover触发
ActionChains(driver).move_to_element(user_info_ele).perform()

#获取用户名称元素
username_ele = driver.find_element_by_css_selector(".username")

print("===测试结果===")
print("用户名：", username_ele.text)

name = username_ele.text 
if name == u"郭郭":
      print('login OK!')
else:
      print('login fail!')
