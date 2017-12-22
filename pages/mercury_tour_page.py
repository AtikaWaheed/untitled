from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        """
        instantiate driver
        """
        self.driver = driver


class MainWelcomePage(BasePage):

    def title_matches(self):
        """
        Make sure that title matches
        """
        return "Welcome: Mercury Tours" in self.driver.title

    def login_cred_submit(self, username, password):
        """
        Submit username and password in fields and submit
        """
        user_name = self.driver.find_element_by_name('userName')
        user_name.send_keys(username)
        password_keys = self.driver.find_element_by_name('password')
        password_keys.send_keys(password)
        submit = self.driver.find_element_by_name('submit')
        submit.click()

    def get_logged_in(self):
        """
        Make sure it gets loggedOut
        """
        return self.driver.find_element_by_css_selector('img[src="images/banner2.gif"]')

    def flights_ver_click(self):
        """
        Moving to flights vertical
        """
        self.driver.find_element_by_link_text('Flights').click()

    def pass_count(self, passcount):
        """
        Enter any passcount in passenger field
        """
        passenger = self.driver.find_element_by_name('passCount')
        Select(passenger).select_by_visible_text(passcount)
        return passcount

    def from_port(self, fromport):
        """
        Enter from_port from field
        """
        departing_port = self.driver.find_element_by_name('fromPort')
        Select(departing_port).select_by_visible_text(fromport)
        return fromport

    def from_month(self, frommonth):
        """
        Select from_month from dropdown
        """
        depart_month = self.driver.find_element_by_name('fromMonth')
        Select(depart_month).select_by_visible_text(frommonth)
        return frommonth

    def from_day(self, fromday):
        """
        Select from_day from dropdown
        """
        depart_day = self.driver.find_element_by_name('fromDay')
        Select(depart_day).select_by_visible_text(fromday)
        return fromday

    def to_port(self, toport):
        """
        Select to_port
        """
        arriving_in = self.driver.find_element_by_name('toPort')
        Select(arriving_in).select_by_visible_text(toport)
        return toport

    def to_month(self, tomonth):
        """
        Select to_month from list
        """
        return_month = self.driver.find_element_by_name('toMonth')
        Select(return_month).select_by_visible_text(tomonth)
        return tomonth

    def to_day(self, today):
        """
        Select to_day from list
        """
        return_date = self.driver.find_element_by_name('toDay')
        Select(return_date).select_by_visible_text(today)
        return today

    def sevice_cred(self):
        """
        Select any Business class from dropdown
        """
        self.driver.find_element_by_css_selector('input[value="Business"]').click()

    def airline_name_select(self, airline):
        """
        Choose an airline
        """
        airline_name = self.driver.find_element_by_css_selector('select[name="airline"]')
        Select(airline_name).select_by_visible_text(airline)
        return airline

    def flight_det_sub(self):
        """
        After entering all credentials submit form and wait to open next page
        """
        self.driver.find_element_by_css_selector('input[name="findFlights"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="images/home.gif"]'))
        )

    def back_click(self):
        """
        Moving back to front page
        """
        self.driver.find_element_by_css_selector('img[src="images/home.gif"]').click()
