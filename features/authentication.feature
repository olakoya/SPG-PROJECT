Feature: Admin Page

    Scenario: Login to the admin page

        Given I am on the admin login page
        When I log in as an admin Username: "admin" Password: "password"
        Then I should be taken to the Rooms page

    Scenario: Logout from the admin page

        Given I am logged in as an admin user
        When I click the logout button
        Then I should be taken to the admin login page