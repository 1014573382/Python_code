from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep, ctime

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
sleep(2)
print(driver.title)

#隐性等待，全局元素等待,等到网页加载完成，就执行下一步，否则就等到设置时间截止执行下一步
driver.implicitly_wait(6)

try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("selenium")
    print(ctime())
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())