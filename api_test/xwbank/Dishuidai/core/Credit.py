import requests
import yaml

with open('./userinfo.yaml') as f:
    userinfo = yaml.load(f, Loader=yaml.FullLoader)

def test_credit():
    r = requests.post(
        "http://132.232.46.158:8080/DSDemoF1/demo/creditApply2api.do",
        json={
            "applicationId": userinfo['applicationId'],
            "applySource": "2",
            "appId": "3015",
            "userInfo": {
                "name": userinfo['name'],
                "cardNo": userinfo['idNo'],
                "phone": userinfo['phone'],
                "telephone": userinfo['phone'],
                "bankCardNo": userinfo['bankCardNo'],
                "userRole": "D",

                "sftpDir": "/data/2001/3015/return/20200915/"
            },
            "creditInfo": {
                "rcOpenId": "10000",
                "amount": 10000000,
                "interestRate": 300,
                "monthInteresRate": 350,
                "yearInterestRate": 400,
                "interestPenaltyRate": 450,
                "startDate": "2020-07-01 12:12:12",
                "endDate": "2020-08-01 12:12:12",
                "lockDownEndTime": "2099-02-01 12:12:12",

                "supMaxInstallment": "3,6,9",
                "supRepayType": "1",
                "preCreditTime": "2020-06-06 18:30:30"
            },
            "didiRcFeature": {
                "onlineActiveLevel6Month": "4",
                "orderActiveLevel30Day": "5",
                "orderActiveLevel6Month": "5",
                "phoneNumStabilityYear": "0",
                "assetScore": "60",
                "carStabilityYear": "0",
                "complainedOrderRateLevel6Month": "4",
                "deviceStabilityYear": "0",
                "gpsApplyCityMD5": "",
                "deviceid": "",
                "longitudeMD5": "",
                "latitudeMD5": "",
                "accountid": "",
                "openIDMD5": "",

                "applyChannel": "1",
                "userRole": "D",
                "productCategory": "2",
                "residentCityStability12Month": "0",
                "riskScore": "600",
                "serviceSta rLevel": "4",
                "workTimeLevel": "5",
                "hasCheat": "0",
                "incomeLevel30Day": "4",
                "incomeLevel6Month": "5",
                "incomeStability6Month": "5",
                "onlineActiveLevel30Day": "4"
            },
            "extendsInfo": ''
        }
    )
