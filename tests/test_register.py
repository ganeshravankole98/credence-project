#test_register

import time

from conftest import setup
from pages.register_user import register_user

def test_register(setup):
    driver = setup

    driver.get("https://automation.credence.in/shop")
    register = register_user(driver)
    register.go_to_register_page()