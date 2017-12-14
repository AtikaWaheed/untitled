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
        mt_page.login_cred_submit("admin", "admin")
        mt_page.flights_ver_click()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_flightfinder.gif"]')
        mt_page.pass_count("4")
        mt_page.from_port("Frankfurt")
        mt_page.from_month("September")
        mt_page.from_day("5")
        mt_page.to_port("London")
        mt_page.to_month("March")
        mt_page.to_day("5")
        mt_page.sevice_cred()
        mt_page.airline_name_select("Blue Skies Airlines")
        mt_page.flight_det_sub()
        assert "After flight finder - No Seats Avaialble" in self.driver.page_source
        mt_page.hotels_ver_click()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_construction.gif"]')
        mt_page.back_click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()