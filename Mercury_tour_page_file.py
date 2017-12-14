import time
from selenium.webdriver.support.select import Select


class BasePage(object):

    def __init__(self, driver):
        # instantiate driver
        self.driver = driver


class MainWelcomePage(BasePage):

    def title_matches(self):
        # Find out Header
        return "Welcome: Mercury Tours" in self.driver.title

    def login_cred(self):
        # Give login cred and click submit
        user_name = self.driver.find_element_by_name('userName')
        user_name.send_keys("admin")
        password_keys = self.driver.find_element_by_name('password')
        password_keys.send_keys("admin")
        submit = self.driver.find_element_by_name('submit')
        submit.click()

    def flights_vertical(self):
        # Move to flights vertical
        self.driver.find_element_by_link_text('Flights').click()

    def pass_count(self):
        passenger = self.driver.find_element_by_name('passCount')
        Select(passenger).select_by_visible_text("4")

    def from_port(self):
        departing_port = self.driver.find_element_by_name('fromPort')
        Select(departing_port).select_by_visible_text("Frankfurt")

    def from_month(self):
        depart_month = self.driver.find_element_by_name('fromMonth')
        Select(depart_month).select_by_visible_text("September")

    def from_day(self):
        depart_day = self.driver.find_element_by_name('fromDay')
        Select(depart_day).select_by_visible_text("5")

    def to_port(self):
        arriving_in = self.driver.find_element_by_name('toPort')
        Select(arriving_in).select_by_visible_text("London")

    def to_month(self):
        return_month = self.driver.find_element_by_name('toMonth')
        Select(return_month).select_by_visible_text("March")

    def to_day(self):
        return_date = self.driver.find_element_by_name('toDay')
        Select(return_date).select_by_visible_text("5")

    def sevice_Cred(self):
        service_class = self.driver.find_element_by_css_selector('input[value="Business"]').click()

    def airline_name_select(self):
        airline_name = self.driver.find_element_by_css_selector('select[name="airline"]')
        Select(airline_name).select_by_visible_text("Blue Skies Airlines")

    def flight_details_submit(self):
        self.driver.find_element_by_css_selector('input[name="findFlights"]').click()
        time.sleep(10)

    def hotels_vertical(self):
        # Click hotels vertical
        self.driver.find_element_by_link_text('Hotels').click()

    def back_home(self):
        self.driver.find_element_by_css_selector('img[src="images/home.gif"]').click()

