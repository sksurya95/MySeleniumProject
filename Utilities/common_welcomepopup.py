import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.Config import COUNTRY_VARIABLES


from POM.Homepage import Homepage
from POM.self_registration import Self_registration
from selenium.webdriver.common.action_chains import ActionChains

from POM.welcomepopup import wcpopup


def handling_popup(driver):

    popup = wcpopup(driver)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(popup.wc_to_vc))
    popup.click_closebutton().click()