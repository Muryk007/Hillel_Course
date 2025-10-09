import pytest
import logging.config

from pathlib import Path
from selenium.webdriver import Chrome
from core.ui.qauto.pages.home_page import HomePage
from ui_tests.qauto.test_data.test_data import fake_email_login
from ui_tests.qauto.test_data.test_data import fake_password_login

log_file = Path(__file__).resolve().parents[3] / "lesson_28" / "sign_up_sign_in.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.config.fileConfig(log_file.parent / "logging.conf")
logger = logging.getLogger()

@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("email, password", fake_email_login)
def test_sign_in_wrong_email(driver, email, password):
    sign_in = HomePage(driver)
    sign_in.open_page()

    logger.info(f"--- NEGATIVE Sign_In test (wrong email) ---")

    sign_in.click_sign_in_button()
    sign_in.set_sign_in_email(email)
    sign_in.set_sign_in_password(password)

    sign_in.click_login_button()
    assert sign_in.wrong_email_alert()
    logger.info(f"Wrong email alert is displayed")

    logger.info(f"--- NEGATIVE Sign_In test (wrong email) passed ---")

@pytest.mark.parametrize("email, password", fake_password_login)
def test_sign_in_wrong_password(driver, email, password):
    sign_in = HomePage(driver)
    sign_in.open_page()

    logger.info(f"--- NEGATIVE Sign_In test (wrong password) ---")

    sign_in.click_sign_in_button()
    sign_in.set_sign_in_email(email)
    sign_in.set_sign_in_password(password)

    sign_in.click_login_button()

    assert sign_in.wrong_email_alert()
    logger.info(f"Wrong password alert is displayed")

    logger.info(f"--- NEGATIVE Sign_In test (wrong password) passed ---")

def test_sign_in_required_fields(driver):
    sign_in = HomePage(driver)
    sign_in.open_page()

    logger.info(f"--- NEGATIVE Sign_In test (required fields) ---")

    sign_in.click_sign_in_button()
    sign_in.sign_in_email().click()
    sign_in.sign_in_password_field().click()

    sign_in.click_login_button()

    assert sign_in.require_email().is_displayed()
    logger.info(f"Required email alert is displayed")
    assert sign_in.require_password().is_displayed()
    logger.info(f"Required password alert is displayed")

    sign_in.not_open_new_page()

    logger.info(f"New page does not open")
    logger.info(f"--- NEGATIVE Sign_In test (required fields) passed ---")


