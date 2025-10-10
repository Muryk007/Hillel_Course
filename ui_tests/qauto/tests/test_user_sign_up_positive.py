import pytest
import logging.config

from pathlib import Path
from selenium.webdriver import Chrome
from core.ui.qauto.pages.home_page import HomePage
from ui_tests.qauto.test_data.test_data import sign_up_data

log_file = Path(__file__).resolve().parents[3] / "lesson_28" / "sign_up_sign_in.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.config.fileConfig(log_file.parent / "logging.conf")
logger = logging.getLogger()

@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "first_name, last_name, email, password", sign_up_data
)
def test_register_user(driver, first_name, last_name, email, password):
    sign_up = HomePage(driver)
    sign_up.open_page()

    logger.info(f"--- POSITIVE Sign_Up test ---")

    sign_up.click_sign_up_button()
    logger.info(f"Click sign up button on home page")

    sign_up.set_sign_up_first_name(first_name)
    logger.info(f"First name set to {first_name}")

    sign_up.set_sign_up_last_name(last_name)
    logger.info(f"Last name set to {last_name}")

    sign_up.set_sign_up_email(email)
    logger.info(f"Email set to {email}")


    sign_up.set_sign_up_password(password)
    logger.info(f"Password set to {password}")

    sign_up.set_repeat_sign_up_password(password)
    logger.info(f"Repeat password set to {password}")

    sign_up.click_register_button()
    logger.info(f"Click register button on home page")

    logger.info(f"--- POSITIVE test passed ---")


