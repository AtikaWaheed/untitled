import unittest
from selenium import webdriver
from pages import mercury_tour_page


class MercuryMainPage(unittest.TestCase):

    def setUp(self):
        """
        Setup driver and initialize class
        """
        self.driver = webdriver.Firefox()
        self.mt_page = mercury_tour_page.MainWelcomePage(self.driver)
        self.mt_page.visit()
        assert "Welcome: Mercury Tours" in self.driver.title

    def test01_login(self):
        """
        Redirected on correct page
        Verify that user can log in entering valid username and valid password
        """
        self.mt_page.login_cred_submit("admin", "admin")

    def test02_open_flight_vertical_by_clicking(self):
        """
        Flights vertical got clicked and page is correct
        Correct values has been given
        Submitted Form
        Moved back to front page
        """
        footer = self.mt_page.open_flight_vertical_by_clicking().split()
        self.assertEqual(footer[1], "2005,")
        passcount = self.mt_page.select_passenger("4")
        self.assertEqual(passcount, "4")
        fromport = self.mt_page.select_departing_location("Frankfurt")
        self.assertEqual(fromport, "Frankfurt")
        fromMonth = self.mt_page.select_departing_month("September")
        self.assertEqual(fromMonth, "September")
        fromday = self.mt_page.select_departing_day("5")
        self.assertEqual(fromday, "5")
        toport = self.mt_page.select_arriving_port("London")
        self.assertEqual(toport, "London")
        tomonth = self.mt_page.select_returning_month("April")
        self.assertEqual(tomonth, "April")
        today = self.mt_page.select_returning_day("5")
        self.assertEqual(today, "5")
        service = self.mt_page.select_service_class()

        self.assertEqual(service, "Business class ")
        airline = self.mt_page.select_an_airline("Blue Skies Airlines")
        self.assertEqual(airline, "Blue Skies Airlines")
        self.mt_page.submit_flight_details_and_back_to_frontpage()
        assert "Welcome: Mercury Tours" in self.driver.title

    def tearDown(self):
        """
        Verify page has closed
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
