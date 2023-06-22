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
name = "GT"
driver.find_element(By.NAME, "enter-name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(2)
# alert.dismiss()
assert name in alert_text
alert.accept()

time.sleep(2)
driver.close()