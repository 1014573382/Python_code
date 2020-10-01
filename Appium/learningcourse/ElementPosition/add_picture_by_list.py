from ElementPosition.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

# 上传头像
images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
images[6].click()

driver.find_element_by_id('com.tal.kaoyan:id/save').click()