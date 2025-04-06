import os
import pytest
from playwright.sync_api import sync_playwright
from pages.homepage import HomePage
from pages.inbox_page import InboxPage

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def homepage(page):
    return HomePage(page)

@pytest.fixture
def inbox(page):
    return InboxPage(page)

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("EMAIL_USERNAME", "username"),
        "password": os.getenv("EMAIL_PASSWORD", "password"),
        "recipient": os.getenv("EMAIL_RECIPIENT", "xxx@gmail.com")
    }

@pytest.fixture
def email_data():
    return {
        "subject": os.getenv("EMAIL_SUBJECT", "Test subject"),
        "body": os.getenv("EMAIL_BODY", "Test body"),
        "attachment": os.getenv("EMAIL_ATTACHMENT", "tests/test.txt")
    }