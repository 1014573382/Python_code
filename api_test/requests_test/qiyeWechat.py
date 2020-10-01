import requests

request_params = {
    "corpid": "ww251b76973ac9fac6",
    "corpsecret": "Ccx7iTSoHI9QSySmlbED4T9HP8raNJmYthKlee9kXEE"
    }
r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        params=request_params)
print(r.json())