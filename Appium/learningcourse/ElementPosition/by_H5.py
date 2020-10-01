from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:21503'

desired_caps['app'] = r'D:\Python\Python&Appium\app\dr.fone3.2.0.apk'
desired_caps['appPackage'] = 'com.wondershare.drfone'
desired_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'


driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

# 点击Backup菜单
print('click BackupBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

# 等待next菜单，然后点击
WebDriverWait(driver,12).until\
    (lambda x: x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
print('click NextBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

# 等待webview页面加载,webview专门用来显示网页的控件
WebDriverWait(driver,12).until\
    (lambda x: x.find_element_by_class_name('android.webkit.WebView'))
# 获取目前整个页面的环境
contexts = driver.contexts
print(contexts)
now = driver.current_context
print('current_context: %s' %now)
# 输出结果：['NATIVE_APP', 'WEBVIEW_com.android.launcher', 'WEBVIEW_com.wondershare.drfone']

# 需android4.4及以上版本的系统中才会输出更多的webview
print('switch context')
#上面获取到contexts是一个list对象，取这个list的第三个参数
driver.switch_to.context(contexts[2])
print("edit email")
# 正常的网页定位，selenium定位
driver.find_element_by_id('email').send_keys('15222186256@163.com')
# 点击submit按钮
print('click sendBtn')
driver.find_element_by_class_name('btn_send').click()

# 切换context 点击返回
driver.switch_to.context('NATIVE_APP')
# 获取当前的环境，看是否切换成功
now = driver.current_context
print(now)
driver.find_element_by_class_name('android.widget.ImageButton').click()

