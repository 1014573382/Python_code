#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#收发件人
sender = "guoxiaoli1512@163.com"
receiver = "15222186256@163.com"

#不用密码发送，而是用授权码
auth_code = "gxl1512"

#主题
subject = "自动化测试报告"
#内容，HTML格式
content = """   
<h3>Python邮件发送测试</h3>
<p><a href="https://www.baidu.com">这是一个百度链接</a></p>
"""

#定义发送内容
#msg = MIMEText("<html><h3>这是一封测试邮件</h3></html>",_subtype="html", _charset="utf-8")
msg = MIMEText(content, "html", "utf-8")
msg["Subject"] = subject
msg["from"] = sender
msg["to"] = receiver

try:
	smtp = smtplib.SMTP()
	smtp.connect("smtp.163.com")
	smtp.login(sender,auth_code)
	#发送邮件（发件人邮箱，收件人邮箱，以字符串形式发送内容）
	smtp.sendmail(sender, receiver, msg.as_string())
	print("Send Success")
	smtp.quit()

except:
	print("Send Failure")