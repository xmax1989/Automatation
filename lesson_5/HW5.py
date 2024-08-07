
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# кликнуть пять раз по кнопке Add Element Chrome

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(2)

search_locator = "[onclick='addElement()']"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

for x in range(0, 5):
    search_input.click()

sleep(2)

Len_Delete = driver.find_elements(By.CSS_SELECTOR, "[onclick='deleteElement()']")

print("Длина списка в Chrome =", len(Len_Delete))

driver.quit()

# кликнуть пять раз по кнопке Add Element Firefox

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(2)

search_locator = "[onclick='addElement()']"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

for x in range(0, 5):
    search_input.click()

sleep(2)

Len_Delete = driver.find_elements(By.CSS_SELECTOR, "[onclick='deleteElement()']")

print("Длина списка в Firefox =", len(Len_Delete))

driver.quit()


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

print("Tests - Completed")