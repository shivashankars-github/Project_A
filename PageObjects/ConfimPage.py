from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    confirm_btn =  (By.XPATH, "//button[@class='btn btn-success']")
    contry_details = (By.ID, "country")
    terms_chckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn =  (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CSS_SELECTOR, ".alert-success")


    def getConfirmBtn(self):
        return self.driver.find_element(*ConfirmPage.confirm_btn)

    def EnterContryName(self):
        return self.driver.find_element(*ConfirmPage.contry_details)

    def getTermsCheckBox(self):
        return self.driver.find_element(*ConfirmPage.terms_chckbox)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def getSuccesMsg(self):
        return self.driver.find_element(*ConfirmPage.message)