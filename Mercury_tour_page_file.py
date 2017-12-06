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
        # Give login cred
        user_name = self.driver.find_element_by_name('userName')
        user_name.send_keys("admin")
        password_keys = self.driver.find_element_by_name('password')
        password_keys.send_keys("admin")

    def submit_cred(self):
        # just submit after giving cred
        submit = self.driver.find_element_by_name('submit')
        submit.click()

    def flights_vertical(self):
        # Move to flights vertical
        self.driver.find_element_by_link_text('Flights').click()

    def flight_details(self):
        # submit form
        self.driver.find_element_by_css_selector('input[value="oneway"]').click()
        time.sleep(5)
        passenger = self.driver.find_element_by_name('passCount')
        departing_port = self.driver.find_element_by_name('fromPort')
        depart_month = self.driver.find_element_by_name('fromMonth')
        depart_day = self.driver.find_element_by_name('fromDay')
        arriving_in = self.driver.find_element_by_name('toPort')
        return_month = self.driver.find_element_by_name('toMonth')
        return_date = self.driver.find_element_by_name('toDay')
        #passenger_list = self.driver.find_element_by_css_selector('option[value="3"]')
        #actions = ActionChains(self.driver)
       # actions.move_to_element(passenger).perform()
        #actions.click(passenger_list)
        Select(passenger).select_by_visible_text("4")
        Select(departing_port).select_by_visible_text("Frankfurt")
        Select(depart_month).select_by_visible_text("September")
        Select(arriving_in).select_by_visible_text("London")
        Select(return_month).select_by_visible_text("March")
        Select(return_date).select_by_visible_text("5")
        service_class = self.driver.find_element_by_css_selector('input[value="Business"]').click()
        airline_name = self.driver.find_element_by_css_selector('select[name="airline"]')
        Select(airline_name).select_by_visible_text("Blue Skies Airlines")
        time.sleep(5)

    def flight_details_submit(self):
        self.driver.find_element_by_css_selector('input[name="findFlights"]').click()
        time.sleep(10)

    def hotels_vertical(self):
        # Click hotels vertical
        self.driver.find_element_by_link_text('Hotels').click()

    def back_home(self):
        self.driver.find_element_by_css_selector('img[src="images/home.gif"]').click()

