from playwright.sync_api import Page

fake_payload_order_response = {"data":[],"message":"No Orders"}
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?/69b39f0df86ba51a65ff2b")

def test_network(page:Page):

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    page.get_by_placeholder("email@example.com").fill("aniruddhabasagare28@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Admin123!@#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)