#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/11/15 15:20
import os
import allure
from selenium import webdriver
import time
import pytest

@allure.title("百度搜索功能")
@allure.testcase("https://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data',['allure','pytest','unittest'])
def test_steps_demo(test_data):
    with allure.step("step one: 打开浏览器进入百度首页"):
        driver = webdriver.Firefox()
        driver.get("https://www.baidu.com/")
        driver.implicitly_wait(8)

    with allure.step(f"step two: 在搜索栏输入{test_data}，并点击百度一下"):
        try:
            # driver.find_element_by_id("query").click()
            driver.find_element_by_id("kw").send_keys(test_data)
        except:
            print("输入框获取失败")
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("step three: 保存截图"):
        # 判断保存截图目录是否存在，不存在则创建
        if not os.path.exists("./screenshot"):
            os.makedirs("./screenshot")
        else:
            pass
        driver.save_screenshot("./screenshot/a.png")
        allure.attach.file("./screenshot/a.png", name='搜索结果截图', attachment_type=allure.attachment_type.PNG)
        # allure.attach("<body>首页</body>",'attach with html type', allure.attachment_type.HTML)


    with allure.step("step four: 关闭浏览器退出"):
        driver.quit()
