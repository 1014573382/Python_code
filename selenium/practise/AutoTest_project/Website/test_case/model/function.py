from selenium import webdriver
import os    #用于访问操作系统功能的模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def insert_img(driver,filename):
    """指定截图存放路径，使代码具有可移植性，保存图片的路径根据实际代码运行的路径而改变"""
    # 获取当前模块的路径  os.path.dirname(path)
    # 去掉文件名，返回目录路径
    func_path = os.path.dirname(__file__)
    #print(func_path)

    #获取func_path上一级目录
    base_dir = os.path.dirname(func_path)
    #print(base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换,用'/'代替转义路径'\\'
    base_dir = base_dir.replace('\\','/')
    #print(base_dir)

    # 在字符串路径上调用split，返回一个字符串列表（使用split的参数作为分隔符）
    #以/Website为拆分点拆分为一个列表,取列表的第一个元素赋值给base变量
    base = base_dir.split('/Website')[0]
    #print(base)

    filepath = base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)


def send_mail(latest_report):
    """邮件发送最新报告"""
    smtpserver = 'smtp.163.com'
    sender = 'guoxiaoli1512@163.com'
    auth_code = 'gxl1512'
    receivers = ['15222186256@163.com', 'Guoxiaoli2018@outlook.com']
    subject = u'自动化测试报告'

    with open(latest_report, 'rb') as f:
        content = f.read()

    html_content = MIMEText(content, 'html', 'utf-8')

    att = MIMEText(content, 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename ="test_report"'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    msg.attach(html_content)
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, auth_code)

    print("Start send email")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print("Send email success")


def last_report(report_dir):
    """传入测试报告存放路径，返回最新测试报告"""
    lists = os.listdir(report_dir)
    #print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("The latest report is：" + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    #print(file)
    return file


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver,'sougou.png')
    driver.quit()
