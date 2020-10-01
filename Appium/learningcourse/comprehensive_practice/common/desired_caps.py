import yaml
import logging
import logging.config
from appium import webdriver
import os

# 加载日志配置文件
CON_LOG = '../config/log.conf'
# fileConfig方法的作用是从ConfigParser格式的文件中读取日志配置，同时如果当前脚本有配置log参数，则覆盖当前log配置选项
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

"""启动APP配置参数"""
def appium_desired():
    with open('../config/kyb_caps.yaml',encoding='utf-8') as file:
        data = yaml.load(file,Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['appname'])
    # desired_caps['app'] = app_path

    desired_caps['appname'] = data['appname']
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    logging.info('start run app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port'])+'/wd/hub', desired_caps)

    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()

    # with open('../config/kyb_caps.yaml','r',encoding='utf-8') as file:
    #     data = yaml.load(file,Loader=yaml.FullLoader)
    # # os.path.dirname(__file__)获取当前文件的路径
    # base_path = os.path.dirname(os.path.dirname(__file__))
    # print(os.path.dirname(__file__))
    # print(base_path)
    # app_path = os.path.join(base_path, 'app', data['appname'])
    # print(app_path)
