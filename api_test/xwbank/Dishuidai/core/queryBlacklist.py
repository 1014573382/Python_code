import os

import requests
import yaml

# print(os.listdir('../data'))
# print(os.getcwd())

def test_queryBlacklist():

    with open('../data/userinfo.yaml', encoding='utf-8') as f:
        userinfo = yaml.load(f, Loader=yaml.FullLoader)


    r = requests.post(
        'http://132.232.46.158:8080/DSDemoF1/demo/queryBlacklist.do',
        json={
            "appId": "3015",
            "name": userinfo['name'],
            "idNo": userinfo['idNo']
        }
    )
    print(r.json())

if __name__ == '__main__':
    test_queryBlacklist()