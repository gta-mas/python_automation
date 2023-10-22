import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#chrome_options = Options()
#chrome_options.add_argument("--disable-exit-after-done")
veggie_list = []
service_obj = Service("D:/Software Tester/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

#click on column header
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all vegetable names into veggie_list
veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggie_web_elements:
    veggie_list.append(element.text)

original_veggie_list = veggie_list.copy()

#sort this list = new_sorted_list
veggie_list.sort()

#veggie_list == new_sorted_list
assert veggie_list == original_veggie_list
time.sleep(2)


