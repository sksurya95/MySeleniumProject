from selenium.webdriver.common.by import By


class Self_registration:

    def __init__(self, driver):
        self.driver = driver

    FirstName = (By.XPATH, "//input[@name='fnameinput']")
    LastName =  (By.XPATH, "//input[@name='lnameinput']")
    Email =  (By.XPATH, "//input[@name='emailinput']")
    Country =  (By.XPATH, "//span[normalize-space()='Select country']")
    Country_list= (By.XPATH, "//div[@part='dropdown overlay']//span[@title]")
    Checkbox= (By.XPATH, "//input[@type='checkbox']")
    Register= (By.XPATH, "//span[text()='Register']")
    Checkyouremail = (By.XPATH, "//span[@class='check-your-email-heading']")
    Registernow=(By.XPATH,"//button[text()='Register now']")
    companyname=(By.XPATH,"//input[@name='companynameinput']")
    regnumber=(By.XPATH,"//input[@name='regnumberinput']")
    BillingEmail=(By.XPATH,"//input[@name='billingemail']")
    postinput=(By.XPATH,"//input[@name='postalinput']")
    cityinput=(By.XPATH,"//input[@name='cityinput']")
    street=(By.XPATH,"//input[@name='streetinput']")
    Submit=(By.XPATH,"//button[text()='Submit']")

    def input_firstname(self):
        return self.driver.find_element(*Self_registration.FirstName)

    def input_lastname(self):
        return self.driver.find_element(*Self_registration.LastName)

    def input_email(self):
        return self.driver.find_element(*Self_registration.Email)

    def input_country(self):
        return self.driver.find_element(*Self_registration.Country)

    def input_country_list(self):
        return self.driver.find_elements(*Self_registration.Country_list)

    def input_checkbox(self):
        return self.driver.find_element(*Self_registration.Checkbox)

    def input_register(self):
        return self.driver.find_element(*Self_registration.Register)

    def input_checkemail(self):
        return self.driver.find_element(*Self_registration.Checkyouremail)


    def click_registernow(self):
        return self.driver.find_element(*Self_registration.Registernow)

    def input_companyname(self):
        return self.driver.find_element(*Self_registration.companyname)

    def input_registrationnumber(self):
        return self.driver.find_element(*Self_registration.regnumber)

    def input_billingemail(self):
        return self.driver.find_element(*Self_registration.BillingEmail)

    def input_postalinput(self):
        return self.driver.find_element(*Self_registration.postinput)

    def input_city(self):
        return self.driver.find_element(*Self_registration.cityinput)

    def input_street(self):
        return self.driver.find_element(*Self_registration.street)

    def click_submit(self):
        return self.driver.find_element(*Self_registration.Submit)

