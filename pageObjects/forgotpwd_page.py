from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotpwdPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_forgot_password(self):
        forgot_password_link = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")))
        forgot_password_link.click()

    def provide_username_and_reset_password(self, username):
        username_textbox = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        username_textbox.send_keys(username)
        reset_password_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Reset Password']")
        reset_password_button.click()

    def get_reset_password_success_message(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h6[normalize-space()='Reset Password link sent successfully']"))).text