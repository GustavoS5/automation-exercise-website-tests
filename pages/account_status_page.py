"""Account status pages for created/deleted states."""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class AccountStatusPage(BasePage):
    """Shared object for account created and deleted confirmation pages."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.account_created_heading = page.locator("b").filter(
            has_text="ACCOUNT CREATED!"
        )
        self.account_deleted_heading = page.locator("b").filter(
            has_text="ACCOUNT DELETED!"
        )
        self.continue_link = page.get_by_role("link", name="Continue").first

    def continue_to_site(self) -> None:
        """Continue from an account status page."""
        self.continue_link.click()
