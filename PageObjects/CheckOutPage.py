from selenium.webdriver.common.by import By

from A_Project_1one.PageObjects.ConfimPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    product_names = (By.XPATH, "//div/h4/a")
    product_footer = (By.CSS_SELECTOR, ".card-footer")
    checkoutbtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getProductNames(self):
        return self.driver.find_elements(*CheckOutPage.product_names)

    def getPoductFooter(self):
        return  self.driver.find_elements(*CheckOutPage.product_footer)

    def getCheckOutBtn(self):
        checkout_btn = self.driver.find_element(*CheckOutPage.checkoutbtn)
        self.driver.execute_script("arguments[0].click();", checkout_btn)
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
