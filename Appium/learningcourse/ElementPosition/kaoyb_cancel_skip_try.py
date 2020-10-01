from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platformVersion'] = '7.1.2'

desired_caps['app'] = r'D:\Python\Python&Appium\安装包\App\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

# 当前session下不会重置应用的状态，默认false，即不会再次安装和显示升级提示、跳过页面
desired_caps['noReset'] = 'True'

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
check_skipBtn()