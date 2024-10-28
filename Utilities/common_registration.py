import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.Config import COUNTRY_VARIABLES


from POM.Homepage import Homepage
from POM.self_registration import Self_registration
from selenium.webdriver.common.action_chains import ActionChains

country = COUNTRY_VARIABLES
name = country.get("country_name")
print(name)

def random_number():
    return int(time.time())


def email_format(test, random_numbers,  extension):
    generated_email= f"{test}{random_numbers}{extension}"
    return generated_email


def getemail_from_config(country_variables , symbol , random_numbers):
    email_id = country_variables.get('email_id')
    mailbox , domain = email_id.split("@")
    email_generated = f"{mailbox}{symbol}{random_numbers}@{domain}"
    return email_generated


random_numbers=random_number()

def random_email():
    print(name)
    Formatted_email1 = getemail_from_config(name, "+", random_numbers)
    print(Formatted_email1)


# Formatted_email= email_format("test+",random_number(), "@volvo.com")



def self_registration(driver, firstname, lastname, email , country):
    homepage = Homepage(driver)
    register = Self_registration(driver)
    register.input_firstname().send_keys(firstname)
    register.input_lastname().send_keys(lastname)
    # epoch_number = random_number()
    # email_format("firstname" , "lastname" , "epoch_number" , "volvo.com")
    register.input_email().send_keys(email)
    register.input_country().click()
    elements = register.input_country_list()
    for i in elements:
        if i.text == "Canada":
            wait = WebDriverWait(driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, country)))
            country_element = driver.find_element(By.XPATH, country)
            ActionChains(driver).move_to_element(country_element).click().perform()
    register.input_checkbox().click()
    register.input_register().click()
    time.sleep(10)
    # text = register.input_checkemail().text
    # driver.sleep(10)
    # assert "Check your email" in text
def sru_validations(driver, xpath):
    homepage = Homepage(driver)
    register = Self_registration(driver)
    element = driver.find_element(By.XPATH,xpath)
    text = element.text
    return text


def sru_form_validations(driver):
    xpath_text_map = {
        "//label[text()='First name']": "First name",
        "//label[text()='Last name']": "Last name",
        "//span[text()='Email']": "Email",
        "//label[text()='Country of operation']": "Country of operation",
        "//label[text()='Job title']": "Job title",
        "//label[text()='Mobile']": "Mobile",
    }
    time.sleep(2)
    for xpath, expected_text in xpath_text_map.items():
        print(expected_text)
        actual_text = sru_validations(driver, xpath)
        assert expected_text in actual_text

def company(driver , cname,rno , bemail,postal, cityinput, street):
    register=Self_registration(driver)
    register.click_registernow().click()
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(register.companyname))
    register.input_companyname().send_keys(cname)
    register.click_selecttype().click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located(register.regnumber))
    register.click_regnumber().click()
    register.input_registrationnumber().send_keys(rno)
    register.input_billingemail().send_keys(bemail)
    register.input_postalinput().send_keys(postal)
    register.input_city().send_keys(cityinput)
    register.input_street().send_keys(street)
    time.sleep(10)
    register.click_submit().click()
    wait.until(EC.visibility_of_element_located(register.Close))
    register.click_close().click()



#Testabc
