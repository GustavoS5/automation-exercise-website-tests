"""Product detail page object."""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.cart_modal import CartModal


class ProductDetailPage(BasePage):
    """Locators and actions for a single product detail page."""

    url = "/product_details/1"

    def __init__(self, page: Page, product_id: int = 1) -> None:
        super().__init__(page)
        self.product_id = product_id
        self.product_information = page.locator(".product-information")
        self.product_name = self.product_information.locator("h2")
        self.category_text = self.product_information.locator("p").filter(
            has_text="Category"
        )
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_button = page.locator("button.cart")
        self.review_name_input = page.locator("#review-form #name")
        self.review_email_input = page.locator("#review-form #email")
        self.review_textarea = page.locator("#review-form #review")
        self.review_submit_button = page.locator("#button-review")

    def load(self, product_id: int | None = None) -> None:
        """Open a product details page by product id."""
        if product_id is not None:
            self.product_id = product_id

        self.page.goto(f"/product_details/{self.product_id}")

    def set_quantity(self, quantity: int) -> None:
        """Set the quantity before adding the product to cart."""
        self.quantity_input.fill(str(quantity))

    def add_to_cart(self) -> CartModal:
        """Add the displayed product to cart and return the modal component."""
        self.add_to_cart_button.click()
        modal = CartModal(self.page)
        modal.wait_until_visible()
        return modal

    def fill_review(self, *, name: str, email: str, review: str) -> None:
        """Fill the product review form."""
        self.review_name_input.fill(name)
        self.review_email_input.fill(email)
        self.review_textarea.fill(review)
