from page_objects.OrderHistory import OrderHistory


class dashboard:
    def __init__(self, page):
        self.page = page

    def navigate_to_order(self):
        orders_button = self.page.get_by_role("button", name="ORDERS")
        orders_button.wait_for()
        orders_button.click()
        orderHistory = OrderHistory(self.page)
        return orderHistory