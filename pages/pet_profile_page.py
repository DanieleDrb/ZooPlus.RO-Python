import time
import pyautogui

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.pet_profile_data import PetProfileData


class PetProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.select = Select

    def select_created_pet_profile(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div:nth-child(2) > article:nth-child(1) > div:nth-child(1) > a:nth-child(3)")
        )).click()

    def assert_name_pet(self):
        actual_pet_name = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Chicco']").text
        assert actual_pet_name == PetProfileData.pet_name
        return print(f" Name of the pet : {actual_pet_name}")

    def assert_description_pet(self):
        actual_description_pet = self.driver.find_element(
            By.XPATH, "//dd[@class='z-p1 PetView-module__descriptionText--U41NAlP_JJ']").text
        assert actual_description_pet == PetProfileData.pet_description
        return print(f" Description : {actual_description_pet}")

    def assert_breed_pet(self):
        actual_breed_pet = self.driver.find_element(
            By.XPATH, "//dd[@class='z-h4 PetView-module__breedText--Mr8Q80bPw4']").text
        assert actual_breed_pet == PetProfileData.pet_breed
        return print(f" Breed : {actual_breed_pet}")

    def assert_gender_pet(self):
        actual_gender_pet = self.driver.find_element(
            By.XPATH, "//span[@class='PetView-module__genderMaleText--hvHveaN3xB']").text
        assert "M" in actual_gender_pet
        return print(f" Sex : {actual_gender_pet}")

    def edit_pet_data(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Editează datele animăluțului')]")
        )).click()

    def add_image(self):
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             ".Picture-module__galleryClickable--cW9OntkJEC > div:nth-child(1) > button:nth-child(1) > svg:nth-child(1)")
        )).click()

        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".PictureEdit-module__addPictureButton--_jfcoHF9d9")
        )).click()

        image_path = "C:\\Users\\dany_\\Interfata\\Desktop\\Open\\wego\\German Shepherd Dog1.jpg"
        time.sleep(1)
        pyautogui.write(image_path)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

    def save_button(self):
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#mpp-form-terms-agreement")
        )).click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Salvare']").click()

    def assert_presence_of_image(self):
        profile_image = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR,
             "div[class='Picture-module__squareImageGallery--wLYFmweUz6 Picture-module__squareImage--zHS_x6hwGC'] img")
        ))
        assert profile_image.is_displayed()
    
    def delete_pet(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Șterge')]")
        )).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Eliminare']")
        )).click()

