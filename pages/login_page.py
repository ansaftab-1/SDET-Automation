from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for SauceDemo Login Page."""

    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open_url(self.URL)

    def login(self, username: str = "standard_user", password: str = "secret_sauce"):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_CONTAINER)
