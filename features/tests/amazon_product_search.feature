# Created by shaha at 8/12/2022
Feature: Amazon search result tests

  Scenario: User can search for a product
    Given Open Google page
    When Input watches into search field
    And Click on search icon
    Then Product results for watches are shown


  Scenario: User can search for a product
    Given Open Amazon page
    When Search for coffee on Amazon
    Then User sees results for coffee


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select any department by alias electronics
    And Search for keyboard on Amazon
    Then verify electronics department is selected

