import logging
import time
import os
import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from basic_fun import desired_capability
from basic_fun import server_start

class Common(object):

    def __init__(self,driver):
        self.driver = driver

    def find_element(self, *location):
        return self.driver.find_element(*location)

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_screensize(self):
        '''获取屏幕尺寸'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)


    def swipe_left(self):
        logging.info('swipe_left')
        l = self.get_screensize()
        y1 = l[1] * 0.5
        x1 = l[0] * 0.9
        x2 = l[0] * 0.2
        self.swipe(x1, y1, x2, y1, 1000)


    # 同意并授权
    authorize_button = (By.ID, 'com.mymoney:id/confirmBtn')
    # 下一页
    nextpage_button = (By.ID, 'com.mymoney:id/next_btn')

    # 开始随手记和选择账本按钮
    begin_button = (By.ID, 'com.mymoney:id/begin_btn')
    select_button = (By.ID, 'com.mymoney:id/select_btn')

    # 不是首次安装，进入app直接点击‘跳过’快速进入app(按钮不起作用)
    skip_btn = (By.ID, 'com.mymoney:id/msplash_skip_tv')


    def auth_and_skip_boot(self):
        '''首次安装之后进行授权并选择开始随手记'''
        logging.info("==========check_authBtn===========")
        try:
            auth_element = self.driver.find_element(*self.authorize_button)
        except NoSuchElementException:
            logging.info("Authozise element is not found!")
            try:
                # WebDriverWait(driver,6).until(lambda x: x.find_element(*self.skip_btn))
                skipBtn = self.driver.find_element(*self.skip_btn)
            except NoSuchElementException:
                logging.info("No skipBtn")
            else:
                logging.info("click skipBtn into app")
                skipBtn.click()
        else:
            logging.info('click authBtn')
            auth_element.click()

            # 显示等待加载出下一步页面
            WebDriverWait(driver, 10).until(lambda x: x.find_element(*self.nextpage_button))
            logging.info('click nextpageBtn')
            # 点击下一页或是直接左滑都可
            self.driver.find_element(*self.nextpage_button).click()
            time.sleep(2)
            self.swipe_left()
            time.sleep(2)
            self.driver.find_element(*self.begin_button).click()


    def get_time(self):
        self.now = time.strftime("%Y-%m-%d_%H-%M-%M")
        return self.now

    def get_screenshot(self, module):
        '''获取截图'''
        time = self.get_time()
        file_path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/_%s_%s.png' %(module, time)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(file_path)

    def get_csv_data(self, csv_file, line):
        '''
         获取csv文件指定行的数据
         csv_file: csv文件路径, line: 数据行数
        '''
        # encoding='utf-8-sig' 防止读出来的数据有非法字符
        with open(csv_file, 'r', encoding='utf-8-sig')as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row



def latest_report(report_dir):
        """传入测试报告存放路径，返回最新测试报告"""
        report_lists = os.listdir(report_dir)
        report_lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
        print('The latest report is:', report_lists[-1])

        latest_file = os.path.join(report_dir, report_lists[-1])
        return latest_file

def send_email(latest_report):
    """邮件发送最新测试报告"""
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    sender = '15222186256@163.com'
    receivers = ['guoxiaoli1512@163.com', 'Guoxiaoli2018@outlook.com']
    auth_code = 'gxl1512'

    subject = 'Android app 自动化测试报告'
    with open(latest_report, 'rb') as report:
        content = report.read()

    # html 邮件正文
    html_content = MIMEText(content, 'html', 'utf-8')

    att = MIMEText(content, 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "test_report.html"'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    msg.attach(html_content)
    msg.attach(att)

    try:
        # 连接 登录smtp服务器
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender, auth_code)

        # 发送邮件（发件人邮箱，收件人邮箱，发送内容）
        logging.info("********Start send email********")
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()
        logging.info("********Send email success********")
    except:
        logging.info("Send email fail")


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    server_start.start_appium_action(host, port)

    driver = desired_capability.appium_desired()
    com = Common(driver)
    com.auth_and_skip_boot()
    com.get_screenshot('beginmymoney')

