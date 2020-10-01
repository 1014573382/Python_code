from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md

print("connect devices...")

device = mr.waitForConnection(5,'127.0.0.1:62025')

print("install app")
device.installPackage(r'D:\Python\kaoyan3.1.0.apk')

print("launch app")
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent = package + '/' + activity

device.startActivity(component=runComponent)
