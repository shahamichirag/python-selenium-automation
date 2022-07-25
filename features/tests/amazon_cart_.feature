# Created by shaha at 7/13/2022
Feature: Amazon cart tests
  # Enter feature description here

  Scenario: amazon cart shows empty status
    Given open Amazon page
    When Click cart icon
    Then Verify the cart is empty

  Scenario: amazon cart shows number of items added
    Given open Amazon page
    When Search for notebook on Amazon
    When Click on the first product
    When Click on the add to cart button
    Then Verify the cart has 1 item(s)