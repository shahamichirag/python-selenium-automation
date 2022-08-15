from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURN_AND_ORDER = (By.ID, 'nav-orders')

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_button(self):
        self.find_element(*self.RETURN_AND_ORDER).click()
