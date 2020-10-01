import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#登录用户名和密码
username = "15222186256"
password = "gxl10230701"

class LoginOrderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.url = "https://xdclass.net"
        self.driver.get(self.url)


    def tearDown(self) -> None:
        print("单个测试用例结束")
        #退出浏览器
        self.driver.quit()


    def test_login_order(self):
        u"登录并选择课程测试用例"
        driver = self.driver
        login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
        ActionChains(driver).click(login_ele).perform()

        sleep(2)
        # 查找输入框,输入账号，输入框要提前清理里面的数据
        driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
        driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys(username)
        # 查找密码输入框，输入密码
        sleep(1)
        driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
        driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys(password)

        #获取登录按钮并点击
        sleep(1)
        driver.find_element_by_css_selector(".btn").click()

        sleep(2)
        userinfo_ele = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[4]/div[3]/img")
        ActionChains(driver).move_to_element(userinfo_ele).perform()

        #sleep(1)
        driver.implicitly_wait(5)
        #获取用户名元素
        username_ele = driver.find_element_by_css_selector(".username")
        print(username_ele.text)

        name = username_ele.text
        self.assertEqual(name, u"郭郭", msg="登录失败")
        
        vedio_ele = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/a[2]/div/img")
        vedio_ele.click()
        print("进入课程详情页面")
        sleep(3)
        
        """
        #隐性等待，最长等5秒
        driver.implicitly_wait(5)
        #找到“立即购买”按钮
        driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div[1]/div[1]/a").click()
        print("进入下单界面")
        """

if __name__ == '__main__':
    unittest.main()






