import pytest
import logging.config

from pathlib import Path
from selenium.webdriver import Chrome
from core.ui.qauto.pages.home_page import HomePage
from ui_tests.qauto.test_data.test_data import invalid_sign_up_data
from ui_tests.qauto.test_data.test_data import exist_user_data

log_file = Path(__file__).resolve().parents[3] / "lesson_28" / "sign_up_sign_in.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.config.fileConfig(log_file.parent / "logging.conf")
logger = logging.getLogger()

@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


def test_required_fields(driver):
    sign_up = HomePage(driver)
    sign_up.open_page()

    logger.info(f"--- NEGATIVE Sign_Up test (required fields) ---")

    sign_up.click_sign_up_button()
    sign_up.sign_up_first_name().click()
    sign_up.sign_up_last_name().click()
    sign_up.sign_up_email_field().click()
    sign_up.sign_up_password_field().click()
    sign_up.repeat_sign_up_password().click()
    sign_up.click_register_button()

    assert sign_up.sing_up_first_name_required().is_displayed()
    logger.info(f"First name required alert is displayed")
    assert sign_up.sign_up_last_name_required().is_displayed()
    logger.info(f"Last name required alert is displayed")
    assert sign_up.sign_up_email_required().is_displayed()
    logger.info(f"Email required alert is displayed")
    assert sign_up.sign_up_password_required().is_displayed()
    logger.info(f"Password required alert is displayed")
    assert sign_up.sign_up_password_confirm_required().is_displayed()
    logger.info(f"Confirm Password required alert is displayed")

    logger.info(f"--- NEGATIVE Sign_Up test (required fields) passed ---")

@pytest.mark.parametrize("first_name, last_name, email, password", exist_user_data)
def test_user_exists(driver, first_name, last_name, email, password):
    sign_up = HomePage(driver)
    sign_up.open_page()

    logger.info(f"--- NEGATIVE Sign_Up test (user exists) ---")

    sign_up.click_sign_up_button()
    sign_up.set_sign_up_first_name(first_name)
    sign_up.set_sign_up_last_name(last_name)
    sign_up.set_sign_up_email(email)
    sign_up.set_sign_up_password(password)
    sign_up.set_repeat_sign_up_password(password)
    sign_up.click_register_button()

    assert sign_up.user_exists_alert().is_displayed()
    logger.info(f"User exists alert is displayed")

    logger.info(f"--- NEGATIVE Sign_Up test (user exists) passed ---")

@pytest.mark.parametrize("first_name, last_name, email, password", invalid_sign_up_data)
def test_incorrect_inputs(driver, first_name, last_name, email, password):
    sign_up = HomePage(driver)
    sign_up.open_page()

    logger.info(f"--- NEGATIVE Sign_Up test (incorrect inputs) ---")

    sign_up.click_sign_up_button()
    sign_up.set_sign_up_first_name(first_name)
    sign_up.set_sign_up_last_name(last_name)
    sign_up.set_sign_up_email(email)
    sign_up.set_sign_up_password(password)
    sign_up.set_repeat_sign_up_password(password)
    sign_up.click_register_button()

    assert sign_up.invalid_sign_up_first_name_alert_1().is_displayed()
    assert sign_up.invalid_sign_up_first_name_alert_2().is_displayed()
    logger.info(f"Invalid First name alert is displayed")
    assert sign_up.invalid_sign_up_last_name_alert_1().is_displayed()
    assert sign_up.invalid_sign_up_last_name_alert_2().is_displayed()
    logger.info(f"Invalid Last name alert is displayed")
    assert sign_up.invalid_sign_up_email().is_displayed()
    logger.info(f"Invalid Email alert is displayed")
    assert sign_up.invalid_sign_up_password().is_displayed()
    logger.info(f"Invalid Password alert is displayed")
    assert sign_up.invalid_sign_up_password_re_enter().is_displayed()
    logger.info(f"Invalid Password alert is displayed")

    assert not sign_up.register_button_is_clickable()
    logger.info(f"Register button is not clickable")

    logger.info(f"--- NEGATIVE Sign_Up test (incorrect inputs) passed ---")