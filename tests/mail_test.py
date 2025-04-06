from pytest_bdd import scenarios, given, when, then

scenarios('mail.feature')

#----------------------- Given ------------------------------
@given("the user visits login homepage")
def open_login_homepage(homepage):
    homepage.goto()

@given("the user clicks the cookie widget")
def click_cookie_widget(homepage):
    homepage.click_cookie_widget()

#----------------------- When ------------------------------
@when("the user logins with valid credentials")
def enter_valid_credentials(homepage, credentials):
    homepage.login(credentials["username"], credentials["password"])

@when("the user navigates to the inbox")
def enter_inbox(homepage):
    homepage.navigate_to_inbox()

@when("the user navigates to write email widget")
def navigate_to_write_email_widget(inbox):
    inbox.click_write_email()

@when("the user writes recipient email into the recipient field")
def enter_recipient(inbox, credentials):
    inbox.enter_recipient(credentials["recipient"])

@when("the user writes email subject")
def fill_subject(inbox, email_data):
    inbox.fill_subject(email_data["subject"])

@when("the user writes email body")
def fill_email_body(inbox, email_data):
    inbox.fill_body(email_data["body"])

@when("the user attaches a file to the email")
def attach_file(inbox, email_data):
    inbox.attach_file(email_data["attachment"])

@when("the user sends the email")
def send_email(inbox):
    inbox.send_email()
    
@when("the user logs out - homepage")
def log_out(homepage):
    homepage.logout()

@when("the user logs out - inbox")
def log_out(inbox):
    inbox.logout()

#----------------------- Then ------------------------------
@then("the login should be successful")
def check_login(homepage):
    homepage.is_user_logged_in()

@then("the logout should be successful")
def check_logout(homepage):
    homepage.is_user_logged_out()

@then("the mail should be succesfully sent")
def check_sending_mail(inbox):
    inbox.check_email_send()

@then("the attachment should be succesfully loaded")
def check_sending_mail(inbox):
    inbox.is_file_attached()
    
    