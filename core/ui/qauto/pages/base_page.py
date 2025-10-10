from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None

# home page
    def open_page(self, url=None):
        url = self.url or url
        self.driver.get(url)

    def _sign_up_button(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _sign_in_button(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

# can be used on all pages
    def wait_for_new_page(self, old_url=None, timeout=5):
        old_url = old_url or self.driver.current_url
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
            return self.driver.current_url
        except TimeoutException:
            raise AssertionError(f"URL did not change from {old_url} within {timeout} seconds.")

    def wait_for_url_not_change(self, old_url=None, timeout=5):
        old_url = old_url or self.driver.current_url
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.current_url != old_url
            )
            raise AssertionError(f"URL unexpectedly changed from {old_url} to {self.driver.current_url}")
        except TimeoutException:
            print(f"URL did not change within {timeout} seconds (expected behavior)")

# app-signin-up modal
    def _sign_up_first_name(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _sign_up_last_name(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _sign_up_email_field (self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _sign_up_password_field (self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _sign_up_password_confirm_field (self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _register_button(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _register_button_is_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )

    def _sign_up_first_name_required(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _sign_up_last_name_required(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _sign_up_email_required(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _sign_up_password_required(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _sign_up_confirm_password_required(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _invalid_first_name(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _invalid_last_name(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _invalid_email(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _invalid_password(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _invalid_password_re_enter(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _user_exists(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

# app-signin-modal
    def _sign_in_email_field(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _sign_in_password_field(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _remember_me_checkbox(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _login_btn(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )

    def _wrong_email_password(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _email_required (self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def _password_required(self, locator):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

