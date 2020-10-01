from ElementPosition.capability import driver

# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('guoxly')
driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('guoxly')
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("请输入密码")').send_keys('gz091081')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()