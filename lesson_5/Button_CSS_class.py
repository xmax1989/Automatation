from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager


# клик по кнопе с CSS-классом Chrome

for x in range(3):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("http://uitestingplayground.com/classattr")

    sleep(1)

    search_locator = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"

    search_input = driver.find_element(By.XPATH, search_locator)

    search_input.click()

    sleep(1)

    driver.quit()

# клик по кнопе с CSS-классом Firefox

for x in range(3):

    driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))

    driver.get("http://uitestingplayground.com/classattr")

    sleep(1)

    search_locator = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"

    search_input = driver.find_element(By.XPATH, search_locator)

    search_input.click()

    sleep(1)

    driver.quit()

    print("Test - Completed")
