from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Returns and Orders button')
def click_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@when('Verify Sign-In page opens and Sign-In header is visible')
def verify_signin(context):
    expected_result = "Sign-In"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}.'

@then('Email field is present')
def verify_email_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed()
