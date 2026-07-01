"""Smoke tests proving header navigation works with ads blocked.

These exercises hit exactly the header links that AdSense's
``#google_vignette`` overlay was intercepting during Playwright's
auto-waiting clicks. With the ``block_ads`` autouse fixture in
``conftest.py`` active, the ad iframe never loads, so the clicks reach the
real target.
"""

from __future__ import annotations

import pytest
from pages.home_page import HomePage

pytestmark = pytest.mark.smoke


def test_header_navigation_to_products(home_page: HomePage) -> None:
    """Products link in the shared header reaches the all-products listing."""
    home_page.go_to_products()
    assert home_page.current_url.rstrip("/").endswith("/products")


def test_header_navigation_to_cart(home_page: HomePage) -> None:
    """Cart link in the shared header reaches the cart page."""
    home_page.go_to_cart()
    assert "/view_cart" in home_page.current_url


def test_header_navigation_to_contact_us(home_page: HomePage) -> None:
    """Contact Us link in the shared header reaches the contact page."""
    home_page.go_to_contact_us()
    assert "/contact_us" in home_page.current_url


def test_header_navigation_to_signup_login(home_page: HomePage) -> None:
    """Signup/Login link in the shared header reaches the login page."""
    home_page.go_to_signup_login()
    assert "/login" in home_page.current_url


def test_header_navigation_back_home(home_page: HomePage) -> None:
    """After navigating away, the Home link returns to the landing page.

    The home URL is the site root: ``https://automationexercise.com/``. We
    compare the URL authority only, so we are immune to whether the trailing
    slash is present.
    """
    home_page.go_to_products()
    assert home_page.current_url.rstrip("/").endswith("/products")
    home_page.go_to_home()
    parsed = home_page.current_url.split("://", 1)[-1]  # drop scheme
    assert "/" not in parsed.rstrip("/")
    assert parsed.split("/", 1)[0] == "automationexercise.com"
