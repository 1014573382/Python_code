import logging
from learningcourse.comprehensive_practice.baseView.baseView import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import csv
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Common(BaseView):

    # 取消升级和跳过引导按钮
    cancel_upgradeBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    # 登录后浮窗广告取消按钮
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_upgradeBtn(self):
        logging.info("==========check_updateBtn===========")

        try:
            cancel_element = self.find_element(*self.cancel_upgradeBtn)
        except NoSuchElementException:
            logging.info("update element is not found!")
        else:
            logging.info('click cancelBtn')
            cancel_element.click()

    def check_skipBtn(self):
        logging.info("=============check skipBtn============")

        try:
            skip_element = self.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info("skipBtn element is not found!")
        else:
            logging.info('click skipBtn')
            skip_element.click()

    def get_screenSize(self):
        '''获取屏幕尺寸'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeLeft(self):
        logging.info("swipeLeft")
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.9)
        x2 = int(l[0] * 0.3)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def check_market_ad(self):
        '''检测登录或者注册之后的界面浮窗广告'''
        logging.info('=======check_market_ad=============')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' %(module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)


    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        csv_file: csv文件路径, line: 数据行数
        '''
        # encoding='utf-8-sig' 防止读出来的数据有非法字符
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader,1):
                if index == line:
                    return row


def latest_report(report_dir):
    """传入测试报告存放路径，返回最新测试报告"""
    lists = os.listdir(report_dir)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("The latest report is: ", lists[-1])

    latest_file = os.path.join(report_dir, lists[-1])
    return latest_file


def send_email(latest_report):
    """邮件发送最新测试报告"""
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    receivers = ['guoxiaoli1512@163.com', 'Guoxiaoli2018@outlook.com']
    sender = '15222186256@163.com'
    auth_code = 'gxl1512'   #设置客户端授权码来代替密码登录

    subject = 'Android app 自动化测试报告'
    with open(latest_report, 'rb') as report:
        content = report.read()

    # HTML邮件正文
    html_content = MIMEText(content, 'html', 'utf-8')

    # 创建邮件附件
    att = MIMEText(content, 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "test_report.html"'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    msg.attach(html_content)
    msg.attach(att)

    # 连接 登录smtp服务器
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, auth_code)

    # 发送邮件（发件人邮箱，收件人邮箱，发送内容）
    logging.info("********Start send email********")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    logging.info("********Send email success********")


if __name__ == '__main__':
    # driver = appium_desired()
    # com = Common(driver)
    # com.check_upgradeBtn()
    # # com.check_skipBtn()
    # com.swipeLeft()
    # com.swipeLeft()
    # com.getScreenShot('startApp')
    # print(com.get_screenSize())
    # print(com.getTime())

    list = ["这", "是", "一个", "测试","数据"]
    # for i in range(len(list)):
    #     print(i, list[i])
    for index,item in enumerate(list):
        print(index,item)

    for index,item in enumerate(list,2):
        print('索引从2开始：',index,item)