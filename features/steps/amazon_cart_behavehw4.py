from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count').click()

@then('Verify the cart is empty')
def verify_cart(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text

    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'

    print('Amazon cart status is empty!')