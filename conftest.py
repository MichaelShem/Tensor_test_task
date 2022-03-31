import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    print("\nstart browser for test..")

    yield browser
    print("\nquit browser..")
    browser.quit()
