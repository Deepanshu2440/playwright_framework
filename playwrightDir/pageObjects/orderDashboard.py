from playwright.sync_api import expect


class OrderDashboard:

    def __init__(self, page):
        self.page = page

    def dashboard(self, orderId):
        self.page.get_by_role('button', name='  ORDERS').click()
        expect(self.page.get_by_text(orderId)).to_be_visible()
        return self.page


