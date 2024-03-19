from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def add_new_employee(self, first_name, last_name):
        # Navigate to PIM module
        pim_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='PIM']")))
        ActionChains(self.driver).move_to_element(pim_menu).click().perform()

        # Click on Add button
        add_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
        ActionChains(self.driver).move_to_element(add_button).click().perform()

        # Fill in employee details
        first_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
        last_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)

        # Click on Save button
        save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        ActionChains(self.driver).move_to_element(save_button).click().perform()

        #Click on Save button
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']")))
        ActionChains(self.driver).move_to_element(save_button).click().perform()

        return f"{first_name} {last_name}"

    def edit_employee(self, first_name, last_name, new_last_name, other_id):
        # Navigate to PIM module
        pim_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='PIM']")))
        ActionChains(self.driver).move_to_element(pim_menu).click().perform()

        # Search for the employee using employee ID
        search_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")))
        search_input.send_keys(first_name + " " + last_name)
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
        ActionChains(self.driver).move_to_element(search_button).click().perform()

        # Click on employee to edit
        edit_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")))
        ActionChains(self.driver).move_to_element(edit_icon).click().perform()

        # Update employee details with provided updated_details
        last_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
        time.sleep(3)  # Add a small delay
        last_name_input.send_keys(Keys.CONTROL + "a")  # Select all text
        last_name_input.send_keys(Keys.BACKSPACE)  # Delete selected text
        time.sleep(3)  # Add a small delay
        last_name_input.send_keys(new_last_name)
        time.sleep(5)

        other_ID_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/input[1]")))
        other_ID_input.send_keys(other_id)
        time.sleep(5)
        gender_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       "//label[normalize-space()='Female']")))
        ActionChains(self.driver).move_to_element(gender_button).click().perform()
        time.sleep(5)
        # Click on Save button
        save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']")))
        ActionChains(self.driver).move_to_element(save_button).click().perform()
        time.sleep(5)
        return f"{first_name} {new_last_name} {other_id}"

    def delete_employee(self, first_name, new_last_name):
        # Navigate to PIM module
        pim_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='PIM']")))
        ActionChains(self.driver).move_to_element(pim_menu).click().perform()

        # Search for the employee using employee ID
        search_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                 "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")))
        search_input.send_keys(first_name + " " + new_last_name)
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
        ActionChains(self.driver).move_to_element(search_button).click().perform()
        time.sleep(5)
        # Click on employee to delete
        delete_icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']")))
        ActionChains(self.driver).move_to_element(delete_icon).click().perform()
        time.sleep(5)
        # Click on Delete button
        delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']")))
        ActionChains(self.driver).move_to_element(delete_button).click().perform()
        time.sleep(5)
        return "Successfully Deleted"