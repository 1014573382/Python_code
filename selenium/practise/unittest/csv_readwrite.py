import csv

# 读取CSV文件，用for循环迭代访问reader，每一行都是一个列表,list中每个元素是一个字符串
with open('userinfo.csv', 'r') as users:
    reader = csv.reader(users)
    for data in reader:
        # 跳过第一行
        if reader.line_num == 1:
            continue
        print(data)
        # data[0] 表示第一列，data[1]表示第二列
        # username = data[0]
        # password = data[1]


user1 = [['Jack', '男', '28'],['Mary', '女', '23']]
# user2 = ['Mary', '女', '23']
# 创建csv文件，并写入内容
with open('user.csv','w', newline='') as user:
    write = csv.writer(user)
    # 写入的内容都是以列表的形式传入函数
    write.writerow(['name', 'sex', 'age'])
    write.writerow(['guoguo','女', '24'])
    # 一次写多行
    write.writerows(user1)
    print("Write file over.")