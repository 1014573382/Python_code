from LoginClass_Para import *
import xlrd
# from selenium import webdriver
# from time import sleep

driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)

#打开excel表格，参数为文件路径
data = xlrd.open_workbook('userinfo.xlsx')
sheet_name = data.sheet_names()  #获取所有sheet的名称,以列表存储
print(sheet_name)
table = data.sheet_by_name(sheet_name[0])  # 通过名称获取表格

rows = table.nrows  #获取总行数
# print(rows)
for i in range(rows):      #获取每一行的数据
    row_content = table.row_values(i)
    # print(row_content[1])
    username = row_content[0]
    password = row_content[1]

    Login().user_login(driver,username,password)
    sleep(5)
    Login().user_logout(driver)
    sleep(4)

    # # 可传入不同用户名和账号进行登录测试
    # Login().user_login(driver,"guoxl","gz091081")
    # sleep(5)
    # Login().user_logout(driver)

driver.quit()