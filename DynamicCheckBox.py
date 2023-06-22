import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("D:/Software Tester/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

time.sleep(2)

# RADIO buttons
radios = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
print(len(radios))

radios[2].click()
assert radios[2].is_selected()


# for radio in radios:
#     if radio.get_attribute("value") == "radio2":
#         radio.click()
#         assert radio.is_selected()
#         break
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(2)
driver.close()

