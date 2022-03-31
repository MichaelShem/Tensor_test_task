from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST_FIELD = (By.CSS_SELECTOR, ".mini-suggest__popup_visible")
    SEARCH_RESULT_LIST = (By.CSS_SELECTOR, "#search-result > li")
    LINKS = (By.TAG_NAME, "a")
    IMAGE_LINK = (By.CSS_SELECTOR, 'a[data-id="images"]')


class ImagePageLocators:
    FIRST_CATEGORY_IMAGE = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 a")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item_pos_0 a")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input.mini-suggest__input")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".MediaViewer-ButtonNext")
    BUTTON_PREV = (By.CSS_SELECTOR, ".MediaViewer-ButtonPrev")
