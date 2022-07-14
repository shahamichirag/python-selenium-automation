from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-cart-count').click()

Expected_result = "Your Amazon Cart is empty"
Actual_result = driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text

assert Expected_result == Actual_result, f'Expected {Expected_result} but got {Actual_result}.'

print('Amazon cart status is empty!')

driver.quit()