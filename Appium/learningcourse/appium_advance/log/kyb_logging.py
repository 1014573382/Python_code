from appium import webdriver
import yaml
import logging
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO, filename='runlog.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

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

def check_cancelBtn():
    logging.info("check_cancelBtn")

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('cancelBtn is not found!')
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


check_cancelBtn()
check_skipBtn()