from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    Cookie = (By.XPATH, "//button[text()='Accept All Cookies']")
    Register_button = (By.XPATH,"//span[text()='Register']")

    def click_acceptcookies(self):
        return self.driver.find_element(*Homepage.Cookie)

    def click_register(self):
        return self.driver.find_element(*Homepage.Register_button)
