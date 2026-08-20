import pytest
from pages.login_page import LoginPage


def test_login_locked_out_user(driver):
    """Test 3: Verify login blockage and error message for locked_out_user."""
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    error_message = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out." in error_message, (
        f"Unexpected error message: {error_message}"
    )
