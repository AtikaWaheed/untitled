import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.python.org")
       # wait = WebDriverWait(self.driver, 30)
        #ele = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'python-logo' )))

    def test_search_in_python(self):

        main_page = Page.MainPage(self.driver)
        assert main_page.matches_the_title()
        main_page.matches_the_title()
        main_page.search_element_by_id()
        main_page.click_Go_button()
        WebDriverWait(self.driver, 30)
        assert main_page.is_result_found(), "No results found."
        main_page.about_Page()


    def tearDown(self):
        self.driver.close()

if _name_ == "__main__":
    unittest.main()