from appium import webdriver
import yaml
from time import ctime
from learningcourse.appium_sync.kyb_test import KybTest

with open('desired_caps.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# 若是真机，需要用adb devices获取设备的udid,模拟器的话udid和deviceName一样
devicelist = ['127.0.0.1:62001', '127.0.0.1:62025']

def appium_desired(udid, port):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid
    desired_caps['appname'] = data['appname']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    print('appium port: %s start run %s at %s' %(port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)

    k = KybTest(driver)
    k.skip_update_guide()
    return driver


if __name__ == '__main__':
    appium_desired(devicelist[0], 4723)
    appium_desired(devicelist[1], 4725)
