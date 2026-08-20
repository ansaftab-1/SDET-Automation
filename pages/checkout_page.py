from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object for SauceDemo Checkout Pages (Step 1, Step 2, and Complete)."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_CONTAINER = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_complete_header_text(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_CONTAINER)
