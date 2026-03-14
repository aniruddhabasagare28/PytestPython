import time
from playwright.sync_api import Page, expect, Playwright


def test_playwright_basics(playwright):
    # This will help to create a engine for driver for edge and chrome
    # By default this is the headless mode , so make it false to see execution
    browser = playwright.chromium.launch(headless = False)

    # Opening your browser incoginito mode also in different context or separate than other one
    context = browser.new_context()

    #open a fresh page , using this you will automate your test cases
    page = context.new_page()
    page.goto("https://www.google.com")

#page is only work with chromium with headless mode  on single context
def test_playwright_basics_shortcut(page:Page):
    page.goto("https://www.google.com")

def test_login_practice(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    time.sleep(5)

def test_login_practice_wrong_credentials(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefox_browser(playwright:Playwright):
    firefox_browser = playwright.firefox.launch(headless=False)
    context = firefox_browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_child_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").first.click()
    child_page = new_page_info.value
    expect(child_page.locator("//a[text()='mentor@rahulshettyacademy.com']")).to_be_visible()
    time.sleep(5)