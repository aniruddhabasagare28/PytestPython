from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import page

from utils.apiBase import APIUtils

fake_payload_order_response = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(
        json= fake_payload_order_response
    )

def test_network(page:Page):

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    page.get_by_placeholder("email@example.com").fill("aniruddhabasagare28@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Admin123!@#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    order_text = page.locator(".mt-4").text_content()
    print(order_text)


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    get_token = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()

