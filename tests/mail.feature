Feature: Login/Logout + Sending Mails

    #----------------------- Blok 3 ------------------------------
    Scenario: Verify logout after sending an email with attachment
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        And the user navigates to the inbox
        And the user navigates to write email widget
        And the user writes recipient email into the recipient field
        And the user writes email subject
        And the user writes email body
        And the user attaches a file to the email
        And the user sends the email
        And the user logs out - inbox
        Then the logout should be successful
    
    Scenario: Verify sending an email with attachment
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        And the user navigates to the inbox
        And the user navigates to write email widget
        And the user writes recipient email into the recipient field
        And the user writes email subject
        And the user writes email body
        And the user attaches a file to the email
        And the user sends the email
        Then the mail should be succesfully sent

    Scenario: Verify adding attachment to email
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        And the user navigates to the inbox
        And the user navigates to write email widget
        And the user attaches a file to the email
        Then the attachment should be succesfully loaded

    #----------------------- Blok 2 ------------------------------
    Scenario: Verify logout after sending an email without attachment
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        And the user navigates to the inbox
        And the user navigates to write email widget
        And the user writes recipient email into the recipient field
        And the user writes email subject
        And the user writes email body
        And the user sends the email
        And the user logs out - inbox
        Then the logout should be successful

    Scenario: Verify sending an email without attachment
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        And the user navigates to the inbox
        And the user navigates to write email widget
        And the user writes recipient email into the recipient field
        And the user writes email subject
        And the user writes email body
        And the user sends the email
        Then the mail should be succesfully sent

    #----------------------- Blok 1 ------------------------------
    Scenario: Verify login with valid credentials
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        Then the login should be successful

    Scenario: Verify logout after logging in
        Given the user visits login homepage
        And the user clicks the cookie widget
        When the user logins with valid credentials
        And the user logs out - homepage
        Then the logout should be successful