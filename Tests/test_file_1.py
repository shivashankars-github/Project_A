from A_Project_1one.PageObjects.HomePage import HomePage
from A_Project_1one.Utilities.BaseClass import BaseClass


class TestCaseOne(BaseClass):


    def test_end2end(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("Getting all Product names")
        product_names = checkoutpage.getProductNames()

        i = -1
        for name in product_names:
            i = i + 1
            if name.text == "Blackberry":
                log.info(name.text + "is selected")
                checkoutpage.getPoductFooter()[i].click()

        confirmpage = checkoutpage.getCheckOutBtn()
        confirmpage.getConfirmBtn().click()
        confirmpage.EnterContryName().send_keys("ind")

        self.verifyLinkPrecense("India")
        self.driver.find_element_by_link_text("India").click()


        confirmpage.getTermsCheckBox().click()
        confirmpage.getPurchaseBtn().click()
        successText = confirmpage.getSuccesMsg().text

        assert "Success! Thank you!" in successText




