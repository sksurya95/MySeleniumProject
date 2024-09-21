from selenium.webdriver.common.by import By


class Emailbox:

    def __init__(self, driver):
        self.driver = driver

    Email = (By.XPATH, "//input[@name='loginfmt']")
    Submit = (By.XPATH , "//button[@type='submit']")
    Password = (By.XPATH , "//input[@name='passwd']")
    Signin = (By.XPATH , "//input[@type='submit']")
    Code = (By.XPATH , "//input[@name='otc']")
    Verify = (By.XPATH, "//input[@type='submit']")
    Yes = (By.XPATH, "//input[@type='submit']")

    def input_email_id(self):
        return self.driver.find_element(*Emailbox.Email)

    def click_next(self):
        return self.driver.find_element(*Emailbox.Submit)

    def input_password(self):
        return self.driver.find_element(*Emailbox.Password)

    def click_signin(self):
        return self.driver.find_element(*Emailbox.Signin)

    def input_otp(self):
        return self.driver.find_element(*Emailbox.Code)

    def input_verify(self):
        return self.driver.find_element(*Emailbox.Verify)

    def input_Yes(self):
        return self.driver.find_element(*Emailbox.Yes)