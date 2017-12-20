import unittest
from selenium import webdriver
from pages import mercury_tour_page


class MercuryMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.guru99.com/selenium/newtours/")
        self.mt_page = mercury_tour_page.MainWelcomePage(self.driver)

    def test_tiltle_matches(self):
        assert self.mt_page.title_matches()
        self.mt_page.title_matches()

    def test_login(self):
        self.mt_page.login_cred_submit("admin", "admin")

    def test_flights_ver_click(self):
        self.mt_page.flights_ver_click()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_flightfinder.gif"]')

    def test_pass_count(self):
        self.mt_page.pass_count("4")

    def test_from_port(self):
        self.mt_page.from_port("Frankfurt")

    def test_from_month(self):
        self.mt_page.from_month("September")

    def test_from_day(self):
        self.mt_page.from_day("5")

    def test_to_port(self):
        self.mt_page.to_port("London")

    def test_to_month(self):
        self.mt_page.to_month("March")

    def test_to_day(self):
        self.mt_page.to_day("5")

    def test_sevice_cred(self):
        self.mt_page.sevice_cred()

    def test_airline_name_select(self):
        self.mt_page.airline_name_select("Blue Skies Airlines")

    def test_flight_det_sub(self):
        self.mt_page.flight_det_sub()

    def test_hotels_ver_click(self):
        self.mt_page.hotels_ver_click()

    def test_back_click(self):
        assert self.driver.find_element_by_css_selector('img[src="images/mast_construction.gif"]')
        self.mt_page.back_click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
