from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")

    def get_header(self):
        return self.header_title.inner_text()

    def get_item_count(self):
        return self.inventory_items.count()
