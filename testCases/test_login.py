import pytest
from selenium import webdriver
from OrangeHRM_V1.pageObjects.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(setup):
    username = "Admin"
    password = "admin123"
    login_page = LoginPage(setup)
    login_page.login(username, password)

    WebDriverWait(setup, 10).until(EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"))
    assert "dashboard" in setup.current_url

def test_invalid_login(setup):
    username = "Admin"
    password = "Invalid password"
    login_page = LoginPage(setup)
    login_page.login(username, password)

    error_message = WebDriverWait(setup, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))).text
    assert "Invalid credentials" in error_message
