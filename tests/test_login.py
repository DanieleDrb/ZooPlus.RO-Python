
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utilities.data import Data


@pytest.fixture(scope="function")
def setup_teardown():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(setup_teardown):
    def _login_page():
        return LoginPage(setup_teardown)
    yield _login_page()


@pytest.fixture(scope="function")
def home_page(setup_teardown):
    def _home_page():
        return HomePage(setup_teardown)
    yield _home_page()


def test_account_log_in_log_out(login_page, home_page):
    user = Data().login()
    home_page.open()
    home_page.cookie_button()
    home_page.my_zooplus_button()
    login_page.login(user)
    login_page.assert_account_logged_in()
    login_page.log_out()
    home_page.my_zooplus_button()










