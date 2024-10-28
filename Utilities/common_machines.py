import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.Config import COUNTRY_VARIABLES
from POM.Machine import Machines


def MyMachinePIN17(driver, country_variables):
    machine= Machines (driver)
    machine.click_machines().click()
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located(machine.Machine_list))
    text=machine.verify_Machinelist().text
    assert "Machines list" in text
    pin17_value = country_variables.get("pin17")
    print(pin17_value)
    driver.refresh()
    time.sleep(2)
    machine.type_pin17().send_keys(pin17_value)
    machine.click_add().click()
    # def Machinepopup (driver):
        
