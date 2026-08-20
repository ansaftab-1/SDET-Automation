from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base Page class providing common Selenium interaction wrappers."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.find_visible(locator)
        element.click()

    def type_text(self, locator, text: str):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    def get_current_url(self) -> str:
        return self.driver.current_url
