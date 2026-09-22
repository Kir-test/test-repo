from selenium import webdriver
from lesson_06.cookies_data import (
    USER1_SESSION,
    USER1_TOKEN,
    USER2_SESSION,
    USER2_TOKEN,
)


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru")

    driver.add_cookie({
        "name": "session",
        "value": USER1_SESSION
    })

    driver.add_cookie({
        "name": "token",
        "value": USER1_TOKEN
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/kir_test1")

    url_1 = driver.current_url

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru")

    driver.add_cookie({
        "name": "session",
        "value": USER2_SESSION
    })

    driver.add_cookie({
        "name": "token",
        "value": USER2_TOKEN
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/kir_test2")

    url_2 = driver.current_url

    assert url_1 != url_2

    driver.quit()
