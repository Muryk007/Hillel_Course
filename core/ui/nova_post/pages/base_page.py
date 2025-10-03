from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def open_page(self, url=None):
        url = self.url or url
        self.driver.get(url)

    def _track_input_field(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))

    def _search_button(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))

    def _search_result_field(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))
