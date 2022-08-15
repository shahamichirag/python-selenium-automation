from pages.base_page import Page


class Mainpage(Page):

    def open_main(self):
        self.driver.get('https://www.amazon.com/')
        