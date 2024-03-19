import pytest
from selenium import webdriver
from OrangeHRM.pageObjects.pim_page import PIMPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def pim_page(driver):
    return PIMPage(driver)

@pytest.fixture(scope="module")
def login(pim_page):
    pim_page.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    WebDriverWait(pim_page.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys("Admin")
    pim_page.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    pim_page.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

def test_add_new_employee(pim_page, login):
    result = pim_page.add_new_employee("John", "Doe")
    assert result == "John Doe"

def test_edit_employee(pim_page, login):
    result = pim_page.edit_employee("John", "Doe","Walter","0001")
    assert result == "John Walter 0001"

def test_delete_employee(pim_page, login):
    result = pim_page.delete_employee("John","Walter")
    assert "Successfully Deleted" in result
