"""Cart page object."""

from __future__ import annotations

from playwright.sync_api import Locator, Page, TimeoutError

from pages.base_page import BasePage


class CartPage(BasePage):
    """Locators and actions for the shopping cart."""

    url = "/view_cart"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.shopping_cart_breadcrumb = page.get_by_text("Shopping Cart", exact=True)
        self.cart_table = page.locator("#cart_info_table")
        self.cart_rows = self.cart_table.locator("tbody tr")
        self.proceed_to_checkout_link = page.locator("a.check_out")
        self.checkout_modal = page.locator("#checkoutModal")
        self.register_login_link = page.locator("#checkoutModal a[href='/login']")
        self.empty_cart_message = page.locator("#empty_cart")

    def load(self) -> None:
        """Open the cart page."""
        self.navigate()

    def cart_item_by_name(self, product_name: str) -> Locator:
        """Return a cart row containing the requested product name."""
        return self.cart_rows.filter(has_text=product_name).first

    def item_price(self, product_name: str) -> Locator:
        """Return the price cell for a cart item."""
        return self.cart_item_by_name(product_name).locator(".cart_price")

    def item_quantity(self, product_name: str) -> Locator:
        """Return the quantity cell for a cart item."""
        return self.cart_item_by_name(product_name).locator(".cart_quantity")

    def item_total(self, product_name: str) -> Locator:
        """Return the total cell for a cart item."""
        return self.cart_item_by_name(product_name).locator(".cart_total")

    def remove_item(self, product_name: str) -> None:
        """Remove a cart item by product name."""
        cart_item = self.cart_item_by_name(product_name)
        cart_item.locator(".cart_quantity_delete").click()
        try:
            cart_item.wait_for(state="detached", timeout=10_000)
        except TimeoutError:
            cart_item.locator(".cart_quantity_delete").click()
            cart_item.wait_for(state="detached")

    def proceed_to_checkout(self) -> None:
        """Click Proceed To Checkout."""
        self.proceed_to_checkout_link.scroll_into_view_if_needed()
        self.proceed_to_checkout_link.click()
        try:
            self.page.wait_for_url("**/checkout", timeout=10_000)
        except TimeoutError:
            try:
                self.checkout_modal.wait_for(state="visible", timeout=3_000)
            except TimeoutError:
                self.proceed_to_checkout_link.click()
                try:
                    self.page.wait_for_url("**/checkout", timeout=10_000)
                except TimeoutError:
                    self.checkout_modal.wait_for(state="visible")

    def go_to_register_login_from_checkout_modal(self) -> None:
        """Open signup/login from the checkout modal."""
        self.checkout_modal.wait_for(state="visible")
        self.register_login_link.click()
