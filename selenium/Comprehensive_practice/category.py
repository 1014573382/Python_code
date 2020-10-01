import unittest
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class CategoryTestCase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(20)
		self.url = "https://xdclass.net"
		self.driver.get(self.url)


	def tearDown(self):
		print("测试结束")
		#退出浏览器
		#self.driver.quit()


	def test_menu(self):
		u"弹出菜单并进入子菜单测试用例"
		driver = self.driver
		#定位到鼠标移动到上面的元素----"后端"菜单
		menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
		#对定位到的元素执行鼠标移动到上面的操作
		ActionChains(driver).move_to_element(menu_ele).perform()
		sleep(2)

		#选中“python”子菜单并点击
		sub_menu_ele = driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(2)")
		sub_menu_ele.click()
		print("进入python子菜单")		


if __name__ == '__main__':
	unittest.main()


