import pathlib

import pytest
import logging.config

from pathlib import Path
from selenium.webdriver import Chrome
from core.ui.nova_post.pages.search_page import SearchPage

log_conf_path = Path().absolute() / "lesson_27" / "logging.conf"
logging.config.fileConfig(log_conf_path)
logger = logging.getLogger()

@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

def test_tracking(driver):
    search_page = SearchPage(driver)
    search_page.open_page()

    search_page.search("20400479134830")

    result_text = search_page.get_search_result_text()

    if result_text != "Отримана":
        logger.error(f"Текст <<{result_text}>> не співпав з <<Отримана>>.")
        logger.warning(f"Посилка не отримана.")
    else:
        logger.info(f"Текст <<{result_text}>> співпав з <<Отримана>>.")
        logger.info(f"Посилка отримана.")
        pass

    # assert result_text == "Отримана", f"Очікував 'Отримана', але отримав: {result_text}"