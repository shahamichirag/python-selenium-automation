from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-results']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image['data-image-latency's-product-image']")


@then('Verify that every product has a name and an image on search result page')
def verify_product_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error! Title should not be blank!'
        product.find_element(*PRODUCT_IMG)


