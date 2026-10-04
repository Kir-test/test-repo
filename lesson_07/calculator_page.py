from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, value):
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        )
        button.click()

    def get_result(self, timeout=60):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), "15"
            )
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
