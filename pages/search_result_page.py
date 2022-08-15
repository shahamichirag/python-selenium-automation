from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Searchresult(Page):
    PRICE_ITEM = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def first_product_click(self):
        self.wait.until(
            EC.presence_of_element_located(self.PRICE_ITEM), message='Price is not mentioned'
        ).click()

