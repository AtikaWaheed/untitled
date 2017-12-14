from selenium.webdriver.support.select import Select


class BasePage(object):

    def __init__(self, driver):
        # instantiate driver
        self.driver = driver


class MainWelcomePage(BasePage):

    def title_matches(self):
        # Find out Header
        return "Welcome: Mercury Tours" in self.driver.title

    def login_cred_submit(self, username, password):
        # Give login cred and click submit
        user_name = self.driver.find_element_by_name('userName')
        user_name.send_keys(username)
        password_keys = self.driver.find_element_by_name('password')
        password_keys.send_keys(password)
        submit = self.driver.find_element_by_name('submit')
        submit.click()

    def flights_ver_click(self):
        # Move to flights vertical
        self.driver.find_element_by_link_text('Flights').click()

    def pass_count(self, passcount):
        passenger = self.driver.find_element_by_name('passCount')
        Select(passenger).select_by_visible_text(passcount)

    def from_port(self, fromport):
        departing_port = self.driver.find_element_by_name('fromPort')
        Select(departing_port).select_by_visible_text(fromport)

    def from_month(self, frommonth):
        depart_month = self.driver.find_element_by_name('fromMonth')
        Select(depart_month).select_by_visible_text(frommonth)

    def from_day(self, fromday):
        depart_day = self.driver.find_element_by_name('fromDay')
        Select(depart_day).select_by_visible_text(fromday)

    def to_port(self, toport):
        arriving_in = self.driver.find_element_by_name('toPort')
        Select(arriving_in).select_by_visible_text(toport)

    def to_month(self, tomonth):
        return_month = self.driver.find_element_by_name('toMonth')
        Select(return_month).select_by_visible_text(tomonth)

    def to_day(self, today):
        return_date = self.driver.find_element_by_name('toDay')
        Select(return_date).select_by_visible_text(today)

    def sevice_cred(self):
        self.driver.find_element_by_css_selector('input[value="Business"]').click()

    def airline_name_select(self, airline):
        airline_name = self.driver.find_element_by_css_selector('select[name="airline"]')
        Select(airline_name).select_by_visible_text(airline)

    def flight_det_sub(self):
        self.driver.find_element_by_css_selector('input[name="findFlights"]').click()

    def hotels_ver_click(self):
        # Click hotels vertical
        self.driver.find_element_by_link_text('Hotels').click()

    def back_click(self):
        self.driver.find_element_by_css_selector('img[src="images/home.gif"]').click()


