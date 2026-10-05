import allure
from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from login_page import LoginPage
from main_shop_page import MainShopPage


@allure.title("Проверка оформления заказа")
@allure.description(
    "Проверка добавления товаров в корзину и оформления заказа."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу авторизации"):
            login_page.open()

        with allure.step("Выполнить авторизацию"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        shop_page = MainShopPage(driver)

        with allure.step("Добавить товары в корзину"):
            shop_page.add_product("Sauce Labs Backpack")
            shop_page.add_product("Sauce Labs Bolt T-Shirt")
            shop_page.add_product("Sauce Labs Onesie")

        with allure.step("Открыть корзину"):
            shop_page.open_cart()

        cart_page = CartPage(driver)

        with allure.step("Получить список товаров в корзине"):
            items = cart_page.get_items()

        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        with allure.step("Проверить состав корзины"):
            assert items == expected_items

        with allure.step("Перейти к оформлению заказа"):
            cart_page.checkout()

        checkout_page = CheckoutPage(driver)

        with allure.step("Заполнить данные для оформления заказа"):
            checkout_page.fill_form(
                "Кирилл",
                "Тестер",
                "43043",
            )

        with allure.step("Получить итоговую сумму заказа"):
            total = checkout_page.get_total()

        with allure.step("Проверить итоговую сумму"):
            assert total == "Total: $58.29"

    finally:
        driver.quit()
