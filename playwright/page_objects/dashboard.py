class dashboard:
    def __init__(self, page):
        self.page = page

    def navigate_to_order(self):
        self.page.get_by_role("button", name="ORDERS").click()


