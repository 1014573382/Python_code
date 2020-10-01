import yaml
from appium import webdriver
import logging
import logging.config
import os


# 加载日志配置文件
LOG_CONF = '../config/log.conf'
# fileConfig方法的作用是从ConfigParser格式的文件中读取日志配置，同时如果当前脚本有配置log参数，则覆盖当前log配置选项
logging.config.fileConfig(LOG_CONF)
logging = logging.getLogger()


"""启动APP配置参数"""
def appium_desired():
    with open('../config/mymoney_caps.yaml', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    # desired_caps['platformVersion'] = data['platformVersion']
    # desired_caps['deviceName'] = data['deviceName']
    desired_caps['noReset'] = data['noReset']

    # os.path.dirname(__file__) 获取当前文件所在的目录(即文件的上一级目录)
    # base_path = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_path, 'app', data['appname'])
    # desired_caps['appname'] = app_path

    desired_caps['appname'] = data['appname']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']


    logging.info('start run app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    driver.implicitly_wait(8)
    return driver



if __name__ == '__main__':
    # base_path = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_path, 'app', 'mymoney.apk')
    # print(app_path)
    # print(os.path.join('root', 'test', 'runoob.txt'))

    appium_desired()
