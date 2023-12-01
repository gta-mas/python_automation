import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestHomePage:

    def test_form_submission(self):

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

        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message