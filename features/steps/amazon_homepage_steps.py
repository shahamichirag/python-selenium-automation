from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@given('Open Amazon product {product_id} page')
def open_product_id_page(context, product_id):
    sleep(5)
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Returns and Orders button')
def click_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count').click()


@then('Verify the cart is empty')
def verify_cart(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'
    print('Amazon cart status is empty!')