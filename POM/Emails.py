from selenium.webdriver.common.by import By

class Emails:

    def __init__(self, driver):
        self.driver = driver
    #Set Password emails
    Sandbox = (By.XPATH, "//span[text()='Sandbox: Welcome to Volvo Connect']")
    password_button = (By.XPATH, "//span[text()='Set password ']")
    change_password = (By.XPATH,"//h2[text()='Change Your Password']")
    new_password=(By.XPATH,"//input[@id='newpassword']")
    confirm_password=(By.XPATH,"//input[@id='confirmpassword']")
    change=(By.XPATH,"//button[@id='password-button']")

    def click_sandbox(self):
        return self.driver.find_element(*Emails.Sandbox)

    def click_password(self):
        return self.driver.find_element(*Emails.password_button)

    def verify_changepassword(self):
        return self.driver.find_element(*Emails.change_password)

    def type_newpassword(self):
        return self.driver.find_element(*Emails.new_password)

    def type_confirmpassword(self):
        return self.driver.find_element(*Emails.confirm_password)

    def click_changepassword(self):
        return self.driver.find_element(*Emails.change)

    