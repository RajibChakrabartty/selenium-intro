import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Maximize Chrome Browser
driver.maximize_window()

# Hitting on Base URL
url = "https://www.yatra.com/"
driver.get(url)
driver.implicitly_wait(10)
print(driver.current_url)

# Selecting From City
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").click()
time.sleep(3)
from_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
time.sleep(3)
from_city.send_keys("Australia")

search_city = driver.find_elements(By.XPATH, "//div[@class='viewport']/div/div/li")

for city in search_city:
    if "Sydney (SYD)" in search_city.text:
        city.click()
        break

# Closing Browser
driver.close
