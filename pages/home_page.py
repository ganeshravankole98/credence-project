from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_products(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".thumbnail"))
        )

    def add_first_product_to_cart(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn"))
        )
        buttons[0].click()


    def go_to_cart(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cart')]").click()

