import pytest

from A_Project_1one.PageObjects.HomePage import HomePage
from A_Project_1one.TestData.HomePageData import Homepagedata
from A_Project_1one.Utilities.BaseClass import BaseClass


class TestCaseTwo(BaseClass):


    def test_formsubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        log.info("Name entered :" + homepage.getName().get_attribute("value"))
        log.info("email entered :" + homepage.getemail().get_attribute("value"))

        self.getOptionByText(homepage.getGender(), getData["Gender"])


        homepage.getSubmitBtn().click()
        assert "Success" in homepage.getSuccessmsg().text

        self.driver.refresh()

    @pytest.fixture(params= Homepagedata.get_testdata())
    def getData(self, request):
        return request.param




