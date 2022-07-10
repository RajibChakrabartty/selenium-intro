import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setting Up Browsers
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.yatra.com/")
# Maximizing Windows
driver.maximize_window()

# Accepting Cookies
driver.find_element(By.XPATH, "//button[contains(text(),'Ok,I Agree')]").click()

# Locating *From City
depart_from = driver.find_element(By.CSS_SELECTOR, "#BE_flight_origin_city")
driver.implicitly_wait(5)
depart_from.click()
time.sleep(2)
depart_from.send_keys("Australia")
time.sleep(2)

# Clicking on Current City from City List
form_airports = driver.find_elements(By.XPATH, '//p[@class = "ac_cityname"]')
for airport in form_airports:
    print(airport.text)
    if airport.text == "Adelaide (ADL)":
        airport.click()
        time.sleep(3)
        break
    else:
        continue
print("Clicked on Adelaide!")

# Locating *To City
depart_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
depart_to.send_keys("India")
time.sleep(2)

# Clicking on Arrival City from List
arrival_airports = driver.find_elements(By.XPATH, '//p[@class = "ac_cityname"]')
for airport in arrival_airports:
    print(airport.text)
    if airport.text == "Chennai (MAA)":
        airport.click()
        time.sleep(3)
        break
    else:
        continue
print("Clicked on Chennai")

# Clicking on Departure Date
departure_date = driver.find_element(By.CSS_SELECTOR, "#BE_flight_origin_date")
departure_date.click()
time.sleep(2)

# Selecting Departure Date
all_dates = driver.find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class!='inActiveTD']")
for date in all_dates:
    if date.get_attribute("data-date") == "08/02/2023":
        date.click()
        time.sleep(2)
        break

# Selecting Non Stop Flight
non_stop = driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']")
non_stop.click()
time.sleep(2)
print("Non Stop Flight Selected")

# Checking 1 traveller is selected/ not
traveller_info = driver.find_element(By.XPATH, "//span[(text() ='Traveller')]")
traveller_info.click()
time.sleep(2)

# Increasing Travellers
add_traveller = driver.find_element(By.XPATH, "(//span[@class='ddSpinnerPlus'])[1]")
add_traveller.click()
time.sleep(2)


