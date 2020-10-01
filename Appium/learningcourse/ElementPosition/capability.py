from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
# 模拟器设备
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['automationName'] = 'uiautomator2'
#mx4真机
# desired_caps['platformVersion']='5.1'
# desired_caps['deviceName']='MX4'
# desired_caps['udid']='750BBKL22GDN'

desired_caps['app'] = r'D:\Python\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

# desired_caps['noReset'] = 'True'

# send_keys()传入中文时需要在capability中配置如下内容
# desired_caps['unicodeKeyboard']="True"
# desired_caps['resetKeyboard']="True"

# 传入desires_caps参数与服务器建立会话，appium服务端口号为4723
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)

def check_cancelBtn():
    print("check_cancelBtn")

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()


def check_skipBtn():
    print("check_skipBtn")
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print("no skipBtn")
    else:
        skipBtn.click()


check_cancelBtn()
# check_skipBtn()