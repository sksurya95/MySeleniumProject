from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.Homepage import Homepage
from POM.Machine import Machines


def homepage_ecm(driver):
    homepage = Homepage(driver)
    machine = Machines (driver)
    driver.refresh()
    text=homepage.verify_explore().text
    assert "Explore" in text
    print(text)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located(machine.Machines))
    print(machine.click_machines().text)

