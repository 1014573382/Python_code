from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def latest_report(report_dir):
    """传入测试报告存放路径，返回最新测试报告"""
    lists = os.listdir(report_dir)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("The latest report is: ", lists[-1])

    latest_file = os.path.join(report_dir, lists[-1])
    return latest_file


def send_email(latest_report):
    """邮件发送最新测试报告"""
    smtpserver = "smtp.163.com"
    sender = "guoxiaoli1512@163.com"
    auth_code = "gxl1512"
    receivers = "15222186256@163.com, Guoxiaoli2018@outlook.com"

    with open(latest_report, 'rb') as f:
        content = f.read()

    html_content = MIMEText(content, 'html', 'utf-8')

    att = MIMEText(content, 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename ="test_report"'

    msg = MIMEMultipart()
    msg['Subject'] = u"帝国网站管理后台系统测试报告"
    msg['From'] = sender
    msg['To'] =','.join(receivers)
    msg.attach(html_content)
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,auth_code)

    print("Send email start")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print("Send email success")