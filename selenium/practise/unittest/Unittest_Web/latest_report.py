import os   #用于访问操作系统功能的模块
report_dir = './testreport'

#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
lists = os.listdir(report_dir)
print(lists)

# lambda表达式，也就是指匿名函数，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用
# lambda [parameter_list] : 表达式
# g = lambda x,y:x + y   g(2,3) --->5
# os.path.getatime(path) 返回最近访问时间（浮点型秒数）
# os.path.getmtime(path)	 返回最近文件修改时间
# os.path.getctime(path)	 返回文件 path 创建时间

#按时间顺序对该目录文件夹下面的文件进行排序
lists.sort(key=lambda fn:os.path.getctime(report_dir+'\\'+fn))
print("The latest report is:" + lists[-1])

# os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
# 输出最新报告的路径
file = os.path.join(report_dir,lists[-1])
print(file)