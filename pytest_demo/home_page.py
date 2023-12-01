from selenium.webdriver.common.by import By

from pytest_demo.checkout_page import CheckoutPage


class HomePage:
    #constructor accepts argument to form a connection with this local driver
    #setting up test case driver to local driver
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
#       self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page


