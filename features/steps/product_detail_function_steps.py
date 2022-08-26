from selenium.webdriver.common.by import By
from behave import given, when, then



COLOR_OPTIONS = (By.CSS_SELECTOR,'#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@then('Verify user can select all available colors')
def verify_can_select_colors(context):
    expected_colors = ['Ballet', 'Bisque Multi', 'Black', 'Black Sig', 'Brown', 'Coral Reef Multi', 'Dark Powder Blush', ' Luggage', 'Navy', 'Pearl Grey', ' Powder Blush',' Vanilla']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)
    actual_colors = []
    for color in colors[:5]:
        color.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        print('Actual colors: ', actual_colors)

    assert expected_colors[:5] == actual_colors, f'Expected {expected_colors} but got {actual_colors}'