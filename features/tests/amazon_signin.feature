# Created by shaha at 7/13/2022
Feature: Amazon Returns and Orders button tests
  # Enter feature description here

  Scenario: Sign-In page opens on clicking Return and Orders button
    Given Open Amazon page
    When Click on Returns and Orders button
    When Verify Sign-In page opens and Sign-In header is visible
    Then Email field is present




