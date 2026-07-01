"""Product detail page object."""

from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.cart_modal import CartModal


class ProductDetailPage(BasePage):
    """Locators and actions for a single product detail page."""

    url = "/product_details/1"

    def __init__(self, page: Page, product_id: int = 1) -> None:
        super().__init__(page)
        self.product_id = product_id

    @property
    def product_information(self) -> Locator:
        return self.page.locator(".product-information")

    @property
    def product_name(self) -> Locator:
        return self.product_information.locator("h2")

    @property
    def category_text(self) -> Locator:
        return self.product_information.locator("p").filter(has_text="Category")

    @property
    def quantity_input(self) -> Locator:
        return self.page.locator("#quantity")

    @property
    def add_to_cart_button(self) -> Locator:
        return self.page.locator("button.cart")

    @property
    def review_name_input(self) -> Locator:
        return self.page.locator("#review-form #name")

    @property
    def review_email_input(self) -> Locator:
        return self.page.locator("#review-form #email")

    @property
    def review_textarea(self) -> Locator:
        return self.page.locator("#review-form #review")

    @property
    def review_submit_button(self) -> Locator:
        return self.page.locator("#button-review")

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
