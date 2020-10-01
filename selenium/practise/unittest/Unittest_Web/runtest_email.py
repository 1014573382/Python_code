import unittest
from HTMLTestRunner import HTMLTestRunner
import os, time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(latest_report):
    smtpserver = 'smtp.163.com'
    sender = 'guoxiaoli1512@163.com'
    auth_code = 'gxl1512'
    receivers = ['15222186256@163.com', 'Guoxiaoli2018@outlook.com']

    subject = u'登录模块自动化测试'

    f = open(latest_report, 'rb')
    content = f.read()
    f.close()

    # HTML 形式的正文内容
    html = MIMEText(content, 'html', 'utf-8')

    #创建html附件 将测试报告放在附件中发送,	application/octet-stream 表示下载文件类型
    att = MIMEText(content, 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename = "report.html"'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    msg.attach(html)
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, auth_code)

    print("开始发送邮件")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print("发送成功")


def latest_report(report_dir):
    """找到指定路径下最新的测试报告"""
    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(report_dir)
    # 按文件创建时间对该目录下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getctime(report_dir+'\\'+fn))
    print('The new report is:'+ lists[-1])

    # 输出最新报告的路径
    file = os.path.join(report_dir,lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    # 测试用例路径，‘./’表示同一文件夹下
    test_dir = './'
    # 测试报告存放路径
    report_dir = './testreport'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report = report_dir + '/' + now + 'report.html'

    title = u"自动化测试报告"
    desc = u"登录模块测试用例"
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title=title, description=desc)
        runner.run(discover)

    latest_report= latest_report(report_dir)
    send_mail(latest_report)



