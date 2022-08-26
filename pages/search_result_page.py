from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Searchresult(Page):
    PRICE_ITEM = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    NAV_SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{SUBSTR}']")

    def first_product_click(self):
        self.wait.until(
            EC.presence_of_element_located(self.PRICE_ITEM), message='Price is not mentioned'
        ).click()

    def get_subnav_locator(self, category):
        return[self.NAV_SUBNAV[0], self.NAV_SUBNAV[1].replace('{SUBSTR}', category)]

    def verify_dept_selected(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)





