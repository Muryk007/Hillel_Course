from selenium.webdriver.common.by import By

class SearchPageLocators:
    track_input_field = (By.ID, "en")
    search_button = (By.ID, "np-number-input-desktop-btn-search-en")
    search_result_field = (By.CLASS_NAME, "header__status-text")

