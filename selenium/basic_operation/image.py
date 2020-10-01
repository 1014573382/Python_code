from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.jd.com")

#隐性等待，在10秒内网页加载完成即可进行后续操作，否则一直等到10秒为止
driver.implicitly_wait(10)
print(driver.title)

driver.find_element_by_class_name("user_login").click()
#保存屏幕截图到代码目录
driver.get_screenshot_as_file("./login.png")

#找到账户登录并点击
account_login_ele = driver.find_element_by_css_selector("div.login-tab:nth-child(3) > a:nth-child(1)")
ActionChains(driver).click(account_login_ele).perform()

#输入用户名和密码
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("1522218625")

driver.find_element_by_id("nloginpwd").clear()
driver.find_element_by_id("nloginpwd").send_keys("gxl10230701")

#保存截图
driver.get_screenshot_as_file("./logininfo.png")

try:
	driver.find_element_by_id("loginsubmit").click()
except:
	driver.get_screenshot_as_file("./error.png")
