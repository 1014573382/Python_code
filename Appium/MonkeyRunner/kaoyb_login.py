from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

print("Connect device...")
device = mr.waitForConnection(5,'127.0.0.1:62025')
# device = mr.waitForConnection()

print("install app")
device.installPackage(r'D:\Python\kaoyan3.1.0.apk')

print("launch app...")
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent=package+'/'+activity

device.startActivity(component=runComponent)
mr.sleep(3)

print("touch cancel button")
device.touch(508,740,'DOWN_AND_UP')
mr.sleep(1)

print("touch skip button")
device.touch(649,45,'DOWN_AND_UP')
mr.sleep(1)

print("input username and password")
device.touch(155,288,'DOWN_AND_UP')
mr.sleep(2)
device.type('guoxly')

device.touch(149,364,'DOWN_AND_UP')
mr.sleep(2)
device.type('gz091081')
mr.sleep(2)

print("touch login button")
device.touch(337,475,'DOWN_AND_UP')


print("takeSnapshot")
screenshot=device.takeSnapshot()
screenshot.writeToFile(r'D:\Python\Code\Appium\MonkeyRunner\kyb.png','png')