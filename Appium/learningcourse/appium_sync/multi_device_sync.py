from appium import webdriver
import yaml
from time import ctime
import multiprocessing


with open('desired_caps.yaml', 'r', encoding = 'utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

deviceslist = ['127.0.0.1:62001', '127.0.0.1:62025']

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
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['ip'] = data['ip']

    print('appium port: %s start run %s at %s' %(port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver

#构建desired进程租
desired_process = []

#加载desied进程
for i in range(len(deviceslist)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=appium_desired, args=(deviceslist[i], port))
    desired_process.append(desired)


if __name__ == '__main__':
    # 启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


