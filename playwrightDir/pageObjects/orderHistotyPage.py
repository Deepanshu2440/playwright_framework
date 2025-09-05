from playwright.sync_api import expect


class OrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def history(self, order):
        self.page.locator(".tr").filter(has_text=order)
        self.page.get_by_role('button', name='VIEW').nth(0).click()


