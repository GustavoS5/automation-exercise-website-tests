"""Checkout, order, invoice, and cart persistence coverage."""

from __future__ import annotations

import pytest
from faker import Faker
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.signup_login_page import SignupLoginPage
from playwright.sync_api import Page, expect

from tests.helpers import (
    add_first_product_and_open_cart,
    create_account_and_continue,
    delete_account_after_order,
    delete_current_account,
    make_account_data,
    place_order_from_checkout,
)


@pytest.mark.e2e
def test_order_can_be_placed_after_registering_from_checkout(
    page: Page,
    faker: Faker,
) -> None:
    """A shopper can register from checkout and place an order."""
    account = make_account_data(faker)
    cart_page = add_first_product_and_open_cart(page)

    cart_page.proceed_to_checkout()
    cart_page.go_to_register_login_from_checkout_modal()
    create_account_and_continue(page, account)

    HomePage(page).go_to_cart()
    CartPage(page).proceed_to_checkout()
    place_order_from_checkout(page, account)
    delete_account_after_order(page)


@pytest.mark.e2e
def test_order_can_be_placed_after_registering_before_checkout(
    page: Page,
    faker: Faker,
) -> None:
    """A registered shopper can place an order from checkout."""
    account = make_account_data(faker)
    create_account_and_continue(page, account)
    cart_page = add_first_product_and_open_cart(page)

    cart_page.proceed_to_checkout()
    place_order_from_checkout(page, account)
    delete_account_after_order(page)


@pytest.mark.e2e
def test_order_can_be_placed_after_login_before_checkout(
    page: Page,
    faker: Faker,
) -> None:
    """A returning shopper can log in and place an order."""
    account = make_account_data(faker)
    home_page = create_account_and_continue(page, account)
    home_page.logout()

    signup_login_page = SignupLoginPage(page)
    signup_login_page.login(email=account.email, password=account.password)
    expect(HomePage(page).logged_in_as_link).to_contain_text(account.name)

    cart_page = add_first_product_and_open_cart(page)
    cart_page.proceed_to_checkout()
    place_order_from_checkout(page, account)
    delete_account_after_order(page)


@pytest.mark.e2e
def test_searched_cart_items_persist_after_login(page: Page, faker: Faker) -> None:
    """Searched products added to the cart remain visible after login."""
    account = make_account_data(faker)
    products_page = ProductsPage(page)
    products_page.load()

    expect(products_page.all_products_heading).to_be_visible()
    products_page.search("Blue Top")
    expect(products_page.searched_products_heading).to_be_visible()
    products_page.add_product_to_cart_by_name("Blue Top").view_cart()
    expect(CartPage(page).cart_item_by_name("Blue Top")).to_be_visible()

    CartPage(page).go_to_signup_login()
    create_account_and_continue(page, account)

    HomePage(page).go_to_cart()
    expect(CartPage(page).cart_item_by_name("Blue Top")).to_be_visible()

    delete_current_account(page)


@pytest.mark.e2e
def test_checkout_addresses_match_registered_account(
    page: Page,
    faker: Faker,
) -> None:
    """Checkout delivery and billing addresses match registration details."""
    account = make_account_data(faker)
    create_account_and_continue(page, account)

    add_first_product_and_open_cart(page).proceed_to_checkout()
    checkout_page = CheckoutPage(page)

    expect(checkout_page.delivery_address).to_contain_text(account.first_name)
    expect(checkout_page.delivery_address).to_contain_text(account.last_name)
    expect(checkout_page.delivery_address).to_contain_text(account.address1)
    expect(checkout_page.delivery_address).to_contain_text(account.city)
    expect(checkout_page.billing_address).to_contain_text(account.first_name)
    expect(checkout_page.billing_address).to_contain_text(account.last_name)
    expect(checkout_page.billing_address).to_contain_text(account.address1)
    expect(checkout_page.billing_address).to_contain_text(account.city)

    delete_current_account(page)


@pytest.mark.e2e
def test_invoice_can_be_downloaded_after_order(
    page: Page,
    faker: Faker,
) -> None:
    """An invoice can be downloaded after placing an order."""
    account = make_account_data(faker)
    cart_page = add_first_product_and_open_cart(page)

    cart_page.proceed_to_checkout()
    cart_page.go_to_register_login_from_checkout_modal()
    create_account_and_continue(page, account)

    HomePage(page).go_to_cart()
    CartPage(page).proceed_to_checkout()
    order_placed_page = place_order_from_checkout(page, account)
    download = order_placed_page.download_invoice()

    assert download.suggested_filename

    delete_account_after_order(page)
