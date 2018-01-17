import unittest
from selenium import webdriver
from pages import mercury_tour_page


class TestMercuryMainPage(unittest.TestCase):

    def setUp(self):
        """
        Setup driver and initialize class
        """
        self.driver = webdriver.Firefox()
        self.mt_page = mercury_tour_page.MainWelcomePage(self.driver)
        self.mt_page.visit()

    def test01_login(self):
        """
        Redirected on correct page
        Verify that user can log in entering valid username and valid password
        """
        self.mt_page.login_submit_verify("admin", "admin")
        assert self.mt_page.title in self.driver.title

    def test02_open_flight_vertical_by_clicking(self):
        """
        Flights vertical got clicked and page is correct
        Correct values has been given
        Submitted Form
        Moved back to front page
        """
        self.mt_page.open_flight_vertical_by_clicking()
        assert self.mt_page.find_flight in self.driver.title
        self.mt_page.select_passenger("4")
        self.mt_page.select_departing_location("Frankfurt")
        self.mt_page.select_departing_month("September")
        self.mt_page.select_departing_day("5")
        self.mt_page.select_arriving_port("London")
        self.mt_page.select_returning_month("April")
        self.mt_page.select_returning_day("4")
        self.mt_page.select_business_class()
        self.mt_page.select_an_airline("Blue Skies Airlines")
        self.mt_page.submit_flight_details()
        assert self.mt_page.find_flight in self.driver.title
        self.mt_page.back_to_main_page()
        assert self.mt_page.title in self.driver.title

    def tearDown(self):
        """
        Verify page has closed
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
