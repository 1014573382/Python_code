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
import os, time, datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class MailUtils():
	#表示一个类方法，不需要实例化，可以直接调用
	@classmethod
	def send_test_report(cls):		
		#邮件信息配置， 授权码:gxl1512
		sender = '15222186256@163.com'
		receiver = 'guoxiaoli1512@163.com'
		auth_code = 'gxl1512' #设置客户端授权码，不是密码

		smtpserver = 'smtp.163.com'
		subject = '自动化测试报告'

		#读取文件内容
		f = open("D:/Python/result.html", "rb")
		mail_body = f.read()
		f.close()


		#HTML 形式的正文内容
		html = MIMEText(mail_body, _subtype='html', _charset='utf-8')


		#创建html附件 将测试报告放在附件中发送
		att1 = MIMEText(mail_body, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		# filename为附件名称，可以任意写，写什么名字，邮件中显示什么名字
		att1["Content-Disposition"] = 'attachment; filename="report.html"'


		#创建图片附件, os.getcwd() 方法用于返回当前工作目录,等同于./
		img_file = open(os.getcwd()+"/login.png",'rb').read()
		att2 = MIMEImage(img_file)
		#att2.add_header('Content-Disposition','attachment', filename = "test.png")
		#att2.add_header('Content-ID', '<0>')
		att2['Content-Disposition'] = 'attachment; filename = "test.png"'

		#创建一个带附件的实例
		msg = MIMEMultipart()
		msg['Subject'] = subject  #邮件的标题
		msg['from'] = sender
		msg['to'] = receiver
		msg.attach(html)  #将html附加在msg里
		msg.attach(att1)  #新增一个附件
		msg.attach(att2)  #增加图片附件

		try:
			#连接 登录上smtp服务器
			smtp = smtplib.SMTP()
			smtp.connect(smtpserver)
			smtp.login(sender, auth_code)

			#发送邮件（发件人邮箱，收件人邮箱，发送内容）
			smtp.sendmail(sender, receiver, msg.as_string())
			print("发送成功")
			smtp.quit()

		except:
			print("发送失败")
