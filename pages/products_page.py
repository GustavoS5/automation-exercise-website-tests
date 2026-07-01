"""Products listing page object."""

from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.cart_modal import CartModal


class ProductsPage(BasePage):
    """Locators and actions for the all-products listing."""

    url = "/products"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.all_products_heading = page.get_by_role("heading", name="ALL PRODUCTS")
        self.searched_products_heading = page.get_by_role(
            "heading", name="SEARCHED PRODUCTS"
        )
        self.search_input = page.get_by_placeholder("Search Product")
        self.search_button = page.locator("#submit_search")
        self.product_cards = page.locator(".features_items .product-image-wrapper")

    def load(self) -> None:
        """Open the products listing page."""
        self.navigate()

    def search(self, term: str) -> None:
        """Search products by name or category text."""
        self.search_input.fill(term)
        self.search_button.click()

    def product_card_by_name(self, product_name: str) -> Locator:
        """Return a product card containing the requested product name."""
        return self.product_cards.filter(has_text=product_name).first

    def view_product_by_id(self, product_id: int) -> None:
        """Open a product detail page from the listing."""
        self.page.locator(f"a[href='/product_details/{product_id}']").first.click()

    def _add_to_cart_link_by_id(self, product_id: int) -> Locator:
        return self.page.locator(f"a.add-to-cart[data-product-id='{product_id}']").first

    def add_product_to_cart_by_id(self, product_id: int) -> CartModal:
        """Add a product to cart from the listing by product id."""
        self._add_to_cart_link_by_id(product_id).click()
        modal = CartModal(self.page)
        modal.wait_until_visible()
        return modal

    def add_product_to_cart_by_name(self, product_name: str) -> CartModal:
        """Add a product to cart from the listing by visible product name."""
        self.product_card_by_name(product_name).locator("a.add-to-cart").first.click()
        modal = CartModal(self.page)
        modal.wait_until_visible()
        return modal
