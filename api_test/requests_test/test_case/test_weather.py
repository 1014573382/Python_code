import unittest
import requests
from time import sleep


class WeatherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'http://t.weather.sojson.com/api/weather/city'

        # 代理设置，避免ip被封
        self.proxies = {'http':'http://125.118.146.222:6666'}

    def tearDown(self) -> None:
        print('test over')

    def test_weather_chengdu(self):
        '''测试成都天气'''
        data = {'city_code':'101270101'}
        # r = requests.get(self.url + '/' + data['city_code'], proxies=self.proxies)
        r = requests.get(self.url + '/' + data['city_code'])
        result = r.json()
        print(result)
        # 断言
        self.assertEqual(result['status'], 200, msg='response error')
        self.assertEqual(result['cityInfo']['city'],'成都市')
        sleep(3)

    def test_weather_tianjin(self):
        '''测试天津天气'''
        data = {'city_code':'101030100'}
        r = requests.get(self.url + '/' + data['city_code'])
        result = r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['cityInfo']['city'],'天津市')
        sleep(3)

    def test_weather_param_error(self):
        '''测试参数错误'''
        data = {'city_code': '1010301'}
        r = requests.get(self.url + '/' + data['city_code'])
        result = r.json()
        self.assertEqual(result['message'], 'Request resource not found.')
        sleep(3)


if __name__ == '__main__':
    unittest.main()

