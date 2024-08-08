from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager


# поле ввода Chrome

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)

search_locator = "[type='number']"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("1000")
sleep(3)

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.clear()
sleep(3)

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("999")
sleep(3)

driver.quit()

# поле ввода Firefox

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)

search_locator = "[type='number']"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("1000")
sleep(3)

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.clear()
sleep(3)

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("999")
sleep(3)

driver.quit()

print("Test - Completed")
