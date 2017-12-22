import unittest
from selenium import webdriver
from pages import mercury_tour_page


class MercuryMainPage(unittest.TestCase):

    def setUp(self):
        """
        Setup driver and initialize class
        """
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.guru99.com/selenium/newtours/")
        self.mt_page = mercury_tour_page.MainWelcomePage(self.driver)

    def test_title_matches(self):
        """
        Verify correct page is open
        """
        assert self.mt_page.title_matches()

    def test_login(self):
        """
        Verify that user can log in entering valid username and valid password
        """
        self.mt_page.login_cred_submit("admin", "admin")
        assert self.mt_page.get_logged_in()

    def test_flights_ver_click(self):
        """
        Verify the exact flight page on display
        """
        self.mt_page.flights_ver_click()
        assert self.driver.find_element_by_css_selector('img[src="images/mast_flightfinder.gif"]')

    def test_pass_count(self):
        """
        Verify correct pass_count number has picked
        """
        count = self.mt_page.pass_count("4")
        self.assertEqual(count, "4")

    def test_from_port(self):
        """
        Verify correct from_port has picked
        """
        port = self.mt_page.from_port("Frankfurt")
        self.assertEqual(port, "Frankfurt")

    def test_from_month(self):
        """
        Verify correct from_month has picked
        """
        f_month = self.mt_page.from_month("September")
        self.assertEqual(f_month, "September")

    def test_from_day(self):
        """
        Verify correct from_day has picked
        """
        f_day = self.mt_page.from_day("5")
        self.assertEqual(f_day, "5")

    def test_to_port(self):
        """
        Verify correct to_port has picked
        """
        t_port = self.mt_page.to_port("London")
        self.assertEqual(t_port, "London")

    def test_to_month(self):
        """
        Verify correct to_month has picked
        """
        t_month = self.mt_page.to_month("March")
        self.assertEqual(t_month, "March")

    def test_to_day(self):
        """
        Verify correct to_day has picked
        """
        t_day = self.mt_page.to_day("5")
        self.assertEqual(t_day, "5")

    def test_sevice_cred(self):
        """
        Verify service_cred has picked correct and selected also
        """
        s_cred = self.mt_page.sevice_cred()
        assert self.driver.find_element_by_css_selector('input[value="Business"]').text() == "Business class "

    def test_airline_name_select(self):
        """
        Verify correct airline has picked and selected
        """
        air_name = self.mt_page.airline_name_select("Blue Skies Airlines")
        self.assertEqual(air_name, "Blue Skies Airlines")

    def test_flight_det_sub(self):
        """
        Verify flight details has submitted
        """
        det_sub = self.mt_page.flight_det_sub()
        self.assertTrue(det_sub)

    def test_back_click(self):
        """
        Verify we have moved to front page
        """
        self.mt_page.back_click()
        assert self.mt_page.title_matches()

    def tearDown(self):
        """
        Verify page has closed
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
