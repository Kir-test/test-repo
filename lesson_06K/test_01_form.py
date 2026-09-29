from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        element = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, name)
            )
        )
        element.send_keys(value)

    submit = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Submit']")
        )
    )

    submit.click()

    wait.until(
        EC.url_contains("data-types-submitted.html")
    )

    zip_code = wait.until(
        EC.presence_of_element_located(
            (By.ID, "zip-code")
        )
    )

    assert "alert-danger" in zip_code.get_attribute("class")

    valid_fields = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company",
    ]

    for field in valid_fields:
        element = wait.until(
            EC.presence_of_element_located(
                (By.ID, field)
            )
        )

        assert "alert-success" in element.get_attribute("class")

    driver.quit()
