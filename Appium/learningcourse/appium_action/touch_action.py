from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['automationName'] = 'uiautomator2'

desired_caps['app'] = r'D:\Python\Python&Appium\app\mymoney.apk'
desired_caps['appPackage'] = 'com.mymoney'
desired_caps['appActivity'] = 'com.mymoney.biz.splash.SplashScreenActivity'

desired_caps['noReset'] = 'True'
# 传入desires_caps参数与服务器建立会话，appium服务端口号为4723
driver = webdriver.Remote(r'http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y

l = get_size()
print(l)

# 向左滑动
def swipeLeft():
    l = get_size()
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    # 从(x1,y1)滑到(x2,y1),间隔1秒
    driver.swipe(x1,y1,x2,y1, 1000)

# 从上往下滑
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.9)
    y2 = int(l[1] * 0.2)
    driver.swipe(x1, y1, x1, y2, 1000)

# 检测是否首次安装，有引导页面
try:
    #等待启动页面元素，然后向左滑动两次,跳过引导页面
    WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id('com.mymoney:id/next_btn'))
    for i in range(2):
        swipeLeft()
        sleep(1)

    #点击“开始随手记”按钮
    driver.find_element_by_id('com.mymoney:id/begin_btn').click()
except TimeoutException:
    print("无引导页面")

#检测是否有活动页面弹窗，如果有就点击关闭
try:
    closBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closBtn.click()

# 检测是否有每日快速签到入口，有的话点击跳过
try:
    driver.find_element_by_id('com.mymoney:id/splash_skip_tv').click()
except NoSuchElementException:
    pass

sleep(2)
#点击更多菜单
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()

#等待界面菜单加载出来，然后向上滑动
WebDriverWait(driver,6).until(lambda x:x.find_element_by_id("com.mymoney:id/content_container_ly"))
swipeUp()

#点击高级菜单
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("高级")').click()

#点击密码与手势密码菜单
driver.find_element_by_android_uiautomator\
('new UiSelector().text("密码与手势密码")').click()

#点击手势密码保护
driver.find_element_by_android_uiautomator\
('new UiSelector().text("手势密码保护")').click()

#连续滑动两次设置图案密码
for i in range(2):
    TouchAction(driver).press(x=201,y=285).wait(2000)\
        .move_to(x=203,y=431).wait(1000)\
        .move_to(x=506,y=429).wait(1000)\
        .move_to(x=506,y=585).wait(1000).release().perform()
