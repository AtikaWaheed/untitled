import unittest
from selenium import webdriver
from pages import page_arbisoft
import time

class ArbisoftFD(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://arbisoft.com/")
        time.sleep(5)

    def test_arbisoft(self):
        arb_tool = page_arbisoft.MainPage(self.driver)
        assert arb_tool.title_matches()
        arb_tool.title_matches()
        arb_tool.test_nav_links()
        assert len(self.nav_links) == 7

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
        unittest.main()
