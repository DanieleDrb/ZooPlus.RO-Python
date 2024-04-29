from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def description(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#description-header")

    def scroll_until_element_visible(self, element):
        while not element.is_displayed():
            ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

    def assert_presence_of_description(self):
        description_element = self.description()
        self.scroll_until_element_visible(description_element)
        assert description_element.is_displayed(), "Description element is not visible"











