from selenium.webdriver.common.by import By
from time import sleep
from Common.login import *
# 导入Select类，进行下拉框操作
from selenium.webdriver.support.select import Select

class Element(LoginOut):

    # 增加信息模块元素
    add_info = (By.CSS_SELECTOR, 'td.flyoutLink:nth-child(1)')
    # 增加国内‘新闻模块’元素
    domestic_news = (By.CSS_SELECTOR, '#addclassid > option:nth-child(3)')

    #添加基础信息
    title = (By.NAME, 'title')
    attribute = (By.CSS_SELECTOR, 'table.tableborder:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)')
    ftitle = (By.NAME, 'ftitle')
    #推荐和头条下拉框
    recommend = (By.ID, 'isgood')
    firsttitle = (By.ID, 'firsttitle')

    keyboard = (By.NAME, 'keyboard')
    content_introduction = (By.NAME, 'smalltext')
    author = (By.NAME, 'writer')
    information_source = (By.NAME, 'befrom')
    content = (By.CSS_SELECTOR, 'html')


    def add_news_action(self):
        self.find_element(*self.add_info).click()
        sleep(2)
        # 切换到框架进行增加信息操作(通过iframe的 id 进行定位)
        self.driver.switch_to_frame('main')
        self.find_element(*self.domestic_news).click()
        self.find_element(*self.title).send_keys("十九届四中全会在京召开")
        sleep(1)
        self.find_element(*self.attribute).click()
        sleep(1)
        self.find_element(*self.ftitle).send_keys("习近平谈国家治理")
        sleep(1)

        #选择value = "3"的项：通过value属性
        Select(self.find_element(*self.recommend)).select_by_value('3')
        # 选择第五项选项：通过选项的顺序选择，第一个为 0
        Select(self.find_element(*self.firsttitle)).select_by_index('4')
        # 通过选项可见文本选择，选择text="二级头条"的值，即在下拉时我们可以看到的文本
        # Select(self.find_element(*self.firsttitle)).select_by_visible_text('二级头条')
        sleep(1)
        self.find_element(*self.keyboard).send_keys("四中全会")
        sleep(1)
        self.find_element(*self.content_introduction).send_keys("中国共产党第十九届中央委员会第四次全体会议28日上午在京召开。")
        sleep(1)
        self.find_element(*self.author).send_keys("guoxl")
        sleep(1)
        self.find_element(*self.information_source).send_keys("新闻报道")
        sleep(1)
        add_news_windows = self.driver.current_window_handle
        self.driver.switch_to_frame('newstext___Frame')
        self.find_element(*self.content).send_keys("中国共产党第十九届中央委员会第四\
        次全体会议28日上午在京召开。中央委员会总书记习近平代表中央政治局向全会作工作报告，并就《中共中央关于坚\
        持和完善中国特色社会主义制度、推进国家治理体系和治理能力现代化若干重大问题的决定（讨论稿）》向全会作了说明。")
        sleep(1)
        self.driver.switch_to_default_content()

    # 媒体工具
    media_tools = (By.LINK_TEXT, '媒体工具')
    software_name = (By.NAME, 'title')
    support = (By.ID, 'isgood')
    key = (By.NAME, 'keyboard')
    run_env = (By.ID, 'softfj')
    language = (By.ID, 'language')
    brief_introduce = (By.ID, 'softsay')
    addnews = (By.NAME, 'addnews')

    def add_media_tools(self):
        self.find_element(*self.add_info).click()
        sleep(2)
        # 切换到框架进行增加信息操作(通过iframe的 id 进行定位)
        self.driver.switch_to_frame('main')
        # 选择媒体工具
        Select(self.driver.find_element(By.ID, 'addclassid')).select_by_value('41')
        #self.find_element(*self.media_tools).click()
        self.find_element(*self.software_name).send_keys("135编辑器")
        sleep(1)
        Select(self.find_element(*self.support)).select_by_value('2')
        sleep(1)
        self.find_element(*self.key).send_keys("一键排版")
        sleep(1)
        self.find_element(*self.run_env).send_keys("Windows")
        sleep(1)
        Select(self.find_element(*self.language)).select_by_value("简体中文")
        sleep(1)
        self.find_element(*self.brief_introduce).send_keys("135编辑器有丰富的样式，并且支持换色、一键排版、导入文章、生成长图文等功能。")
        sleep(2)
        self.find_element(*self.addnews).click()


    # 管理信息模块元素
    manage_news = (By.CSS_SELECTOR, 'td.flyoutLink:nth-child(2)')
    delete_news = (By.CSS_SELECTOR, 'table.tableborder:nth-child(8) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(8) > div:nth-child(1) > a:nth-child(3)')

    def manage_news_action(self):
        self.find_element(*self.add_info).click()
        sleep(2)
        self.find_element(*self.manage_news).click()
        sleep(2)
        #切换到框架进行增加删除等操作(通过iframe的 id 进行定位)
        self.driver.switch_to_frame('main')
        self.find_element(*self.delete_news).click()
        sleep(1)
        self.driver.switch_to_alert().dismiss()







