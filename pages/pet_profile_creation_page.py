
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.pet_profile_data import PetProfileData


class PetProfileCreation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.select = Select

    def create_new_profile(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Creează profilul animăluțului')]")
        )).click()
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Creează profilul animalului')]")
        )).click()

    def select_type_of_animal(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "label[aria-label='" + PetProfileData.pet_type + "']")
        )).click()

    def pet_breed(self):
        return (self.driver.find_element(
            By.CSS_SELECTOR, "label[aria-label='" + PetProfileData.pet_breed + "']")
                .click())

    def animal_name_input(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mpp-form-name")
        )).send_keys(PetProfileData.pet_name)

    def animal_nickname_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#mpp-form-nickname").send_keys(PetProfileData.pet_nickname)

    def animal_gender_select(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#gender-" + PetProfileData.pet_gender + "").click()

    def continue_button(self):
        return self.driver.find_element(By.XPATH, "//button[contains(text(),'Continuă')]").click()

    def animal_birthday(self):
        return self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#mpp-form-birthday")
            )).click()

    def select_month_and_year(self):
        month_dropdown = Select(self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "select[name='month']")
        )))
        month_dropdown.select_by_visible_text(PetProfileData.month)

        year_dropdown = Select(self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "select[name='year']")
        )))
        year_dropdown.select_by_visible_text(PetProfileData.year)

    def select_day(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'" + PetProfileData.day + "')]").click()

    def search_food_brand(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#favouriteFoodBrands")
        )).send_keys("Wolf of Wilderness")

    def select_food_brand(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "label[aria-label='" + PetProfileData.food_brand + "']")
        )).click()

    def select_sensibility(self):
        return self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'" + PetProfileData.sensibility + "')]")
        )).click()

    def enter_description_pet(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mpp-form-description")
        )).send_keys(PetProfileData.pet_description)

    def select_color_avatar(self):
        return (self.driver.find_element(By.CSS_SELECTOR, "label[aria-label='" + PetProfileData.color_avatar + "']")
                .click())

    def consent_pet_info(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#mpp-form-gdpr-consent").click()

    def agreement_terms_and_conditions(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#mpp-form-terms-agreement").click()

    def save_button(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Salvare']").click()








