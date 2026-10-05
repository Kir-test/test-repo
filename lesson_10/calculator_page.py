from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver) -> None:
        """Инициализирует страницу калькулятора.

        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, delay: int) -> None:
        """Устанавливает задержку выполнения калькулятора.

        Args:
            delay: Время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, value: str) -> None:
        """Нажимает кнопку калькулятора.

        Args:
            value: Значение кнопки.
        """
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        )
        button.click()

    def get_result(self, timeout: int = 60) -> str:
        """Ожидает и возвращает результат вычисления.

        Args:
            timeout: Максимальное время ожидания результата в секундах.

        Returns:
            Текст результата вычисления.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), "15"
            )
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
