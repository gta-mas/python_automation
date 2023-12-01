from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    svk = (By.LINK_TEXT, "Slovakia")
    checkbox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    submit_order = (By.CSS_SELECTOR, "[type='submit']")


    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)
#       driver.find_element(By.ID, "country")

    def confirmCountry(self):
        return self.driver.find_element(*ConfirmPage.svk)
#       driver.find_element(By.LINK_TEXT, "Slovakia")

    def confirmCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
#       driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submit_order)
#   driver.find_element(By.CSS_SELECTOR, "[type='submit']")


