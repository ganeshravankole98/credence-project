import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    yield driver
    driver.quit()