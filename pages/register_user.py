#register_user

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class register_user:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_register_page(self):
         self.wait.until(
         EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        ).click()


    def name(self,name):
        self.wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys("Ganesh")

    def email(self,email):
        self.wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("cred@test.com")

    def password(self,password):
        self.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Credence@123")

    def password_confirm(self,password):
        self.wait.until(EC.element_to_be_clickable((By.ID, "password_confirm"))).send_keys(password)


    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, "btn.btn.submit").click()