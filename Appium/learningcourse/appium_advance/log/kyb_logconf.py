from appium import webdriver
from time import sleep
import yaml
import logging
import logging.config
from selenium.common.exceptions import NoSuchElementException

# 修改为从配置文件引用日志配置的参数
# 将这些日志配置的参数抽离出来，各个模块需要使用则直接引用即可
CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

with open('../yaml/desired_caps.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    logging.info('start app...')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(3)

def check_cancelBtn():
    logging.info("check_cancelBtn")

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('no cancelBtn')
    else:
        cancelBtn.click()


def check_skipBtn():
    logging.info("check_skipBtn")
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info("skipBtn element is not found!")
    else:
        skipBtn.click()
        sleep(1)


check_cancelBtn()
check_skipBtn()

logging.info('start login')
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('guoxly')
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('gz091081')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
logging.info('login finished')