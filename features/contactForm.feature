Feature: Contact Form

    Scenario: Contact Form
        Given I am on the home page
        When I populate the contact form at the bottom of the page
        And Click the submit button
        Then The text "Thanks for getting in touch <name>!" should be displayed
        Given I have submitted the contact form
        # When I log in as an admin user
        And I navigate to the admin messages page
        Then I should see the details of the message I submitted