"""Account information page object."""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class AccountInformationPage(BasePage):
    """Locators and actions for the account creation form."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading = page.get_by_role("heading", name="ENTER ACCOUNT INFORMATION")
        self.title_mr_radio = page.locator("#id_gender1")
        self.title_mrs_radio = page.locator("#id_gender2")
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.day_select = page.locator("#days")
        self.month_select = page.locator("#months")
        self.year_select = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.locator("#mobile_number")
        self.create_account_button = page.get_by_role("button", name="Create Account")

    def fill_required_account_details(
        self,
        *,
        password: str,
        first_name: str,
        last_name: str,
        company: str,
        address1: str,
        address2: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile_number: str,
    ) -> None:
        """Fill the full account-information form with stable test data."""
        self.title_mr_radio.check()
        self.password_input.fill(password)
        self.day_select.select_option("1")
        self.month_select.select_option("1")
        self.year_select.select_option("2000")
        self.newsletter_checkbox.check()
        self.offers_checkbox.check()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address1_input.fill(address1)
        self.address2_input.fill(address2)
        self.country_select.select_option(country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_number_input.fill(mobile_number)

    def create_account(self) -> None:
        """Submit the account creation form."""
        self.create_account_button.click()
