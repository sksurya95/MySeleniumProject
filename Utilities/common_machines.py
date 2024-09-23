from POM.Homepage import Homepage


def MyMachine(driver):
    homepage=Homepage(driver)
    homepage.click_machines().click()

