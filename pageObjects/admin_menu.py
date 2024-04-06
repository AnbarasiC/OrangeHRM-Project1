from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def validate_title(self):
        return self.driver.title

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))).send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    def validate_admin_menu_items(self):
        menu_items = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']
        menu_item_elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='oxd-sidepanel-body']//ul/li")))
        menu_item_texts = [element.text for element in menu_item_elements]
        print("Menu Items Texts:")
        for menu_item_text in menu_item_texts:
            print(menu_item_text)
        return menu_item_texts