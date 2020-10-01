from learningcourse.ElementPosition.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
# 假定‘添加头像’元素没有id属性，必须通过找到其父元素，通过相对定位方式来进行定位
root_element = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()
