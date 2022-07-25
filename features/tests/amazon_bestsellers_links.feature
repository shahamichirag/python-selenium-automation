# Created by shaha at 7/21/2022
Feature: Amazon Bestsellers page links tests
  # Enter feature description here

  Scenario: Amazon Bestsellers page contains all links
    Given Open Amazon Bestseller page
    #When Click on Bestsellers
    Then Verify 5 links are present on Amazon Bestsellers page
    # Enter steps here