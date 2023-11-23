from selenium.webdriver.common.by import By


class HomePage:
    #constructor accepts argument to form a connection with this local driver
    #setting up test case driver to local driver
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
#       self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
