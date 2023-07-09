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
chrome_options.add_experimental_option("detach", True)
service_obj = Service("D:/Software Tester/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# driver.find_element(By.LINK_TEXT, "Click Here").click()
# # retrieves names of all open windows in the form of list
# open_windows = driver.window_handles
#
# driver.switch_to.window(open_windows[1])
# print(driver.find_element(By.TAG_NAME, "h3").text)
# driver.close()
#
# driver.switch_to.window(open_windows[0])
# assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

# EXERCISE
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
open_windows = driver.window_handles

driver.switch_to.window(open_windows[1])
ptext = (driver.find_element(By.CSS_SELECTOR, ".im-para.red")).text
ex_wait = WebDriverWait(driver, 10)
ex_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".im-para.red")))
start_index = ptext.find('at') + 3
end_index = ptext.find('with') - 1
email_address = ptext[start_index:end_index]

driver.switch_to.window(open_windows[0])
driver.find_element(By.ID, "username").send_keys(email_address)
driver.find_element(By.ID, "password").send_keys("123456abcd")
driver.find_element(By.ID, "signInBtn").click()
time.sleep(2)
error_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text
print(error_message)
