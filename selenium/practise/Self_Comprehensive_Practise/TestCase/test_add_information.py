import unittest
from Common import start_end
from Common.element import *


class TestAddInformation(start_end.StartEnd):

    def test_add_news(self):
        u"测试增加新闻"
        print("Test add_news start")
        po = Element()
        po.login('admin', 'admin', 'admin')
        sleep(5)
        po.add_news_action()
        print('Test add_news over')

    def test_add_mediatools(self):
        u"测试媒体工具"
        print("Test add_mediatools start")
        po1 = Element()
        po1.login('admin', 'admin', 'admin')
        sleep(5)
        po1.add_media_tools()
        print('Test add_mediatools over')

"""
    def test_manage_news(self):
        "测试管理信息"
        print("Test manage_news start")
        po = Element()
        po.login('admin', 'admin', 'admin')
        sleep(5)
        po.manage_news_action()
        print('Test manage_news over')
"""


if __name__ == '__main__':
    unittest.main()

