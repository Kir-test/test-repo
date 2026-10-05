import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка сложения двух чисел с использованием калькулятора."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator.set_delay(45)

        with allure.step("Ввести выражение 7 + 8"):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")

        with allure.step("Получить результат вычисления"):
            result = calculator.get_result()

        with allure.step("Проверить, что результат равен 15"):
            assert result == "15"
    finally:
        driver.quit()
