#读取xml属性节点
from xml.dom import minidom

#加载xml文件
dom=minidom.parse('student_info.xml')

root=dom.documentElement

#获取所有login标签对应的元素
logins=root.getElementsByTagName('login')


for i in range(2):
    print(logins[i].getAttribute("username"))
    print(logins[i].getAttribute("password"))