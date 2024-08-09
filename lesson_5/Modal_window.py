from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager


# модальное окно Chrome

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(2)

search_locator = "[class=modal-footer]"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

sleep(2)

search_input.click()

sleep(2)

driver.quit()

# модальное окно Firefox

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(2)

search_locator = "[class=modal-footer]"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

sleep(2)

search_input.click()

sleep(2)

driver.quit()

print("Test - Completed")
