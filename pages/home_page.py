"""Home page object for automationexercise.com."""

from __future__ import annotations

import re

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class HomePage(BasePage):
    """Locators and actions for the public home page."""

    url = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.hero_heading = page.get_by_role(
            "heading",
            name=re.compile("Full-Fledged practice website", re.IGNORECASE),
        ).first
        self.features_heading = page.get_by_role("heading", name="FEATURES ITEMS")
        self.product_cards = page.locator(".features_items .product-image-wrapper")

    def product_card_by_name(self, product_name: str) -> Locator:
        """Return a product card containing the requested product name."""
        return self.product_cards.filter(has_text=product_name).first

    def load(self) -> None:
        """Open the home page."""
        self.navigate()
