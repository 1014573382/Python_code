import requests


url = 'https://api.jisuapi.com/dream/search'
appkey = 'fa1b2caced0f0529'

param_data = {'appkey': 'fa1b2caced0f0529', 'keyword': '梦见哭泣', 'pagenum':1, 'pagesize': 10}
r = requests.get(url, params=param_data)
print(r.text)
# print(r.json())