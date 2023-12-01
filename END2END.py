import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--disable-exit-after-done")
chrome_options.add_argument("--start-maximized")

service_obj = Service("D:/Software Testing/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(@href,'shop')] - XPATH   a[href*='shop'] - CSS
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("slov")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Slovakia")))
driver.find_element(By.LINK_TEXT, "Slovakia").click()
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
success_text = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success_text
