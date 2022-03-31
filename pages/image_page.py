from .base_page import BasePage
from .locators import ImagePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImagePage(BasePage):

    def should_be_image_page(self, expected_url):
        current_url = self.browser.current_url
        assert expected_url in current_url, "url is not correct"

    def should_open_first_category_image(self):
        first_category_image = self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY_IMAGE)
        first_category_image_name = first_category_image.text
        first_category_image.click()

        expected_url = first_category_image.get_attribute("href")
        current_url = self.browser.current_url

        search_field = self.browser.find_element(*ImagePageLocators.SEARCH_FIELD)
        search_field_value = search_field.get_attribute("value")

        assert expected_url == current_url, "invalid page opened"
        assert search_field_value == first_category_image_name, "invalid text in search field"

    def should_open_first_image(self):
        first_image = self.browser.find_element(*ImagePageLocators.FIRST_IMAGE)
        first_image_url = first_image.get_attribute("href").split("url=")[1].split("&")[0]
        first_image.click()
        WebDriverWait(self.browser, 5).until(EC.url_contains(first_image_url))
        assert first_image_url in self.browser.current_url, "first image do not open"

    def should_be_switch_to_next_and_prev_image(self):
        prev_page_url = self.browser.current_url
        button_next = self.browser.find_element(*ImagePageLocators.BUTTON_NEXT)
        button_next.click()
        WebDriverWait(self.browser, 5).until(EC.url_changes(prev_page_url))
        next_page_url = self.browser.current_url
        assert prev_page_url != next_page_url, "Next image do not open"

        button_prev = self.browser.find_element(*ImagePageLocators.BUTTON_PREV)
        button_prev.click()
        WebDriverWait(self.browser, 5).until(EC.url_changes(next_page_url))
        assert prev_page_url == self.browser.current_url, "Prev image do not open"

