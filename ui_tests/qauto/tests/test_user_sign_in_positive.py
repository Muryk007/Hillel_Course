import time
import pytest
import logging.config

from pathlib import Path
from selenium.webdriver import Chrome
from core.ui.qauto.pages.home_page import HomePage
from ui_tests.qauto.test_data.test_data import login_data

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
    "email, password", login_data
)
def test_sign_in(driver, email, password):
    sign_in = HomePage(driver)
    sign_in.open_page()

    logger.info(f"--- POSITIVE Sign_In test ---")

    sign_in.click_sign_in_button()
    sign_in.set_sign_in_email(email)
    sign_in.set_sign_in_password(password)
    sign_in.click_remember_me_checkbox()

    sign_in.click_login_button().open_new_page()
    logger.info(f"--- User signed in and new page is opened ---")
    logger.info(f"--- POSITIVE Sign_In test passed---")

