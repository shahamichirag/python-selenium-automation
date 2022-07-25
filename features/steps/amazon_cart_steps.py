from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
PRICE_ITEM = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_CART_BTN= (By.ID, 'add-to-cart-button')

CART_ITEMS = (By.XPATH, "//div[@id='nav-cart-count-container']/span[@id='nav-cart-count']")

@when('Search for {search_word} on Amazon')
def search_product(context, search_word):
    context.driver.find_element(*INPUT_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_ICON).click()
    #sleep(5)

@when('Click on the first product')
def first_product_click(context):
    context.driver.find_element(*PRICE_ITEM).click()

@when('Click on the add to cart button')
def add_cart_button(context):
    #sleep(5)
    context.driver.find_element(*ADD_CART_BTN).click()


@then('Verify the cart has {expected_counts} item(s)')
def verify_cart_count(context, expected_counts):
    #sleep(5)
    expected_counts = int(expected_counts)
    actual_counts = context.driver.find_element(*CART_ITEMS).text
    actual_counts = int(actual_counts)
    assert expected_counts == actual_counts; f'Expected {expected_counts} but got {actual_counts}'



