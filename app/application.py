from pages.main_page import Mainpage
from pages.header import Header
from pages.sign_in_page import Signin
from pages.cart_page import Cartpage
from pages.search_result_page import Searchresult


class Application:
    def __init__(self,driver):
        self.driver = driver

        self.main_page = Mainpage(self.driver)
        self.header = Header(self.driver)
        self.sign_in_page = Signin(self.driver)
        self.cart_page = Cartpage(self.driver)
        self.search_result_page = Searchresult(self.driver)