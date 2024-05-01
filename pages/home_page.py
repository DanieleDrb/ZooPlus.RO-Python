import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.zooplus.ro/")

    def my_zooplus_button(self):
        time.sleep(1)
        return self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div:nth-child(3) > div:nth-child(1) > a:nth-child(2) > div:nth-child(2)"))
        ).click()

    def cookie_button(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='onetrust-reject-all-handler']"
        ))).click()

    def input_food_name(self, food_name):
        return self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#search_query_field_desktop")
        )).send_keys(food_name)

    def search_button(self):
        time.sleep(1)
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-zta='search_form_button_desktop']//*[name()='svg']")
        )).click()

    def selected_product_1(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@id='594865']")
        )).click()

    def selected_product_2(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@id='1011019']")
        )).click()









