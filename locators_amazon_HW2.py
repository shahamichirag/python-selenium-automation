
'''from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()


# LOCATOR FOR AMAZON LOGO USING XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# LOCATOR FOR CONTINUE BUTTON USING XPATH
driver.find_element(By.ID, 'continue')

# LOCATOR FOR NEED HELP LINK USING XPATH
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# OR USING CONTAINS
driver.find_element(By.XPATH, "//span[contains(@class,'expander')]")

# LOCATORS FOR FORGOT YOUR PASSWORD USING ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')
# OR USING CONTAINS
driver.find_element(By.XPATH, "//a[contains(@href, 'forgotpassword?')]")

#LOCATORS FOR OTHER ISSUES USING ID
driver.find_element(By.ID, 'ap-other-signin-issues-link')
#LOCATORS FOR OTHER ISSUES USING MULTIPLE NODES
driver.find_element(By.XPATH, "//div[@aria-expanded='true']//a[contains(@href,'account-issues')]")

#LOCATORS FOR CREATE YOUR AMAZON ACCOUNT USING ID
driver.find_element(By.ID, 'createAccountSubmit')

#LOCATORS FOR CONDITIONS OF USE
driver.find_element.(By.XPATH, "//a[contains(text(),'Conditions of Use') and @class='a-link-normal']")

#LOCATORS FOR PRIVACY POLICY
driver.find_element.(By.XPATH, "//a[contains(text(),'Privacy Notice') and @class='a-link-normal']")

'''

