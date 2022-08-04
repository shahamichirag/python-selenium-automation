# Created by shaha at 8/4/2022
Feature: Amazon Privacy Policy tests


  Scenario: User can open and close Amazon privacy Notice
    Given Open Amazon T&C Page
    When Store original window
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify that Amazon Privacy Notice Page is opened
    And User can close new window
    And User can switch back to the Original window