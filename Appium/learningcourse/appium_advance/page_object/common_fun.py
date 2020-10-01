from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):

    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        logging.info("==========check cancelBtn===========")

        try:
            cancel_element = self.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info("update element is not found!")
        else:
            logging.info("click cancelBtn")
            cancel_element.click()


    def check_skipBtn(self):
        logging.info("=============check skipBtn============")

        try:
            skip_element = self.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info("skipBtn element is not found!")
        else:
            skip_element.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()






