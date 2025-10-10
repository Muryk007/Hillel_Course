from selenium.webdriver.common.by import By

class HomePageLocators:
# home page
    sign_up_btn = (By.XPATH, '//button[contains(@class, "btn-primary")]')
    sign_in_btn = (
        By.XPATH, '//div[contains(@class, "align-items-center")]/button[contains(@class, "header_signin")]'
    )

# app-signup-modal
    user_first_name_field = (By.ID, 'signupName')
    user_last_name_field = (By.ID, 'signupLastName')
    user_email_field = (By.ID, 'signupEmail')
    user_password_field = (By.ID, 'signupPassword')
    repeat_password_field = (By.ID, 'signupRepeatPassword')
    register_btn = (By.XPATH, '//div[@class="modal-footer"]/button[contains(@class, "btn-primary")]')

    first_name_required = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Name required")]')
    last_name_required = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Last name")]')
    email_required = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Email required")]')
    password_required = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Password required")]')
    re_enter_password_required = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Re-enter password required")]'
    )

    invalid_first_name_alert_1 = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Name is invalid")]')
    invalid_first_name_alert_2 = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Name has to be from 2 to 20 characters long")]'
    )
    invalid_last_name_alert_1 = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Last name is invalid")]'
    )
    invalid_last_name_alert_2 = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Last name has to be from 2 to 20 characters long")]'
    )
    invalid_email_alert = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Email is incorrect")]'
    )
    invalid_password_alert = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Password has to be from 8 to 15 characters long and")]'
    )
    invalid_re_enter_password_alert = (
        By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Password has to be from 8 to 15 characters long and")]'
    )

    user_exist_alert = (By.XPATH, '//p[contains(@class, "alert-danger") and contains(text(), "User already exists")]')

# app-signin-modal
    sign_in_email_field = (By.ID, 'signinEmail')
    sign_in_password_field = (By.ID, 'signinPassword')
    remember_checkbox = (By.ID, 'remember')

    login_btn = (
        By.XPATH, '//div[contains(@class, "justify-content-between")]/button[contains(@class, "btn-primary")]'
    )

    registration_from_sign_in = (
        By.XPATH, '//div[contains(@class, "justify-content-between")]/button[contains(@class, "btn-link")]'
    )

    wrong_email_password = (
        By.XPATH, '//p[contains(text(), "Wrong email or password")]'
    )

    email_required = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Email required")]')
    password_required = (By.XPATH, '//div[@class="invalid-feedback"]/p[contains(text(), "Password required")]')