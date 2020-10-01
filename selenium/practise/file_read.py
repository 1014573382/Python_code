# 新增一行数据
#with open('D:\List.txt', 'a') as f:
    #content = f.readlines()
    #print('tony',34,'男',file=f)

# with open('D:\List.txt', 'r') as f:
#     con = f.readlines()
#     for data in con:
#         print(data)

import csv
stu = ['Mary', 28, 'Tianjin']
stu1 = ['Jack', 25, 'Shanghai']

with open('Stu_info.csv', 'w', newline='') as out:
    #设定写入模式
    csv_write = csv.writer(out, dialect='excel')
    #写入具体内容
    csv_write.writerow(stu)
    csv_write.writerow(stu1)
    print("Write file over.")
