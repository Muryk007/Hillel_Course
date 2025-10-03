from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from core.ui.nova_post.pages.base_page import BasePage
from core.ui.nova_post.locators.search_page_locators import SearchPageLocators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.locators = SearchPageLocators

    def _input_field(self):
        return self._track_input_field(self.locators.track_input_field)

    def _search_track_button(self):
        return self._search_button(self.locators.search_button)

    def set_track_number(self, number):
        self._input_field().send_keys(number)
        return self

    def button_click(self):
        self._search_track_button().click()
        return self

    def search(self, number):
        self.set_track_number(number).button_click()
        return self

    def get_search_result_text(self, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.locators.search_result_field)
            )
            return element.text.strip()
        except TimeoutException:
            return None