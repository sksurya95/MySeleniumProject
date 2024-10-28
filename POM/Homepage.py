from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    Cookie = (By.XPATH, "//button[text()='Accept All Cookies']")
    Register_button = (By.XPATH,"//span[text()='Register']")
    Explore=(By.XPATH,"//button[text()='Explore']")
    Consent = (By.XPATH,"//span[text()='Consent is required for viewing telematics data.']")
    # Machines = (By.XPATH, "//p[text()='My machines']")


    def click_acceptcookies(self):
        return self.driver.find_element(*Homepage.Cookie)

    def click_register(self):
        return self.driver.find_element(*Homepage.Register_button)

    def verify_explore(self):
        return self.driver.find_element(*Homepage.Explore)

    def verify_consent(self):
        return self.driver.find_element(*Homepage.Consent)

    # def click_machines(self):
    #     return self.driver.find_element(*Homepage.Machines)