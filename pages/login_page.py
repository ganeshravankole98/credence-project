from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email_field)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()