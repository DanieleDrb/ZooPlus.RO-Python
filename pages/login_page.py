
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def email_address_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#username")

    def password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#password")

    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#login-btn")

    def login(self, user):
        if user.get_email_address() != "":
            self.email_address_input().send_keys(user.get_email_address())

        if user.get_password() != "":
            self.password_input().send_keys(user.get_password())

        if user:
            self.login_button().click()

    def main_heading(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[@class='z-anchor WelcomeSection-module_logoutLink__nBmjE']")
        )).text

    def assert_account_logged_in(self):
        assert self.main_heading() == "Delogare"

    def log_out(self):
        return self.driver.find_element(
            By.XPATH, "//a[@class='z-anchor WelcomeSection-module_logoutLink__nBmjE']").click()

    def assert_account_logged_out(self):
        assert self.login_button().is_displayed(), "Account didn't log out"

    def see_the_pets(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Vezi animăluțele')]")
        )).click()






