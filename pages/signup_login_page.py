"""Signup and login page object."""

from __future__ import annotations

from playwright.sync_api import Locator

from pages.base_page import BasePage


class SignupLoginPage(BasePage):
    """Locators and actions for the signup/login page."""

    url = "/login"

    @property
    def login_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Login to your account")

    @property
    def signup_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="New User Signup!")

    @property
    def login_form(self) -> Locator:
        return self.page.locator("form[action='/login']")

    @property
    def signup_form(self) -> Locator:
        return self.page.locator("form[action='/signup']")

    @property
    def login_email_input(self) -> Locator:
        return self.login_form.get_by_placeholder("Email Address")

    @property
    def login_password_input(self) -> Locator:
        return self.login_form.get_by_placeholder("Password")

    @property
    def login_button(self) -> Locator:
        return self.login_form.get_by_role("button", name="Login")

    @property
    def signup_name_input(self) -> Locator:
        return self.signup_form.get_by_placeholder("Name")

    @property
    def signup_email_input(self) -> Locator:
        return self.signup_form.get_by_placeholder("Email Address")

    @property
    def signup_button(self) -> Locator:
        return self.signup_form.get_by_role("button", name="Signup")

    @property
    def invalid_login_message(self) -> Locator:
        return self.page.get_by_text("Your email or password is incorrect!")

    @property
    def existing_email_message(self) -> Locator:
        return self.page.get_by_text("Email Address already exist!")

    def load(self) -> None:
        """Open the signup/login page."""
        self.navigate()

    def login(self, *, email: str, password: str) -> None:
        """Submit the login form."""
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def signup(self, *, name: str, email: str) -> None:
        """Submit the first step of the signup form."""
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()
