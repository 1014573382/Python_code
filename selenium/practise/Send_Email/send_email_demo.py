#coding=utf-8
"""
email模块：支持发送的邮件内容为纯文本、HTML内容、图片、附件。
email模块中有几大类来针对不同的邮件内容形式，常用如下：
MIMEText：（MIME媒体类型）内容形式为纯文本、HTML页面。
MIMEImage：内容形式为图片。
MIMEMultupart：多形式组合，可包含文本和附件

MIMEText(msg,type,chartset)
msg：文本内容
type：文本类型默认为plain（纯文本）
发送HTML格式的时候，修改为html，但同时要求msg的内容也是html的格式。
chartset：文本编码，中文为“utf-8”

"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver = 'smtp.163.com'

#发送邮箱用户名密码
sender = "guoxiaoli1512@163.com"
auth_code = "gxl1512"   #设置客户端授权码来代替密码登录

# receiver = "15222186256@163.com"
receivers = ['15222186256@163.com', 'Guoxiaoli2018@outlook.com']

#发送邮件主题和内容
subject = 'Web selenium 自动化测试报告'
content = '<html><h2 style="color:red">我的测试报告</h2></html>'

#HTML邮件正文
msg = MIMEText(content, 'html', 'utf-8')
# msg['Subject'] = Header(subject,'utf-8')
msg['Subject'] = subject
msg['From'] = sender
# msg['To'] = receiver
msg['To'] = ','.join(receivers)


#连接 登录上smtp服务器
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(sender, auth_code)

#发送邮件（发件人邮箱，收件人邮箱，发送内容）
print("Send begin")
smtp.sendmail(sender, receivers, msg.as_string())
print("Send email end")
smtp.quit()
