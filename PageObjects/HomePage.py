from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")

    def shopItems(self):
       return self.driver.find_element(*HomePage.shop).click()
       checkoutPage = CheckoutPage(self.driver)
       return  checkoutPage

        #driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
