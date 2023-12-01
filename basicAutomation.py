from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# CHROME can not be invoked directly, only via the driver as an intermediary
service_obj = Service("D:/Software Tester/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# FIREFOX
# service_obj = Service("D:/Software Tester/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# EDGE
# service_obj = Service("D:/Software Tester/msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()

driver.get("https://www.upjs.sk")

print(driver.title)
print(driver.current_url)

driver.get("https://www.upjs.sk/historia-univerzity/historia/")

print(driver.title)
print(driver.current_url)

driver.minimize_window()
driver.back()
driver.refresh()
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.close()