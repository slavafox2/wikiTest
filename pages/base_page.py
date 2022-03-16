from typing import Any


class Page:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, *locator) -> Any:
        return self.driver.find_element(*locator)

    def click(self, *locator):
        e = self.find_element(*locator)
        e.click()

    def input(self, text, *locator):
        self.driver.find_element(*locator).clear().send_keys(text)
