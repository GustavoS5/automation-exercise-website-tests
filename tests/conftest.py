"""Test-level fixtures for the Automation Exercise suite."""

from __future__ import annotations

import pytest
from pages.cart_page import CartPage
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.products_page import ProductsPage
from pages.signup_login_page import SignupLoginPage
from playwright.sync_api import Page


@pytest.fixture
def home_page(page: Page) -> HomePage:
    """A HomePage object already loaded in the browser."""
    home = HomePage(page)
    home.load()
    return home


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    """A ProductsPage object already loaded in the browser."""
    products = ProductsPage(page)
    products.load()
    return products


@pytest.fixture
def product_detail_page(page: Page) -> ProductDetailPage:
    """A ProductDetailPage object already loaded for the first product."""
    product_detail = ProductDetailPage(page)
    product_detail.load()
    return product_detail


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """A CartPage object already loaded in the browser."""
    cart = CartPage(page)
    cart.load()
    return cart


@pytest.fixture
def signup_login_page(page: Page) -> SignupLoginPage:
    """A SignupLoginPage object already loaded in the browser."""
    signup_login = SignupLoginPage(page)
    signup_login.load()
    return signup_login


@pytest.fixture
def contact_us_page(page: Page) -> ContactUsPage:
    """A ContactUsPage object already loaded in the browser."""
    contact_us = ContactUsPage(page)
    contact_us.load()
    return contact_us
