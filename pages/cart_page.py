from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for SauceDemo Shopping Cart Page."""

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item_count(self) -> int:
        return len(self.find_all(self.CART_ITEMS))

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
