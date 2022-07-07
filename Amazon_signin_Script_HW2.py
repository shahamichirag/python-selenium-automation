
from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

Expected_result = "Sign-In"
Actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert Expected_result == Actual_result, f'Expected {Expected_result} but got {Actual_result}.'

print('Sign-In page has opened!')

#l = driver.find_element(By.ID("ap_email")).is_displayed()

driver.quit()
