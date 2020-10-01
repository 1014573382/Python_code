import requests
import json
import unittest


class DreamTest(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://api.jisuapi.com/dream/search'
        self.appkey = 'fa1b2caced0f0529'

    def test1(self):
        param_data = {'appkey': 'fa1b2caced0f0529', 'keyword': '梦见哭泣', 'pagenum':1, 'pagesize': 2}
        r = requests.get(self.url, params=param_data)
        result = r.json()
        print(result)

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result['result']['list'][0]['name'], '哭泣')

    def test2(self):
        param_data = {'appkey': 'fa1b2caced0f0529', 'keyword': '分别', 'pagenum':1, 'pagesize': 3}
        r = requests.get(self.url, params=param_data)
        result = r.json()
        print(result)

        self.assertEqual(r.status_code, 200)

    def test3_noappkey(self):
        param_data = {'keyword': '梦见死亡', 'pagenum':1, 'pagesize': 10}
        r = requests.get(self.url, params=param_data)
        result = r.json()
        print(result)

        self.assertEqual(result['status'], '101')
        self.assertEqual(result['msg'], 'APPKEY为空')

    def test4_nokeyword(self):
        param_data = {'appkey': 'fa1b2caced0f0529', 'pagenum':1, 'pagesize': 10}
        r = requests.get(self.url, params=param_data)
        result = r.json()
        print(result)

        self.assertEqual(result['status'], '201')
        self.assertEqual(result['msg'], '关键词为空')

    def test5_post(self):
        from_data = {'appkey': 'fa1b2caced0f0529', 'keyword': '买衣服', 'pagenum':1, 'pagesize': 10}
        r = requests.post(self.url, data=from_data)
        result = r.json()
        print(result)

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result['msg'], "ok")


if __name__ == '__main__':
    unittest.main()