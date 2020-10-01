from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#使用cookie自动登录，（需跟开发确认）
driver.add_cookie({'name':'BAIDUID', 'value':'6625FE7F7DE97A2A68D1654DB89C583E:FG=1'})
driver.add_cookie({'name':'BDUSS', 'value':'k1OYjhwaGZGeU1wcktqSGMwV0duS1dJcVZENFV2ekdTRy1OdENzY1pLYzFWSGRkRVFBQUFBJCQAAAAAAAAAAAEAAABdO71TQm9zY29neGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADXHT101x09dZ'})

sleep(3)
driver.refresh()

# driver.quit()