from selenium.webdriver.common.by import By

from A_Project_1one.PageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.XPATH, "//div/input[@name ='name']")
    email = (By.XPATH, "//div/input[@name ='email']")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR,"input[type='submit']")
    sucessmsg = (By.CSS_SELECTOR,"[class*='alert-success']")




    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessmsg(self):
        return self.driver.find_element(*HomePage.sucessmsg)