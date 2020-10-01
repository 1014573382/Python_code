# xlrd是读excel，xlwt是写excel的库
import xlrd

#打开excel表格，参数为文件路径
data = xlrd.open_workbook('userinfo.xlsx')
sheet_name = data.sheet_names()  #获取所有sheet的名称,以列表存储
print(sheet_name)
table = data.sheet_by_name(sheet_name[0])  # 通过名称获取表格

rows = table.nrows  #获取总行数
# print(rows)
for i in range(rows):      #获取每一行的数据
    row_content = table.row_values(i)
    print(row_content[1])
    username = row_content[0]
    password = row_content[1]
