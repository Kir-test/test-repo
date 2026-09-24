from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )
    username.send_keys("standard_user")

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    )
    password.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    )
    login_button.click()

    backpack = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    backpack.click()

    bolt_tshirt = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        )
    )
    bolt_tshirt.click()

    onesie = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-onesie")
        )
    )
    onesie.click()

    cart = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    )
    cart.click()

    checkout = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    )
    checkout.click()

    first_name = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )
    first_name.send_keys("Кирилл")

    last_name = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "last-name")
        )
    )
    last_name.send_keys("Тестеров")

    postal_code = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "postal-code")
        )
    )
    postal_code.send_keys("430043")

    continue_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "continue")
        )
    )
    continue_button.click()

    total = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )

    assert total.text == "Total: $58.29"

    driver.quit()
