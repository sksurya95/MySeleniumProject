from selenium.webdriver.common.by import By


class Machines:
    def __init__(self, driver):
        self.driver = driver

    Machines = (By.XPATH, "//p[text()='My machines']")
    Machine_list = (By.XPATH,"//button[text()='Machines list']")
    PIN17 = (By.XPATH, "//input[@placeholder='PIN 17']")
    Add= (By.XPATH, "//span[text()='Add']")
    Close = (By.XPATH,"//button[text()='Close']")


    def click_machines(self):
        return self.driver.find_element(*Machines.Machines)

    def verify_Machinelist(self):
        return self.driver.find_element(*Machines.Machine_list)

    def type_pin17(self):
        return self.driver.find_element(*Machines.PIN17)

    def click_add(self):
        return self.driver.find_element(*Machines.Add)

    def verify_close(self):
        return self.driver.find_element(*Machines.Close)



