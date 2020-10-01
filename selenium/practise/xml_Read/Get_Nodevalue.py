#读取xml文本节点
from xml.dom import minidom

dom=minidom.parse('student_info.xml')

#获取文档对象元素
root=dom.documentElement

#获取所有name标签对应的元素
names=root.getElementsByTagName('name')

ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')

for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)
