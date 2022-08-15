from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@given('Open Amazon product {product_id} page')
def open_product_id_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Returns and Orders button')
def click_button(context):
    context.app.header.click_button()


@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count').click()


@then('Verify the cart is empty')
def verify_cart(context):
    context.app.cart_page.verify_cart()