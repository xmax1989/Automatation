import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # вход на сайт и авторизация
@pytest.mark.test_positive
def test_pay_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # добавляем товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    #работа с корзиной
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    # заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Maxim")
    driver.find_element(By.ID, "last-name").send_keys("Boev")
    driver.find_element(By.ID, "postal-code").send_keys("173023")
    driver.find_element(By.ID, "continue").click()

    # находим и проверяем общую стоимость заказов
    res = driver.find_element(By.CSS_SELECTOR, "[class='summary_total_label']").text
    driver.close()
    price = res.strip('Total: $')
    assert price == "58.29"

    driver.quit()