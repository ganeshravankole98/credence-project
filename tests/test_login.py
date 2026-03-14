from pages.login_page import LoginPage


def test_login(setup):
    driver = setup

    driver.get("https://automation.credence.in/login")

    login = LoginPage(driver)

    login.login("Credencetest@test.com", "Credence@123")