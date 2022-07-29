from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
#from time import sleep

INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
PRICE_ITEM = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_CART_BTN= (By.ID, 'add-to-cart-button')

CART_ITEMS = (By.XPATH, "//div[@id='nav-cart-count-container']/span[@id='nav-cart-count']")

@when('Search for {search_word} on Amazon')
def search_product(context, search_word):
    searchbar = context.driver.find_element(*INPUT_FIELD)
    searchbar.send_keys(search_word)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on the first product')
def first_product_click(context):
    context.driver.wait.until(
        EC.presence_of_element_located(PRICE_ITEM), message= 'Price is not mentioned'
    ).click()


@when('Click on the add to cart button')
def add_cart_button(context):
    context.driver.wait.until (
        EC.presence_of_element_located(ADD_CART_BTN), message='Add to Cart button is not clickable'
    ).click()


@then('Verify the cart has {expected_counts} item(s)')
def verify_cart_count(context, expected_counts):
    context.driver.wait.until(
        EC.presence_of_element_located(CART_ITEMS),message='cart count is not located'
    )
    expected_counts = int(expected_counts)
    actual_counts = context.driver.find_element(*CART_ITEMS).text
    actual_counts = int(actual_counts)
    assert expected_counts == actual_counts; f'Expected {expected_counts} but got {actual_counts}'



