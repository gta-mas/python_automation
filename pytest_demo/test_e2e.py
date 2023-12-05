from selenium import webdriver
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pytest_demo.base_class import BaseClass
from pytest_demo.checkout_page import CheckoutPage
from pytest_demo.confirm_page import ConfirmPage
from pytest_demo.home_page import HomePage


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()

        # //a[contains(@href,'shop')] - XPATH   a[href*='shop'] - CSS
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()

        log.info("Card Titles")

        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # checkout_page = CheckoutPage(self.driver) - cleaned up
        products = checkout_page.getCardTitle()
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            log.info(product_name)
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkout_button = CheckoutPage(self.driver)
        checkout_button.gotoCheckout().click()

        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        checkout_success = CheckoutPage(self.driver)
        confirm_page = checkout_success.checkoutSuccess()

        log.info("Typing Country Name")

        # self.driver.find_element(By.ID, "country").send_keys("slov")
        get_country = ConfirmPage(self.driver)
        get_country.getCountry().send_keys("slov")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Slovakia")))
        self.verify_link_presence("Slovakia")

        # self.driver.find_element(By.LINK_TEXT, "Slovakia").click()
        country = ConfirmPage(self.driver)
        country.confirmCountry().click()

        # self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
        checkbox = ConfirmPage(self.driver)
        checkbox.confirmCheckbox().click()

        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        submit_order = ConfirmPage(self.driver)
        submit_order.submit().click()

        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        log.info("Assertion successful: " + success_text)

        assert "Success! Thank you!" in success_text

