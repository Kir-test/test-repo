from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver) -> None:
        """Инициализирует страницу корзины.

        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def get_items(self) -> list[str]:
        """Возвращает список товаров в корзине.

        Returns:
            Список названий товаров.
        """
        items = self.driver.find_elements(
            By.CLASS_NAME,
            "cart_item"
        )
        return [
            item.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text
            for item in items
        ]

    def checkout(self) -> None:
        """Переходит к оформлению заказа."""
        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()
