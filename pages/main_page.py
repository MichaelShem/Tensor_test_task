from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def send_keys_in_the_search(self, keys):
        input_keys = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        input_keys.send_keys(keys)

    def should_be_image_link(self):
        assert self.is_element_present(*MainPageLocators.IMAGE_LINK), "image link is not present"

    def should_be_link_in_request(self, link_name, result_number):
        result_list = self.browser.find_elements(*MainPageLocators.SEARCH_RESULT_LIST)
        link = result_list[result_number-1].find_elements(*MainPageLocators.LINKS)
        for href in link:
            if link_name in href.get_attribute("href"):
                return True
        assert False, f"link tensor.ru not found in result №{result_number}"

    def should_be_search_field(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), "search field is not presented"

    def should_be_suggest_field(self):
        assert self.is_element_present(*MainPageLocators.SUGGEST_FIELD), "suggest field is not presented"

    def should_be_search_result_list(self):
        assert self.browser.find_elements(*MainPageLocators.SEARCH_RESULT_LIST), "search result is not present"

    def go_to_image_page(self):
        assert self.browser.find_element(*MainPageLocators.IMAGE_LINK), "image link is not present"
        self.browser.find_element(*MainPageLocators.IMAGE_LINK).click()

