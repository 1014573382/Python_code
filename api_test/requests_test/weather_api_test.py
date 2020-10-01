import requests
from urllib import parse


# 构造接口测试数据
data = {'city_code':'101030100'}
url = 'http://t.weather.sojson.com/api/weather/city/%s' %data['city_code']
r = requests.get(url)
# print(r.text)
# 响应结果转化为json格式
response_data = r.json()
print(response_data)

print(response_data['message'])
print('当前日期:',response_data['date'])
print('响应码:',response_data['status'])
print('城市:',response_data['cityInfo']['city'])   # 城市
print('所在省:',response_data['cityInfo']['parent'])  # 省

# 当日天气信息
print('当前温度:',response_data['data']['wendu'])
print('当前湿度:',response_data['data']['shidu'])
print('空气质量:',response_data['data']['quality'])
print('出行建议:',response_data['data']['ganmao'])
print('======================================')
print('以下为具体每日天气预报：')
print('日期:',response_data['data']['forecast'][0]['ymd'])
print(response_data['data']['forecast'][0]['week'])
print('天气:',response_data['data']['forecast'][0]['type'])
print('最低温度:',response_data['data']['forecast'][0]['low'])
print('最高温度:',response_data['data']['forecast'][0]['high'])
print('风向:',response_data['data']['forecast'][0]['fx'])
print('注意事项:',response_data['data']['forecast'][0]['notice'])

print('---------------------------------')
print('日期:',response_data['data']['forecast'][1]['ymd'])
print(response_data['data']['forecast'][1]['week'])
print('天气:',response_data['data']['forecast'][1]['type'])
print('最低温度:',response_data['data']['forecast'][1]['low'])
print('最高温度:',response_data['data']['forecast'][1]['high'])
print('风向:',response_data['data']['forecast'][1]['fx'])
print('注意事项:',response_data['data']['forecast'][1]['notice'])