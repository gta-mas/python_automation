from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_success = (By.XPATH, "//button[@class='btn btn-success']")


    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.products)
#       driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def gotoCheckout(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)
#       driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

    def checkoutSuccess(self):
        return self.driver.find_element(*CheckoutPage.checkout_success)
#       driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()


