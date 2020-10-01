from time import sleep

class Page():
    """基础页面类"""
    def __init__(self,driver):
        self.base_url = 'http://localhost'
        self.driver = driver
        self.timeout = 10

    # 打开不同的子页面
    def __open(self, url):
        url_ = self.base_url + url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did not land on %s' %url_

    def open(self):
        self.__open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

