from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager


# клик по кнопке без ID Chrome

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for x in range(3):

    driver.get("http://uitestingplayground.com/dynamicid")

    sleep(2)

    search_locator = "[class='btn btn-primary']"

    search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

    search_input.click()

    sleep(2)

driver.quit()

# клик по кнопке без ID Firefox

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))

for x in range(3):

    driver.get("http://uitestingplayground.com/dynamicid")

    sleep(2)

    search_locator = "[class='btn btn-primary']"

    search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

    search_input.click()

    sleep(2)

driver.quit()

print("Test - Completed")
