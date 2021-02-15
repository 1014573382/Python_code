from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
#强制等待
#sleep(10)

#隐性等待，等到网页加载完成，就执行下一步，否则就等到设置时间截止执行下一步
#driver.implicitly_wait(10)

print(driver.title)

try:
      #显式等待，每隔0.6秒检查一次，6秒后返超时
      ele = WebDriverWait(driver, 6, 0.6).until(EC.presence_of_element_located((By.ID, "kw")))
      ele.send_keys("小D课堂")
      print("资源加载成功")
      print(driver.title)
except:
      print("资源加载失败，发送报警邮件或短信")

finally:
      print("不管成功与否，都打印，用于资源管理")

      #退出浏览器
      driver.quit()
