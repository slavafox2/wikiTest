from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.first_setting_page import FirstSettingPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.search_page = SearchPage(driver)
        self.first_setting_page = FirstSettingPage(driver)
