import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# создаем переменные вводных данных
First_name = "Иван"
Last_name = "Петров"
Address = "Ленина, 55-3"
Email = "test@skypro.com"
Phone_number = "+7985899998787"
City = "Москва"
Country = "Россия"
Job_position = "QA"
Company = "SkyPro"
# добавляем переменные локаторов
Locator_First_name = "[name='first-name']"
Locator_Last_name = "[name='last-name']"
Locator_Address = "[name='address']"
Locator_Email = "[name='e-mail']"
Locator_Phone = "[name='phone']"
Locator_City = "[name='city']"
Locator_Country = "[name='country']"
Locator_Job_pos = "[name='job-position']"
Locator_Company = "[name='company']"
Locator_Submit = "[class='btn btn-outline-primary mt-3']"

@pytest.mark.test_positive
def test_auth_phorm():    
    # заходим на сайт
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
     # заполняем форму
    driver.find_element(By.CSS_SELECTOR, Locator_First_name).send_keys(First_name)
    driver.find_element(By.CSS_SELECTOR, Locator_Last_name).send_keys(Last_name)
    driver.find_element(By.CSS_SELECTOR, Locator_Address).send_keys(Address)
    driver.find_element(By.CSS_SELECTOR, Locator_Email).send_keys(Email)
    driver.find_element(By.CSS_SELECTOR, Locator_Phone).send_keys(Phone_number)
    driver.find_element(By.CSS_SELECTOR, Locator_City).send_keys(City)
    driver.find_element(By.CSS_SELECTOR, Locator_Country).send_keys(Country)
    driver.find_element(By.CSS_SELECTOR, Locator_Job_pos).send_keys(Job_position)
    driver.find_element(By.CSS_SELECTOR, Locator_Company).send_keys(Company)
    driver.find_element(By.CSS_SELECTOR, Locator_Submit).click()
    sleep(4)
    # проверяем цвет полей  
    color_Zip = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property('background-color')
    assert color_Zip == "rgba(248, 215, 218, 1)"
    color_Adress = driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property('background-color')
    assert color_Adress == "rgba(209, 231, 221, 1)"
    color_Email = driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property('background-color')
    assert color_Email == "rgba(209, 231, 221, 1)"
    color_Phone = driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property('background-color')
    assert color_Phone == "rgba(209, 231, 221, 1)"
    color_City = driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property('background-color')
    assert color_City == "rgba(209, 231, 221, 1)"
    color_Country = driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property('background-color')
    assert color_Country == "rgba(209, 231, 221, 1)"
    color_Jobpos = driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property('background-color')
    assert color_Jobpos == "rgba(209, 231, 221, 1)"
    color_Company = driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property('background-color')
    assert color_Company == "rgba(209, 231, 221, 1)"
    sleep(2)

    driver.quit()
