from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for SauceDemo Inventory (Products) Page."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_item_count(self) -> int:
        return len(self.find_all(self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def add_bike_light_to_cart(self):
        self.click(self.ADD_BIKE_LIGHT_BTN)

    def get_cart_badge_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def select_sort_option(self, value: str):
        dropdown = Select(self.find_visible(self.SORT_DROPDOWN))
        dropdown.select_by_value(value)

    def logout(self):
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)
