from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_LINKS = (By.XPATH,"//div[contains(@class,'_p13n-zg-nav-tab-all_style_zg-tabs-li')]")

@given('Open Amazon Bestseller page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

#@when('Click on Bestsellers')
#def click_bestsellers(context):
 #   context.driver.find_element(By.XPATH, "//div[contains(@class, 'nav-tab-all_style_zg-tabs-li-selected-div')]//a[contains(@href, 'Best-Sellers')]").click()


@then('Verify {expected_amount} links are present on Amazon Bestsellers page')
def verify_bestseller_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*BESTSELLER_LINKS)
    assert len(links) == expected_amount; \
            f'Expected {expected_amount} links but got {len(links)}'