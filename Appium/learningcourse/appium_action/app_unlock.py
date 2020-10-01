from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platformVersion'] = '7.1.2'
# desired_caps['automationName'] = 'uiautomator2'

desired_caps['app'] = r'D:\Python\Python&Appium\app\mymoney.apk'
desired_caps['appPackage'] = 'com.mymoney'
desired_caps['appActivity'] = 'com.mymoney.biz.splash.SplashScreenActivity'

desired_caps['noReset'] = 'True'
# 传入desires_caps参数与服务器建立会话，appium服务端口号为4723
driver = webdriver.Remote(r'http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)


# 检测是否有每日快速签到入口，有的话点击跳过
try:
    driver.find_element_by_id('com.mymoney:id/splash_skip_tv').click()
except NoSuchElementException:
    pass

# 等待加载出解锁页面的模板元素
WebDriverWait(driver,6).until(lambda x: x.find_element_by_id('com.mymoney:id/go_trans_template_btn'))
TouchAction(driver).press(x=231,y=401).wait(200)\
    .move_to(x=231,y=518).wait(200)\
    .move_to(x=502,y=526).wait(200)\
    .move_to(x=495,y=660).release().perform()
