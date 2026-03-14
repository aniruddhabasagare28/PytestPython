from page_objects.dashboard import dashboard


class LoginPage:

    def __init__(self,page):
        self.page = page

    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login_page(self, usr_name, usr_password):
        self.page.get_by_placeholder("email@example.com").fill(usr_name)
        self.page.get_by_placeholder("enter your passsword").fill(usr_password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = dashboard(self.page)
        return dashboard_page