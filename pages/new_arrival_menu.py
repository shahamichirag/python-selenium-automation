from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class Newarrival(Page):
    NEW_ARRIVAL = (By.CSS_SELECTOR, "a.nav-a.nav-hasArrow[aria-label='New Arrivals']")
    WOMEN_DEALS = (By.CSS_SELECTOR, "a[href*='fashion-women'].mm-merch-panel")

    def hover_new_arrival(self):
        new_arrival = self.find_element(*self.NEW_ARRIVAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival)
        actions.perform()

    def verify_user_see_deals(self):
        self.wait_for_element_appear(*self.WOMEN_DEALS)
