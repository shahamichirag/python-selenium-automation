from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By CSS, ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# By CSS, class(es)
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us')
# by class, without a tag
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag')

# By CSS, attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email'][maxlength='128']")
# mix of ids, classes, attributes:
driver.find_element(By.CSS_SELECTOR, "input#ap_email[type='email']")
driver.find_element(By.CSS_SELECTOR, "input#ap_email.auth-autofocus.a-input-text[type='email']")

# by multiple nodes
driver.find_element(By.CSS_SELECTOR, "ul.hmenu-visible li a[href*='new-releases']")

##AMAZON SEARCH USING BDD EXAMPLE BY LANA
driver.find_element(By.XPATH, "//div[@class='nav-search-facade' and .//span[@id='nav-search-label-id']]")

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word} on amazon')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('User sees results for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'