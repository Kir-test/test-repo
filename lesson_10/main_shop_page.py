from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainShopPage:
    def __init__(self, driver) -> None:
        """Инициализирует главную страницу магазина.

        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def add_product(self, product_name: str) -> None:
        """Добавляет выбранный товар в корзину.

        Args:
            product_name: Название товара.
        """
        product_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    (
                        "//div[contains(@class, 'inventory_item')]"
                        f"[.//div[contains(@class, "
                        f"'inventory_item_name') and "
                        f"normalize-space()='{product_name}']]"
                        "//button"
                    ),
                )
            )
        )
        product_button.click()

    def open_cart(self) -> None:
        """Открывает корзину."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()
