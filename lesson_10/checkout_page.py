from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver) -> None:
        """Инициализирует страницу оформления заказа.

        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """Заполняет форму оформления заказа.

        Args:
            first_name: Имя покупателя.
            last_name: Фамилия покупателя.
            postal_code: Почтовый индекс.
        """
        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys(postal_code)

        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.

        Returns:
            Текст с итоговой суммой заказа.
        """
        return self.driver.find_element(
            By.CLASS_NAME,
            "summary_total_label"
        ).text
