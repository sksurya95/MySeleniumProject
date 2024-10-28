import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.Config import COUNTRY_VARIABLES
from POM.salesforcepage import SF


def Salesforce_login(driver,country):
    driver.get("https://test.salesforce.com/")
    sfobject = SF(driver)
    sfobject.input_username().send_keys(country)
    sfobject.input_password().send_keys("Volvo@8220")
    sfobject.click_login().click()
