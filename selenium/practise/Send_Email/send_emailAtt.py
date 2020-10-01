import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

smtpserver = 'smtp.163.com'

sender = "guoxiaoli1512@163.com"
auth_code = "gxl1512"   #设置客户端授权码来代替密码登录

receivers = ['15222186256@163.com', 'Guoxiaoli2018@outlook.com']

subject = 'Web selenuim test report'
#读取文件内容
f = open(r'D:\Python\Code\selenium3+python\practise\test_report\test_report.html', 'rb')
content = f.read()
f.close()
#HTML 形式的正文内容
html = MIMEText(content,'html', 'utf-8')

# 创建图片附件
attach_file = open(r'D:\Python\Code\selenium3+python\practise\test_report\login.png', 'rb').read()
#att = MIMEText(attach_file, 'base64', 'utf-8')
att = MIMEImage(attach_file)
#att['Content-Type'] = 'application/octet-stream'
# filename为附件名称，可以任意写，写什么名字，邮件中显示什么名字
att['Content-Disposition'] = 'attachment; filename = "shot.png"'

msg = MIMEMultipart()
msg.attach(html)
msg['Subject'] = subject  #邮件的标题
msg['From'] = sender
msg['To'] = ','.join(receivers)
msg.attach(att)

#连接 登录上smtp服务器
smtp =smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(sender, auth_code)

print("开始发送")
smtp.sendmail(sender, receivers, msg.as_string())
print("发送成功")
smtp.quit()
