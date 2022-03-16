
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchPage(Page):
    SEARCH_FIELD = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')
    SEARCH_RESULT_WRONG = (By.ID, 'org.wikipedia:id/results_text')

    def input_search(self, search_phrase: str):
        Page.input(self, search_phrase, *self.SEARCH_FIELD)

    def verify_search_result(self, search_phrase: str):
        result_text = Page.find_element(self, *self.SEARCH_RESULT).text
        assert search_phrase in result_text, f'Expected {search_phrase} to be in {result_text}'

    def verify_search_result_empty(self, search_phrase: str):
        result_text_empty = Page.find_element(self, *self.SEARCH_RESULT_WRONG).text
        assert result_text_empty == search_phrase, f'Expected {search_phrase} but got {result_text_empty}'
