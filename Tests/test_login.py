from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_page(page: Page):
    login _page = LoginPage(page)
    login_page.goto("https://automationintesting.online/")


