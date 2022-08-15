from selenium.webdriver.common.by import By
from pages.base_page import Page


class Signin(Page):
    RESULT = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin(self):
        expected_result = 'Sign-In'
        actual_text = self.find_element(*self.RESULT).text
        assert expected_result == actual_text, f'Expected {expected_result}, but got {actual_text}'

    def verify_email_field(self):
        assert self.find_element(*self.EMAIL_FIELD).is_displayed()
