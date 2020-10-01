#读取xml子节点
from xml.dom import minidom

dom=minidom.parse('student_info.xml')

root=dom.documentElement

tags=root.getElementsByTagName('student')
#获取所有student标签对应的元素

print(tags[0].nodeName)
print(tags[0].nodeValue)
print(tags[0].nodeType)