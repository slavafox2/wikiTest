from selenium.webdriver.common.by import By 
from pages.base_page import Page

class FirstSettingPage(Page):
    #  context.driver.find_element(By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()
    SEARCH_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')

    def skip_button(self, *locator):
        self.click(*self.SEARCH_BUTTON)