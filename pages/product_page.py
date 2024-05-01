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

    def select_and_assert_of_analysis_section(self):
    self.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#constituents-header")
    )).click()
    analysis_element_1 = self.wait.until(EC.presence_of_element_located(
        (By.XPATH, "//td[normalize-space()='proteine']")
    )).text
    analysis_element_2 = self.driver.find_element(
        By.XPATH, "//td[contains(text(),'acizi graşi Omega-6')]").text
    assert analysis_element_1 == "proteine", "Analysis section is not displayed as expected"
    assert analysis_element_2 == "acizi graşi Omega-6", "Analysis section is not displayed as expected"






