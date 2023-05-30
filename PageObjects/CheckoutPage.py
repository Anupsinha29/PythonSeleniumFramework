from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    #driver.find_element(By.XPATH,"//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)
    def getcheckoutitems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage =ConfirmPage(self.driver)
        return confirmPage

