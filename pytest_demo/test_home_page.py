import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pytest_demo.base_class import BaseClass
from pytest_demo.home_page import HomePage
from pytest_demo.test_data.home_page_data import HomePageData


class TestHomePage(BaseClass):

    def test_form_submission(self, getData):

        # service_obj = Service("D:/Software Testing/chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        # driver.maximize_window()

        # ID, Xpath, CSS Selector, Classname, name, linkText
        # CSS Selector formula: tagname[attribute="attribute"], #id, .classname
        # Xpath formula: //tagname[@attribute="attribute"]
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Tvoja mac")

        log = self.get_logger()

        home_page = HomePage(self.driver)

        log.info("Name is: " + getData["name"])

        home_page.getName().send_keys(getData["name"])

        # driver.find_element(By.NAME, "email").send_keys("abcd@gmail.com")
        home_page.getEmail().send_keys(getData["email"])

        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        home_page.getPassword().send_keys("123456")

        # driver.find_element(By.ID, "exampleCheck1").click()
        home_page.checkBox().click()

        # dropdown menu
        # dropdown = Select(home_page.getGender())
        # dropdown.select_by_visible_text("Male")
        # dropdown.select_by_index(0)
        # dropdown.select_by_value("value_name")
        self.selectByText(home_page.getGender(), getData["gender"])

        #driver.find_element(By.XPATH, "//input[@type='submit']").click()
        home_page.submitButton().click()

        message = home_page.getSuccess().text
        print(message)

        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def getData(self, request):
        return request.param
