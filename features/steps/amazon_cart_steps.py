from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@when('Search for {search_word} on Amazon')
def search_product(context, search_word):
    context.app.header.search_product(search_word)


@when('Click on the first product')
def first_product_click(context):
    context.app.search_result_page.first_product_click()


@when('Click on the add to cart button')
def add_cart_button(context):
    context.app.cart_page.add_cart_button()


@then('Verify the cart has {expected_counts} item(s)')
def verify_cart_count(context, expected_counts):
    context.app.cart_page.verify_cart_count(1)


