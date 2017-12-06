from selenium.webdriver.common.keys import Keys
class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):

    def matches_the_title(self):
        return "Python" in  self.driver.title

    def search_element_by_id(self):
        element = self.driver.find_element_by_id('id-search-field')
        element.send_keys("python")


    def click_Go_button(self):
        new_element = self.driver.find_element_by_id('submit')
        new_element.click()

    def is_result_found(self):
        return "No results found." not in self.driver.page_source

    def about_Page(self):
        self.driver.find_element_by_link_text('About').click()