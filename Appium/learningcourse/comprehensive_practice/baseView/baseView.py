
class BaseView(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *location):
        return self.driver.find_element(*location)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def swipe(self,start_x, start_y, end_x, end_y,duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y,duration)

