from playwright.sync_api import Playwright

pay_load = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
token = ""

class APIUtils:

    def get_token(self, playwright:Playwright, user_credentials):
        user_name = user_credentials["username"]
        user_password = user_credentials["password"]

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/auth/login",
                data={"userEmail": user_name,"userPassword": user_password})
        assert response.ok
        return response.json()["token"]

    def create_order(self, playwright:Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=pay_load,
                                 headers={"Authorization": token,
                                            "Content-Type":"application/json"})
        print(response.json())
        response_body = response.json()
        order = response_body["orders"][0]
        return order