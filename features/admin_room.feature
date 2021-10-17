Feature: Admin room

    Scenario: Creating an admin room page

    Given I am logged in as an admin user
    And I am on the admin Rooms page 
    When I enter room details
    And Click the Create button
    Then The new room should be added to the admin Rooms page