from pages.inbox_page import InboxPage
from playwright.sync_api import expect
import re

class HomePage:
    
    def __init__(self, page):
        self.page = page
        self.cookie_button = page.get_by_role("button", name="Súhlasím")
        self.login_container = page.get_by_role("complementary")
        self.username_input = self.login_container.locator('input[name="userName"]')
        self.password_input = self.login_container.locator('input[name="password"]')
        self.login_button = page.get_by_role("button", name="Prihlásiť")
        self.inbox_link = self.login_container.get_by_text(re.compile(r"neprečítan(?:é|ú|ých) správ"))
        self.logout_button = self.login_container.get_by_role("button", name="Odhlásiť")

    def goto(self):
        self.page.goto("https://www.centrum.sk/")

    def click_cookie_widget(self):
        self.cookie_button.click()

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def navigate_to_inbox(self):
        self.inbox_link.click()
        return InboxPage(self.page)

    def logout(self):
        self.logout_button.click(timeout=5000)

    def is_user_logged_out(self):
        expect(self.login_button).to_be_visible(timeout=5000)
        expect(self.page).to_have_url("https://www.centrum.sk/")
    
    def is_user_logged_in(self):
        expect(self.inbox_link).to_be_visible(timeout=5000)