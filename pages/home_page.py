"""Home page object for automationexercise.com."""

from __future__ import annotations

import re

from playwright.sync_api import Locator

from pages.base_page import BasePage


class HomePage(BasePage):
    """Locators and actions for the public home page."""

    url = "/"

    @property
    def hero_heading(self) -> Locator:
        return self.page.get_by_role(
            "heading",
            name=re.compile("Full-Fledged practice website", re.IGNORECASE),
        ).first

    @property
    def features_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="FEATURES ITEMS")

    @property
    def product_cards(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper")

    def product_card_by_name(self, product_name: str) -> Locator:
        """Return a product card containing the requested product name."""
        return self.product_cards.filter(has_text=product_name).first

    def load(self) -> None:
        """Open the home page."""
        self.navigate()
