from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.51zxw.net/")

#获取cookie全部内容
cookie = driver.get_cookies()
#打印全部cookie信息
print(cookie)
#打印cookie第一组信息
print(cookie[0])

# 添加cookie
driver.add_cookie({'name': '51zxw', 'value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print("%s--%s" %(cookie['name'],cookie['value']))