from selenium import webdriver

def browser():
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Ie()

    # driver.get("http://localhost")
    return driver

if __name__ == '__main__':
    browser()
