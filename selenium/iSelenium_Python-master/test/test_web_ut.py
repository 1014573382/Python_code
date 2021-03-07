import allure
import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@allure.feature('Test Baidu WebUI')
class TestIselenium():
    # 读入配置文件
    def get_config(self):
        # 从用户跟目录读取配置文件
        config = configparser.ConfigParser()

        # os.environ['HOMEPATH'] 获取当前用户主目录，以下拼接的路径为 \Users\GUOXIAOLI\iselenium.ini
        # 使用下面方式会报错，原因：read没读到内容，应该是Windows不适用\Users\GUOXIAOLI 此种路径方式
        # print(config.read(os.path.join(os.environ['HOMEPATH'], 'iselenium.ini'), encoding='utf-8'))
        config.read(os.path.join('C:\\Users\\GUOXIAOLI', 'iselenium.ini'), encoding='utf-8')
        config.get('driver', 'chrome_driver')
        return config


    def teardown(self):
        # pass
        self.driver.quit()

    def setup(self):
        config = self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        # executable_path 指定Chromedriver的路径，在iselenium.ini配置文件driver下的 chrome_driver
        # config.get() 获取指定节点下指定option的值
        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       options=chrome_options)
        self.driver.implicitly_wait(6)

    @allure.story('Test key word 今日头条')
    def test_webui_1(self):
        """ 测试用例1，验证'今日头条'关键词在百度上的搜索结果
        """

        self._test_baidu('今日头条', 'test_webui_1')


    @allure.story('Test key word 王者荣耀')
    def test_webui_2(self):
        """ 测试用例2， 验证'王者荣耀'关键词在百度上的搜索结果
        """

        self._test_baidu('王者荣耀', 'test_webui_2')


    def _test_baidu(self, search_keyword, testcase_name):
        """ 测试百度搜索子函数

        :param search_keyword: 搜索关键词 (str)
        :param testcase_name: 测试用例名 (str)
        """

        self.driver.get("https://www.baidu.com")
        print('打开浏览器，访问 www.baidu.com')
        time.sleep(3)
        assert f'百度一下' in self.driver.title

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        print(f'搜索关键词~{search_keyword}')
        time.sleep(2)
        assert(f'{search_keyword}' in self.driver.title)
