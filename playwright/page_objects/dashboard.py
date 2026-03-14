from page_objects.OrderHistory import OrderHistory


class dashboard:
    def __init__(self, page):
        self.page = page

    def navigate_to_order(self):
        self.page.locator("button[routerlink='/dashboard/myorders']").click()
        orderHistory = OrderHistory(self.page)
        return orderHistory