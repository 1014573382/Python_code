from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from time import sleep

desired_caps = {'platformName': 'Android',
                'deviceName': '127.0.0.1:62025',
                'platformVersion': '7.1.2',
                'noReset': 'Ture',
                'app': r'D:\Python\Python&Appium\app\BaiduMaps_Android_10-20-2_1009176a.apk',
                'appPackage': 'com.baidu.BaiduMap',
                'appActivity': 'com.baidu.baidumaps.WelcomeScreen'
                }

# 传入desires_caps参数与服务器建立会话，appium服务端口号为4723
driver = webdriver.Remote(r'http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# 点击同意进入百度地图
driver.find_element_by_id('com.baidu.BaiduMap:id/ok_btn').click()
# 点击进入地图
driver.find_element_by_id('com.baidu.BaiduMap:id/btn_enter_map').click()
sleep(2)
# 点击‘下一步’
driver.find_element_by_id('com.baidu.BaiduMap:id/pechoin_next').click()
# 点击‘我知道了’
driver.find_element_by_id('com.baidu.BaiduMap:id/pechoin_guide_ok').click()
sleep(2)

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

# 缩小操作
def pinch():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)

    action1.press(x=x*0.2,y=y*0.2).wait(500).move_to(x=x*0.4,y=y*0.4).wait(500).release()
    action2.press(x=x*0.8,y=y*0.8).wait(500).move_to(x=x*0.6,y=y*0.6).wait(500).release()

    pinch_action.add(action1,action2)
    print('start pinch...')
    pinch_action.perform()


# 放大操作
def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x*0.4,y=y*0.4).wait(500).move_to(x=x*0.2,y=y*0.2).wait(500).release()
    action2.press(x=x*0.6,y=y*0.6).wait(500).move_to(x=x*0.8,y=y*0.8).wait(500).release()

    print('start zoom...')
    zoom_action.add(action1, action2)
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()
        sleep(2)

    for i in range(3):
        zoom()
        sleep(2)