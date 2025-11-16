Feature: Upload Question File
  As a user
  I want to upload a file containing questions
  So that the system can validate and prepare it for classification

  Scenario: Successful upload of a valid file
    Given I logged in for upload file
    And I navigates to the question upload page
    When I selects a valid file in a supported format
    And I uploads the file
    Then the file preview should be displayed
    And the classify button should be enabled
    And the system should confirm the file is ready to classify

  Scenario: Upload fails due to invalid file format
    Given I logged in for upload file
    And I navigates to the question upload page
    When I selects a file with an unsupported format
    And I uploads the file
    Then the system should display an invalid format error message
    And the classify button should remain disabled
