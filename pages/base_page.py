"""Base page object for the Playwright Page Object Model."""

from __future__ import annotations

import re

from playwright.sync_api import Locator, Page, Response


class BasePage:
    """Common state and navigation shared by every page object."""

    url: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.logo = page.locator("header a[href='/'] img").first
        self.home_link = page.locator("header a[href='/']").filter(
            has_text=re.compile("Home")
        )
        self.products_link = page.locator("header a[href='/products']").first
        self.cart_link = page.locator("header a[href='/view_cart']").first
        self.signup_login_link = page.locator("header a[href='/login']").first
        self.logout_link = page.locator("header a[href='/logout']").first
        self.delete_account_link = page.locator(
            "header a[href='/delete_account']"
        ).first
        self.logged_in_as_link = page.locator("header a").filter(
            has_text=re.compile("Logged in as")
        )
        self.contact_us_link = page.locator("header a[href='/contact_us']").first
        self.test_cases_link = page.locator("header a[href='/test_cases']").first
        self.subscription_heading = page.get_by_role("heading", name="SUBSCRIPTION")
        self.subscription_email_input = page.get_by_placeholder("Your email address")
        self.subscribe_button = page.locator("#subscribe")
        self.subscription_success_message = page.locator("#success-subscribe")

    def navigate(self) -> Response | None:
        """Open the page via `page.goto()`, resolved against `--base-url`."""
        return self.page.goto(self.url)

    @property
    def current_url(self) -> str:
        """The page's current full URL."""
        return str(self.page.url)

    def go_to_home(self) -> None:
        """Navigate to the home page from the shared header."""
        self.home_link.click()

    def go_to_products(self) -> None:
        """Navigate to the products listing from the shared header."""
        self.products_link.click()

    def go_to_cart(self) -> None:
        """Navigate to the cart from the shared header."""
        self.cart_link.click()

    def go_to_signup_login(self) -> None:
        """Navigate to the signup/login page from the shared header."""
        self.signup_login_link.click()

    def logout(self) -> None:
        """Log out through the shared header."""
        self.logout_link.click()

    def delete_account(self) -> None:
        """Delete the logged-in account through the shared header."""
        self.delete_account_link.click()

    def go_to_contact_us(self) -> None:
        """Navigate to the contact page from the shared header."""
        self.contact_us_link.click()

    def go_to_test_cases(self) -> None:
        """Navigate to the test cases page from the shared header."""
        self.test_cases_link.click()

    def subscribe(self, email: str) -> Locator:
        """Subscribe from the shared footer and return the success message."""
        self.subscription_email_input.fill(email)
        self.subscribe_button.click()
        return self.subscription_success_message
