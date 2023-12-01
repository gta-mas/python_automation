import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_list = []

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("D:/Software Tester/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
# waits 5 sec for web elements to display, acts as global wait


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

# implicit wait does not work with find_elements command sice it returns a list no matter if empty or containing values
result_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
list_count = len(result_list)
assert list_count > 0

# CHAINING instead of searching the entire body, this command searches only within the previous "product" element
for result in result_list:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expected_list == actual_list
print(actual_list)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# SUM validation, finding the amount elements via parent to child method
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
total_amount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == total_amount


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
explicit_wait = WebDriverWait(driver, 10)
# overrides implicit wait and waits for up to x seconds until the element is visible, present etc...
explicit_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

discount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
print(discount)
assert total_amount > discount

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)



