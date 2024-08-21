import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# добавляем переменные локаторов
Locator_time = "#delay"
Locator = "//span[text() = '7']" # для смены локатора заменить цифру или символ(0,1,-,=,+...)

@pytest.mark.test_positive
def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)
    driver.find_element(By.XPATH, "//span[text() = '7']").click()
    driver.find_element(By.XPATH, "//span[text() = '+']").click()
    driver.find_element(By.XPATH, "//span[text() = '8']").click()
    driver.find_element(By.XPATH, "//span[text() = '=']").click()
    sleep(45)

    res = driver.find_element(By.CSS_SELECTOR, "[class='screen']").text
    assert res == "15"

    driver.quit()