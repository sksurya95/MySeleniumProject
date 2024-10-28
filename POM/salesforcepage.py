from selenium.webdriver.common.by import By

class SF:

    def __init__(self,driver):
        self.driver=  driver

    username= (By.XPATH, "//input[@type='email']")
    password= (By.XPATH, "//input[@id='password']")
    Login = (By.XPATH, "//input[@id='Login']")
    Home = (By.XPATH, "//span[text()='Ho(me']")
    Setup = (By.XPATH, "(//span[@part='boundary'])[5]")
    Console= (By.XPATH, "//span[text()='Developer Console']")
    Query_editor= (By.XPATH, "//span[text()='Query Editor']")
    Query_input= (By.XPATH, "//td[@role='presentation']//textarea")
    Execute= (By.XPATH,"//span[text()='Execute']")

    def input_username(self):
        return self.driver.find_element(*SF.username)

    def input_password(self):
        return self.driver.find_element(*SF.password)

    def click_login(self):
        return self.driver.find_element(*SF.Login)

    def verify_home(self):
        return self.driver.find_element(*SF.Home)

    def click_setup(self):
        return self.driver.find_element(*SF.Setup)

    def click_console(self):
        return self.driver.find_element(*SF.Console)

    def click_queryeditor(self):
        return self.driver.find_element(*SF.Query_editor)

    def type_queryinput(self):
        return self.driver.find_element(*SF.Query_input)

    def click_execute(self):
        return self.driver.find_element(*SF.Execute)
        # driver.get("sf_url")
