import time
import unittest

from selenium import webdriver
from pages import mercury_tour_page


class MercuryMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.guru99.com/selenium/newtours/")

    def test_mercury_tour(self):
        # test mercury tour
        mt_page = mercury_tour_page.MainWelcomePage(self.driver)
        assert mt_page.title_matches()
        mt_page.title_matches()
        mt_page.login_cred()
        mt_page.flights_vertical()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_flightfinder.gif"]')
        mt_page.pass_count()
        mt_page.from_port()
        mt_page.from_month()
        mt_page.from_day()
        mt_page.to_port()
        mt_page.to_month()
        mt_page.to_day()
        mt_page.sevice_Cred()
        mt_page.airline_name_select()
        mt_page.flight_details_submit()
        assert "After flight finder - No Seats Avaialble" in self.driver.page_source
        mt_page.hotels_vertical()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_construction.gif"]')
        mt_page.back_home()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()