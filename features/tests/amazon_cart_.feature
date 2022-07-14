# Created by shaha at 7/13/2022
Feature: Amazon cart tests
  # Enter feature description here

  Scenario: amazon cart shows empty status
    Given open Amazon page
    When Click cart icon
    Then Verify the cart is empty