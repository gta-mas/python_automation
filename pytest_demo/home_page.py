from selenium.webdriver.common.by import By

from pytest_demo.checkout_page import CheckoutPage


class HomePage:
    # constructor accepts argument to form a connection with this local driver
    # setting up test case driver to local driver
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
#       self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def getName(self):
        return self.driver.find_element(*HomePage.name)
#       driver.find_element(By.CSS_SELECTOR, "input[name='name']")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
#       driver.find_element(By.NAME, "email")

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
#       driver.find_element(By.ID, "exampleInputPassword1")

    def checkBox(self):
        return self.driver.find_element(*HomePage.checkbox)
#       driver.find_element(By.ID, "exampleCheck1")

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
#       driver.find_element(By.ID, "exampleFormControlSelect1"))

    def submitButton(self):
        return self.driver.find_element(*HomePage.submit)
#       driver.find_element(By.XPATH, "//input[@type='submit']")

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success_message)
#       driver.find_element(By.CLASS_NAME, "alert-success")

