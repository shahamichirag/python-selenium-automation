from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")
PRIVACY_PAGE = (By.XPATH, "//h1[contains(text(),'Amazon.com Privacy Notice')]")


@given('Open Amazon T&C Page')
def open_amazon_tandc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('original window:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(PRIVACY_LINK)
    ).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then('Verify that Amazon Privacy Notice Page is opened')
def privacy_page_opened(context):
    context.driver.wait.until(
        EC.presence_of_element_located(PRIVACY_PAGE), message='Privacy Page does not open!'
    )


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('User can switch back to the Original window')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)



