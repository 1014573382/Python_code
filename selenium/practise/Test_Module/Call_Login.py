from LoginClass import *

driver = webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)

login = Login()
login.user_login(driver)
sleep(5)
login.user_logout(driver)

sleep(3)
driver.quit()