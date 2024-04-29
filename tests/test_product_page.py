
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def setup_teardown():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(setup_teardown):
    def _home_page():
        return HomePage(setup_teardown)
    yield _home_page()


@pytest.fixture(scope="function")
def product_page(setup_teardown):
    def _product_page():
        return ProductPage(setup_teardown)
    yield _product_page()


def test_presence_of_description_product(home_page, product_page):
    # Open the website and accept cookie
    home_page.open()
    home_page.cookie_button()
    # Go to the page product
    home_page.input_food_name()
    home_page.search_button()
    home_page.selected_product()
    # Verify the presence of description in the product page
    product_page.assert_presence_of_description()
















