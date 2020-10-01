from selenium import webdriver
#from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time,csv,os
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://mail.cashwaytech.com")
        self.driver.implicitly_wait(12)

    def tearDown(self) -> None:
        # driver = self.driver
        # driver.quit()
        print("test over")


    def test_login(self):
        """登录模块测试"""
        driver = self.driver
        # 要读取的CSV文件路径
        userinfo = r"D:\Python\Code\userinfo.csv"
        with open(userinfo,'r') as user:
            reader = csv.reader(user)
            for data in reader:
                if reader.line_num == 1:
                    continue
                driver.find_element_by_css_selector("#inputuin").clear()
                driver.find_element_by_css_selector("#inputuin").send_keys(data[0])
                time.sleep(1)
                driver.find_element_by_name("pp").clear()
                driver.find_element_by_name("pp").send_keys(data[1])
                time.sleep(2)
                driver.find_element_by_css_selector("#btlogin").click()
                time.sleep(3)
                print('\n' + '测试项：', data[2])

                if reader.line_num == 5:
                    try:
                        username = driver.find_element_by_css_selector("#useralias").text
                        if username == u'郭小丽':
                            print("登录正常")
                        else:
                            print("登录失败")
                    except:
                        print("提示失败，请确定元素名称是否正确")
                    continue
                try:
                    # assert driver.find_element_by_css_selector(".signup_item_error > div:nth-child(2)").text
                    try:
                        error_message = driver.find_element_by_css_selector(".signup_item_error > div:nth-child(2)").text
                        self.assertEqual(error_message,data[3],msg="预期值与实际不符")
                        print("提示信息正确，实际值与预期值一致")
                        print("预期值：" , data[3])
                        print("实际值：" , error_message)
                    except:
                        print("提示信息错误，预期值与实际值不符")
                        print("预期值：", data[3])
                        print("实际值：", error_message)
                except:
                    print("提示类型错误，请确定元素名称是否正确")

                driver.refresh()
                #driver.implicitly_wait(10)

    # def test_logout(self):
    #     driver = self.driver
    #     driver.find_element_by_css_selector(".AppHeader-profileAvatar").click()
    #     driver.find_element_by_css_selector("a.Button:nth-child(3)").click()

if __name__ == '__main__':
    # 定义测试报告生成的路径
    report_dir = r"D:\Python\Code\selenium3+python\practise\unittest\Unittest_Web\testreport"
    # 获取当前时间
    date = time.strftime('%Y-%m-%d %H-%M-%S')
    #定义报告文件路径和名字，路径为前面定义的report_dir，名字为report（可自定义），格式为html
    report = report_dir +'/' + date + 'report.html'

    # 判断定义的目录是否存在，不存在则创建
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    else:
        pass

    suite = unittest.TestSuite()
    suite.addTest(Login("test_login"))

    # 加 u 防止中文乱码
    title = u"登录模块测试报告"
    desc = u"登录模块测试详情"
    with open(report, 'wb') as f:
        runner = BSTestRunner(stream=f, title=title,description=desc)
        runner.run(suite)


