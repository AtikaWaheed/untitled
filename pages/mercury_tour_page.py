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
        self.url = "http://demo.guru99.com/selenium/newtours/"

    def visit(self):
        self.driver.get(self.url)


class MainWelcomePage(BasePage):

    def login_cred_submit(self, username, password):
        """
        Submit username and password in fields and submit
        Returned next page
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'userName'))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys(password)
        self.driver.find_element_by_name('submit').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="images/banner2.gif"]'))
        )

    def open_flight_vertical_by_clicking(self):
        """
        Move to flights vertical
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Flights'))
        ).click()
        footer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.footer'))
        ).text
        return footer

    def select_passenger(self, passcount):
        """
        Enter any passcount in passenger field
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'passCount'))
        )).select_by_visible_text(passcount)
        return passcount

    def select_departing_location(self, fromport):
        """
        Enter from_port from field
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'fromPort'))
        )).select_by_visible_text(fromport)
        return fromport

    def select_departing_month(self, frommonth):
        """
        Select from_month from dropdown
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'fromMonth'))
        )).select_by_visible_text(frommonth)
        return frommonth

    def select_departing_day(self, fromday):
        """
        Select from_day from dropdown
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'fromDay'))
        )).select_by_visible_text(fromday)
        return fromday

    def select_arriving_port(self, toport):
        """
        Select to_port
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'toPort'))
        )).select_by_visible_text(toport)
        return toport

    def select_returning_month(self, tomonth):
        """
        Select to_month from list
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'toMonth'))
        )).select_by_visible_text(tomonth)
        return tomonth

    def select_returning_day(self, today):
        """
        Select to_day from list
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'toDay'))
        )).select_by_visible_text(today)
        return today

    def select_service_class(self):
        """
        Select Business class from dropdown
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="Business"]'))
        ).click()
        service = self.driver.find_element_by_css_selector('input[value="Business"]')
        from nose.tools import set_trace;set_trace()
        print service
        #return service


    def select_an_airline(self, airline):
        """
        Choose an airline
        """
        Select(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="airline"]'))
        )).select_by_visible_text(airline)
        return airline

    def submit_flight_details_and_back_to_frontpage(self):
        """
        After entering all credentials submit form and wait to open next page
        """
        self.driver.find_element_by_css_selector('input[name="findFlights"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="images/home.gif"]'))
        ).click()
