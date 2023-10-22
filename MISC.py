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
#chrome_options.add_experimental_option("detach", True)
chrome_options = webdriver.ChromeOptions()
#execute chrome in headless mode
chrome_options.add_argument("headless")
#ignoring certificate errors
chrome_options.add_argument("--ignore-certificate-errors")


service_obj = Service("D:/Software Tester/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#using Selenium to execute JavScript to scroll
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#screenshot: driver.get_screenshot_as_file("screen.png")


time.sleep(2)
