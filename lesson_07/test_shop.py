from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from login_page import LoginPage
from main_shop_page import MainShopPage


def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        shop_page = MainShopPage(driver)
        shop_page.add_product("Sauce Labs Backpack")
        shop_page.add_product("Sauce Labs Bolt T-Shirt")
        shop_page.add_product("Sauce Labs Onesie")
        shop_page.open_cart()

        cart_page = CartPage(driver)

        items = cart_page.get_items()

        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        cart_page.checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form(
            "Кирилл",
            "Тестер",
            "43043",
        )

        total = checkout_page.get_total()

    finally:
        driver.quit()

    assert items == expected_items
    assert total == "Total: $58.29"
