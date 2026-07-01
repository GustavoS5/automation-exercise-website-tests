"""Contact us page object."""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Locator

from pages.base_page import BasePage


class ContactUsPage(BasePage):
    """Locators and actions for the contact form."""

    url = "/contact_us"

    @property
    def contact_us_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="CONTACT US")

    @property
    def get_in_touch_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="GET IN TOUCH")

    @property
    def form(self) -> Locator:
        return self.page.locator("#contact-us-form")

    @property
    def name_input(self) -> Locator:
        return self.form.get_by_placeholder("Name")

    @property
    def email_input(self) -> Locator:
        return self.form.get_by_placeholder("Email")

    @property
    def subject_input(self) -> Locator:
        return self.form.get_by_placeholder("Subject")

    @property
    def message_textarea(self) -> Locator:
        return self.form.get_by_placeholder("Your Message Here")

    @property
    def upload_file_input(self) -> Locator:
        return self.form.locator("input[name='upload_file']")

    @property
    def submit_button(self) -> Locator:
        return self.form.locator("input[name='submit']")

    @property
    def success_message(self) -> Locator:
        return self.page.locator(".status.alert-success")

    def load(self) -> None:
        """Open the contact page."""
        self.navigate()

    def fill_contact_details(
        self,
        *,
        name: str,
        email: str,
        subject: str,
        message: str,
    ) -> None:
        """Fill the contact form fields that are always required."""
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_textarea.fill(message)

    def upload_file(self, file_path: Path) -> None:
        """Attach a file to the contact form."""
        self.upload_file_input.set_input_files(file_path)

    def submit(self) -> None:
        """Submit the contact form."""
        self.submit_button.click()
