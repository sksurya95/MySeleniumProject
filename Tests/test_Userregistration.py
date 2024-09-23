import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.Emails import Emails
from POM.Homepage import Homepage
from POM.self_registration import Self_registration
from POM.welcomepopup import wcpopup
from Utilities.BaseClass import Customer_portal
from Utilities.common_emails import outlook_signin, set_password
from Utilities.common_homepage import homepage_ecm
from Utilities.common_registration import self_registration, sru_validations, sru_form_validations, \
    getemail_from_config, random_numbers, company, random_email
from Utilities.common_welcomepopup import handling_popup


# @pytest.mark.usefixtures("cp")
class TestUserReg(Customer_portal):

    def test_registration(self):
        homepage = Homepage(self.driver)
        register = Self_registration(self.driver)
        time.sleep(2)
        country_variables = self.country_variables
        print(f"Country Variables: {country_variables}")
        homepage.click_acceptcookies().click()
        homepage.click_register().click()
        time.sleep(3)
        xpath_country = f"//span[text()='{country_variables['country_name']}']"
        print(f"XPath Country: {xpath_country}")
        self.Formatted_email = getemail_from_config(country_variables, "+", random_numbers)
        self_registration(self.driver, "CRT", "SRU", self.Formatted_email, xpath_country)

    def test_setpassword(self,credentials):
        self.outlook_signin_helper()
        set_password(self.driver, credentials)

    def test_welcomepopup(self):
        handling_popup(self.driver)

    def test_companyregistration(self):
        company(self.driver, "CRT", "CRT01" , "test@test.com","123" , "CRTCity",  "CRT Street" )

    # def test_random_email_generation(self):
    #     random_email()

    def test_ECMHomepage(self):
        homepage = Homepage(self.driver)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(homepage.Explore))
        homepage_ecm(self.driver)


