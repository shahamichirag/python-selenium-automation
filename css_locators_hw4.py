from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# Amazon sign using CSS tag and Class(es)
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create Account - using CSS(tag and class)
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your Name input field locators using ID
driver.find_element(By.ID, 'ap_customer_name')

# Email field - using ID
driver.find_element(By.ID, 'ap_email')

# Password field - using ID
driver.find_element(By.ID, 'ap_password')

# Re-Enter password field - using ID
driver.find_element(By.ID, 'ap_password_check')

#Continue button locators - using ID
driver.find_element(By.ID, 'continue')

# Condition of Use using CSS - using partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use?']")

#Privacy policy locators
#using CSS with partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice?']")

# Already have an account Sign in locators
# CSS using class and attribute
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='signin?']")
