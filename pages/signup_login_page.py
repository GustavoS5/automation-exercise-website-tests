"""Signup and login page object."""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class SignupLoginPage(BasePage):
    """Locators and actions for the signup/login page."""

    url = "/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_heading = page.get_by_role("heading", name="Login to your account")
        self.signup_heading = page.get_by_role("heading", name="New User Signup!")
        self.login_form = page.locator("form[action='/login']")
        self.signup_form = page.locator("form[action='/signup']")
        # Field locators are scoped to their forms; assigned after the forms.
        self.login_email_input = self.login_form.get_by_placeholder("Email Address")
        self.login_password_input = self.login_form.get_by_placeholder("Password")
        self.login_button = self.login_form.get_by_role("button", name="Login")
        self.signup_name_input = self.signup_form.get_by_placeholder("Name")
        self.signup_email_input = self.signup_form.get_by_placeholder("Email Address")
        self.signup_button = self.signup_form.get_by_role("button", name="Signup")
        self.invalid_login_message = page.get_by_text(
            "Your email or password is incorrect!"
        )
        self.existing_email_message = page.get_by_text("Email Address already exist!")

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
