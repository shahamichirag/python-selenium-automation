from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Cartpage(Page):
    CART_STATUS = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]")
    ADD_CART_BTN = (By.ID, 'add-to-cart-button')
    CART_ITEMS = (By.XPATH, "//div[@id='nav-cart-count-container']/span[@id='nav-cart-count']")

    def verify_cart(self):
        expected_result = "Your Amazon Cart is empty"
        actual_result = self.find_element(*self.CART_STATUS).text
        assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'
        print('Amazon cart status is empty!')

    def add_cart_button(self):
        self.wait.until(
            EC.presence_of_element_located(self.ADD_CART_BTN), message='Add to Cart button is not clickable'
        ).click()

    def verify_cart_count(self, expected_counts):
        self.wait.until(
            EC.presence_of_element_located(self.CART_ITEMS), message='cart count is not located'
        )
        expected_counts = int(expected_counts)
        actual_counts = self.find_element(*self.CART_ITEMS).text
        actual_counts = int(actual_counts)
        assert expected_counts == actual_counts;
        f'Expected {expected_counts} but got {actual_counts}'
