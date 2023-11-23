import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.fixture(scope="class")
#def setup():
 #   print("First execution")
  #  yield
   # print("Last execution")


@pytest.fixture()
def load_data():
    print("User data being created")
    return ["Joe", "Doe", "website.com"]


@pytest.fixture(params=[("Chrome", "Joe", "Doe", "website"), ("Firefox", "Joe", "website"), ("Joe", "Doe", "IE")])
def cross_browser(request):
    return request.param


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-exit-after-done")
    chrome_options.add_argument("--start-maximized")

    service_obj = Service("D:/Software Tester/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()



