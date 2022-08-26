from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()
    sleep(12)


@given('Open Amazon product {product_id} page')
def open_product_id_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Returns and Orders button')
def click_button(context):
    context.app.header.click_button()


@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count').click()


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select any department by alias {alias}')
def select_any_dept(context,alias):
    context.app.header.select_any_dept(alias)


@then('Verify the cart is empty')
def verify_cart(context):
    context.app.cart_page.verify_cart()


@then('Verify {category} department is selected')
def verify_dept_selected(context, category):
    context.app.search_result_page.verify_dept_selected(category)


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()
