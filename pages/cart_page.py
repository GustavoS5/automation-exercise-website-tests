"""Cart page object."""

from __future__ import annotations

from playwright.sync_api import Locator

from pages.base_page import BasePage


class CartPage(BasePage):
    """Locators and actions for the shopping cart."""

    url = "/view_cart"

    @property
    def shopping_cart_breadcrumb(self) -> Locator:
        return self.page.get_by_text("Shopping Cart", exact=True)

    @property
    def cart_table(self) -> Locator:
        return self.page.locator("#cart_info_table")

    @property
    def cart_rows(self) -> Locator:
        return self.cart_table.locator("tbody tr")

    @property
    def proceed_to_checkout_link(self) -> Locator:
        return self.page.locator("a.check_out")

    def load(self) -> None:
        """Open the cart page."""
        self.navigate()

    def cart_item_by_name(self, product_name: str) -> Locator:
        """Return a cart row containing the requested product name."""
        return self.cart_rows.filter(has_text=product_name).first
