import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_add_to_cart_and_complete_checkout(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    assert inventory.get_cart_badge_count() == "1"

    inventory.go_to_cart()
    assert "cart.html" in cart.get_current_url()
    assert cart.get_cart_item_count() == 1

    cart.click_checkout()
    assert "checkout-step-one.html" in checkout.get_current_url()

    checkout.fill_checkout_info("John", "Doe", "90210")
    assert "checkout-step-two.html" in checkout.get_current_url()

    checkout.click_finish()
    assert "checkout-complete.html" in checkout.get_current_url()

    header = checkout.get_complete_header_text()
    assert "Thank you for your order" in header
