from .pages.image_page import ImagePage
from .pages.main_page import MainPage

site_name = "https://yandex.ru/"
expected_url = "https://yandex.ru/images/"


class TestGuestUseImageSearchInYandex:
    def test_guest_can_see_image_link(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.open()
        main_page.should_be_image_link()

    def test_guest_should_go_to_image_page(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.go_to_image_page()
        browser.switch_to.window(browser.window_handles[1])
        image_page = ImagePage(browser, browser.current_url)
        image_page.should_be_image_page(expected_url)

    def test_guest_should_open_first_category_image(self, browser):
        image_page = ImagePage(browser, browser.current_url)
        image_page.should_open_first_category_image()

    def test_guest_should_open_first_image(self, browser):
        image_page = ImagePage(browser, browser.current_url)
        image_page.should_open_first_image()

    def test_should_be_switch_image_forward_and_backward(self, browser):
        image_page = ImagePage(browser, browser.current_url)
        image_page.should_be_switch_to_next_and_prev_image()
