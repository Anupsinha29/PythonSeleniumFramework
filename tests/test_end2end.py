import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    def test_end2end(self):

        homepage = HomePage(self.driver)
        checkoutPage = homepage.shopItems()

        #checkoutpage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()

        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        i = -1
        for card in cards:
            i = i +1
            cardtext = card.text
            print(cardtext)
            if cardtext == "Blackberry":
                checkoutPage.getCardFooter()[i].click()
                #card.find_element(By.XPATH, "div/button").click()

        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        confirmPage = CheckoutPage.getcheckoutitems()

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText










