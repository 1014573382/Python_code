from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

#强制等待
#sleep(10)

#隐性等待，等到网页加载完成，就执行下一步，否则就等到设置时间截止执行下一步
driver.implicitly_wait(10)

print(driver.title)
