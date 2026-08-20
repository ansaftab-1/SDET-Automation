import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(driver):
    """Test 1: Verify successful login with valid credentials (standard_user)."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in inventory_page.get_current_url(), "URL did not match inventory.html"
    assert inventory_page.get_title_text() == "Products", "Title header did not match 'Products'"
    assert inventory_page.get_item_count() == 6, "Expected 6 inventory items on the page"

