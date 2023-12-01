import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("D:/Software Testing/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSS Selector, Classname, name, linkText
# CSS Selector formula: tagname[attribute="attribute"], #id, .classname
# Xpath formula: //tagname[@attribute="attribute"]
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Tvoja mac")
driver.find_element(By.NAME, "email").send_keys("abcd@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# dropdown menu
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
time.sleep(2)
dropdown.select_by_index(0)
# dropdown.select_by_value("value_name")
time.sleep(2)




driver.find_element(By.XPATH,"//input[@type='submit']").click()


message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Another string of text")
time.sleep(3)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()



driver.get("https://rahulshettyacademy.com/client/")

# linktext
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# locating an element by going from parent to child element
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@123456")

driver.find_element(By.ID, "confirmPassword").send_keys("Hello@123456")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# using XPATH for locating elements via text:
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(2)
driver.close()