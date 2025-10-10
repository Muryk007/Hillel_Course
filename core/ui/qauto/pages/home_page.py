from encodings.punycode import selective_find

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.ui.qauto.pages.base_page import BasePage
from core.ui.qauto.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
        self.locators = HomePageLocators

# home page
    def _sign_up_btn(self):
        return self._sign_up_button(self.locators.sign_up_btn)

    def click_sign_up_button(self):
        self._sign_up_btn().click()
        return self

    def sign_in_btn(self):
        return self._sign_in_button(self.locators.sign_in_btn)

    def click_sign_in_button(self):
        self.sign_in_btn().click()
        return self

# can be used on all pages
    def open_new_page(self):
        self.wait_for_new_page()
        return self

    def not_open_new_page(self):
        self.wait_for_url_not_change()
        return self

# sign_up modal
    def sign_up_first_name(self):
        return self._sign_up_first_name(self.locators.user_first_name_field)

    def set_sign_up_first_name(self, first_name):
        self.sign_up_first_name().send_keys(first_name)
        return self

    def sign_up_last_name(self):
        return self._sign_up_last_name(self.locators.user_last_name_field)

    def set_sign_up_last_name(self, last_name):
        self.sign_up_last_name().send_keys(last_name)
        return self

    def sign_up_email_field(self):
        return self._sign_up_email_field(self.locators.user_email_field)

    def set_sign_up_email(self, email):
        self.sign_up_email_field().send_keys(email)
        return self

    def sign_up_password_field(self):
        return self._sign_up_password_field(self.locators.user_password_field)

    def set_sign_up_password(self, password):
        self.sign_up_password_field().send_keys(password)
        return self

    def repeat_sign_up_password(self):
        return self._sign_up_password_confirm_field(self.locators.repeat_password_field)

    def set_repeat_sign_up_password(self, password):
        self.repeat_sign_up_password().send_keys(password)
        return self

    def register_button(self):
        return self._register_button(self.locators.register_btn)

    def click_register_button(self):
        self.register_button().click()
        return self

    def register_button_is_clickable(self):
        try:
            button = self.driver.find_element(*self.locators.register_btn)
            return button.is_enabled() and button.is_displayed()
        except Exception:
            return False

    def sing_up_first_name_required(self):
        return self._sign_up_first_name_required(self.locators.first_name_required)

    def sign_up_last_name_required(self):
        return self._sign_up_last_name_required(self.locators.last_name_required)

    def sign_up_email_required(self):
        return self._sign_up_email_required(self.locators.email_required)

    def sign_up_password_required(self):
        return self._sign_up_password_required(self.locators.password_required)

    def sign_up_password_confirm_required(self):
        return self._sign_up_confirm_password_required(self.locators.re_enter_password_required)

    def invalid_sign_up_first_name_alert_1(self):
        return self._invalid_first_name(self.locators.invalid_first_name_alert_1)

    def invalid_sign_up_first_name_alert_2(self):
        return self._invalid_first_name(self.locators.invalid_first_name_alert_2)

    def invalid_sign_up_last_name_alert_1(self):
        return self._invalid_last_name(self.locators.invalid_last_name_alert_1)

    def invalid_sign_up_last_name_alert_2(self):
        return self._invalid_last_name(self.locators.invalid_last_name_alert_2)

    def invalid_sign_up_email(self):
        return self._invalid_email(self.locators.invalid_email_alert)

    def invalid_sign_up_password(self):
        return self._invalid_password(self.locators.invalid_password_alert)

    def invalid_sign_up_password_re_enter(self):
        return self._invalid_password_re_enter(self.locators.invalid_re_enter_password_alert)

    def user_exists_alert(self):
        return self._user_exists(self.locators.user_exist_alert)

# app-signin-modal
    def sign_in_email(self):
        return self._sign_in_email_field(self.locators.sign_in_email_field)

    def set_sign_in_email(self, email):
        self.sign_in_email().send_keys(email)
        return self

    def sign_in_password_field(self):
        return self._sign_in_password_field(self.locators.sign_in_password_field)

    def set_sign_in_password(self, password):
        self.sign_in_password_field().send_keys(password)
        return self

    def remember_me_checkbox(self):
        return self._remember_me_checkbox(self.locators.remember_checkbox)

    def click_remember_me_checkbox(self):
        self.remember_me_checkbox().click()
        return self

    def login_button(self):
        return self._login_btn(self.locators.login_btn)

    def click_login_button(self):
        self.login_button().click()
        return self

    def wrong_email_alert(self):
        return self._wrong_email_password(self.locators.wrong_email_password)

    def require_email(self):
        return self._email_required(self.locators.email_required)

    def require_password(self):
        return self._password_required(self.locators.password_required)

