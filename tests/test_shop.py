from pages.home_page import HomePage

def test_add_to_cart(setup):
    driver = setup

    home = HomePage(driver)

    home.add_first_product_to_cart()
    home.go_to_cart()


