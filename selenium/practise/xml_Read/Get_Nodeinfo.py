#读取xml元素节点
from xml.dom import minidom

# nodeName 节点名称
# nodeValue 返回文本节点的值
# nodeType  属性以数字值返回指定节点的节点类型：
# 1.如果节点是元素节点，则 nodeType 属性将返回1
# 2.如果节点是属性节点，则 nodeType 属性将返回2

#打开xml文件
dom=minidom.parse('student_info.xml')

#获取文档对象元素
root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)