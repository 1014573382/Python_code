from learningcourse.ElementPosition.capability import driver
from time import sleep

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y

l = get_size()
print(l)

# 向左滑动
def swipeLeft():
    l = get_size()
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    # 从(x1,y1)滑到(x2,y1),间隔1秒
    driver.swipe(x1,y1,x2,y1, 1000)

# 向右滑动
def swipeRight():
    l = get_size()
    x1 = int(l[0] * 0.15)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)

# 从上往下滑
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.9)
    y2 = int(l[1] * 0.2)
    driver.swipe(x1, y1, x1, y2, 1000)

# 从下往上滑
def swipeDown():
    l=get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.35)
    y2 = int(l[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)

for i in range(2):
    swipeLeft()
    sleep(0.5)

driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()