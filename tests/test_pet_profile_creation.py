
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.pet_profile_creation_page import PetProfileCreation
from pages.pet_profile_page import PetProfilePage
from utilities.data import Data


@pytest.fixture(scope="function")
def setup_teardown():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(setup_teardown):
    return HomePage(setup_teardown)


@pytest.fixture(scope="function")
def login_page(setup_teardown):
    return LoginPage(setup_teardown)


@pytest.fixture(scope="function")
def pet_profile_creation_page(setup_teardown):
    return PetProfileCreation(setup_teardown)


@pytest.fixture(scope="function")
def pet_profile_page(setup_teardown):
    return PetProfilePage(setup_teardown)


@pytest.mark.priority(level=1)
def test_pet_profile_successfully_created(home_page, login_page, pet_profile_creation_page):
    # Email + password for login
    user = Data().login()
    # Open the website and accept cookie
    home_page.open()
    home_page.cookie_button()
    # Go to the login page and login
    home_page.my_zooplus_button()
    login_page.login(user)
    # Navigate to pet profile creation page
    pet_profile_creation_page.create_new_profile()
    # Fill out profile form:
    # Step 1: Select animal type
    pet_profile_creation_page.select_type_of_animal()
    # Step 2: What breed is your dog?
    pet_profile_creation_page.pet_breed()
    # Step 3: Personal information about your dog
    pet_profile_creation_page.animal_name_input()
    pet_profile_creation_page.animal_nickname_input()
    pet_profile_creation_page.animal_gender_select()
    pet_profile_creation_page.continue_button()
    # Step 4: When is his birthday?
    pet_profile_creation_page.animal_birthday()
    pet_profile_creation_page.select_month_and_year()
    pet_profile_creation_page.select_day()
    pet_profile_creation_page.continue_button()
    # Step 5: What does (name of the pet) prefer to eat?
    pet_profile_creation_page.search_food_brand()
    pet_profile_creation_page.select_food_brand()
    pet_profile_creation_page.continue_button()
    # Step 6: Does (name of the pet) have any special needs?
    pet_profile_creation_page.select_sensibility()
    # Step 7: Do you have other details to add about (name of the pet)?
    pet_profile_creation_page.enter_description_pet()
    pet_profile_creation_page.select_color_avatar()
    pet_profile_creation_page.consent_pet_info()
    pet_profile_creation_page.agreement_terms_and_conditions()
    # Submit the profile form
    pet_profile_creation_page.save_button()


@pytest.mark.priority(level=2)
def test_assert_creation_of_pet_profile(home_page, login_page, pet_profile_page):
    # Email + password for login
    user = Data().login()
    # Open the website and accept cookie
    home_page.open()
    home_page.cookie_button()
    # Go to the login page and login
    home_page.my_zooplus_button()
    login_page.login(user)
    login_page.see_the_pets()
    # Select the pet we have just created
    pet_profile_page.select_created_pet_profile()
    # Verify name, breed, gender and description
    pet_profile_page.assert_name_pet()
    pet_profile_page.assert_breed_pet()
    pet_profile_page.assert_gender_pet()
    pet_profile_page.assert_description_pet()


@pytest.mark.priority(level=3)
def test_upload_image(home_page, login_page, pet_profile_page):
    # Email + password for login
    user = Data().login()
    # Open the website and accept cookie
    home_page.open()
    home_page.cookie_button()
    # Go to the login page and login
    home_page.my_zooplus_button()
    login_page.login(user)
    login_page.see_the_pets()
    # Select the pet we have just created
    pet_profile_page.select_created_pet_profile()
    # Add the image from my PC
    pet_profile_page.add_image()
    # Save the image in the profile
    pet_profile_page.save_button()
    # Verify if the image is saved as expected
    pet_profile_page.assert_presence_of_image()


@pytest.mark.priority(level=4)
def test_delete_pet_profile(home_page, login_page, pet_profile_page):
    # Email + password for login
    user = Data().login()
    # Open the website and accept cookie
    home_page.open()
    home_page.cookie_button()
    # Go to the login page and login
    home_page.my_zooplus_button()
    login_page.login(user)
    login_page.see_the_pets()
    # Select the pet we have just created
    pet_profile_page.select_created_pet_profile()
    # Go to edit pet data page
    pet_profile_page.edit_pet_data()
    # Delete pet profile
    pet_profile_page.delete_pet()
















