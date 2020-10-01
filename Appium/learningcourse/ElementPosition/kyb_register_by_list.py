from learningcourse.ElementPosition.capability import driver
import random
from time import sleep

#进入注册界面选择并设置头像
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
images=driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
images[5].click()
sleep(1)
driver.find_element_by_id('com.tal.kaoyan:id/save').click()
sleep(1)

# 注册信息填写
username = 'GXL2019'+str(random.randint(5000,10000))
print('username: %s' %username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

password = 'YCL1215'+str(random.randint(1000,5000))
print('password: %s' %password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

email = 'guoxl'+str(random.randint(1000,9000))+'@163.com'
print('email: %s' %email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
sleep(5)

# 立即注册按钮
# driver.find_element_by_class_name('android.widget.Button').click()
# driver.find_element_by_xpath('//*[@class="android.widget.Button"and@index="8"]').click()
driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
sleep(4)

#院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
sleep(2)
#选择省份
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[2].click()
#选择具体院校--天津大学
driver.find_elements_by_class_name('android.widget.TextView')[0].click()

#专业选择
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
#选择经济学类-统计学-经济统计学
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()

# 点击“进入考研帮”按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
