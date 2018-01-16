from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainWelcomePage(object):
    title = "Welcome: Mercury Tours"
    find_flight = "Find a Flight: Mercury Tours"
    time_to_wait = 10

    def __init__(self, driver):
        """
        instantiate driver
        """
        self.driver = driver
        self.url = "http://demo.guru99.com/selenium/newtours/"

    def visit(self):
        self.driver.get(self.url)

    def login_submit_verify(self, username, password):
        """
        Submit username and password in fields and submit
        Returned next page
        """
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.NAME, 'userName'))
        ).send_keys(username)
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys(password)
        self.driver.find_element_by_name('submit').click()
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Salon Travel'))
        )

    def open_flight_vertical_by_clicking(self):
        """
        Move to flights vertical
        """
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Flights'))
        ).click()

    def select_passenger(self, pass_counts):
        """
        Enter any passcount in passenger field
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'passCount'))
        )).select_by_visible_text(pass_counts)

    def select_departing_location(self, from_port):
        """
        Enter from_port from field
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'fromPort'))
        )).select_by_visible_text(from_port)

    def select_departing_month(self, from_month):
        """
        Select from_month from dropdown
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'fromMonth'))
        )).select_by_visible_text(from_month)

    def select_departing_day(self, from_day):
        """
        Select from_day from dropdown
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'fromDay'))
        )).select_by_visible_text(from_day)

    def select_arriving_port(self, to_port):
        """
        Select to_port
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'toPort'))
        )).select_by_visible_text(to_port)

    def select_returning_month(self, to_month):
        """
        Select to_month from list
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'toMonth'))
        )).select_by_visible_text(to_month)

    def select_returning_day(self, to_day):
        """
        Select to_day from list
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.NAME, 'toDay'))
        )).select_by_visible_text(to_day)

    def select_business_class(self):
        """
        Select Business class from dropdown
        """
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="Business"]'))
        ).click()

    def select_an_airline(self, airline_name):
        """
        Choose an airline
        """
        Select(WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="airline"]'))
        )).select_by_visible_text(airline_name)

    def submit_flight_details(self):
        """
        After entering all credentials submit form and wait to open next page
        """
        self.driver.find_element_by_css_selector('input[name="findFlights"]').click()
        contact = WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'CONTACT'))
        )
        return contact

    def back_to_main_page(self):
        """
        Moving back to front door
        """
        WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="images/home.gif"]'))
        ).click()
