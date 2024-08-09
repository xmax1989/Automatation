from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager


# форма авторизации Chrome

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

search_locator = "[type='text']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("tomsmith")
sleep(2)

search_locator = "[type='password']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("SuperSecretPassword!")
sleep(2)

search_locator = "[type='submit']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.click()
sleep(3)

driver.quit()

# форма авторизации Firefox

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

search_locator = "[type='text']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("tomsmith")
sleep(2)

search_locator = "[type='password']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("SuperSecretPassword!")
sleep(2)

search_locator = "[type='submit']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.click()
sleep(3)

driver.quit()

print("Test - Completed")
