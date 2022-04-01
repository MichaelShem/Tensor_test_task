from .pages.main_page import MainPage

site_name = "https://yandex.ru/"
link_name = "tensor.ru"


class TestGuestUseSearchYandex:

    def test_quest_must_see_search_field(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.open()
        main_page.should_be_search_field()

    def test_quest_must_see_suggest_table(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.send_keys_in_the_search("тензор")
        main_page.should_be_suggest_field()

    def test_quest_must_see_search_result(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.key_down_enter()
        main_page.should_be_search_result_list()

    def test_guest_can_see_link_tensor_in_1_result(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.should_be_link_in_request(link_name, 1)

    def test_guest_can_see_link_tensor_in_2_result(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.should_be_link_in_request(link_name, 2)

    def test_guest_can_see_link_tensor_in_3_result(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.should_be_link_in_request(link_name, 3)

    def test_guest_can_see_link_tensor_in_4_result(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.should_be_link_in_request(link_name, 4)

    def test_guest_can_see_link_tensor_in_5_result(self, browser):
        main_page = MainPage(browser, site_name)
        main_page.should_be_link_in_request(link_name, 5)

