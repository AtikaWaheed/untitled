import unittest
import Mercury_tour_page_file
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time


class MercuryMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.guru99.com/selenium/newtours/")

    def test_mercury_tour(self):
        # test mercury tour
        mercury_tour_page = Mercury_tour_page_file.MainWelcomePage(self.driver)
        assert mercury_tour_page.title_matches()
        mercury_tour_page.title_matches()
        mercury_tour_page.login_cred()
        mercury_tour_page.submit_cred()
        mercury_tour_page.flights_vertical()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_flightfinder.gif"]')
        mercury_tour_page.flight_details()
        mercury_tour_page.flight_details_submit()
        assert "After flight finder - No Seats Avaialble" in self.driver.page_source
        mercury_tour_page.flights_vertical()
        mercury_tour_page.hotels_vertical()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_construction.gif"]')
        mercury_tour_page.back_home()

        time.sleep(10)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()