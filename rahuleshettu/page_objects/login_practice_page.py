from playwright.sync_api import Page, expect


class LoginPracticePage:
    LOGIN_PAGE_URL = "https://rahulshettyacademy.com/loginpagePractise/"

    def __init__(self, driver: Page, timeout: int = 10000):
        self.driver = driver
        self.timeout = timeout
        self.username = driver.locator("#username")
        self.password = driver.locator("#password")
        self.terms_checkbox = driver.locator("#terms")
        self.sign_in_button = driver.locator("#signInBtn")
        self.shop_page_marker = driver.locator("a.nav-link.btn.btn-primary")

    def navigate_to_login_page(self) -> None:
        self.driver.goto(self.LOGIN_PAGE_URL)
        expect(self.username).to_be_visible(timeout=self.timeout)

    def login_with_terms(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.terms_checkbox.check()
        self.sign_in_button.click()
        self.driver.wait_for_url("**/shop", timeout=self.timeout)
        expect(self.shop_page_marker).to_be_visible(timeout=self.timeout)

