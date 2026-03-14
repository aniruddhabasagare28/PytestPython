from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import new_context

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browse = playwright.chromium.launch(headless=False)
    context = browse.new_context()
    page = context.new_page()

    # Orders page -> order is present
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("aniruddhabasagare28@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Admin123!@#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button",name="ORDERS").click()

    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you")
    context.close()