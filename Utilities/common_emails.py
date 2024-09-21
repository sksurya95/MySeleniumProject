import time
import pyotp
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.Config import COUNTRY_VARIABLES
from POM.Emails import Emails
from POM.outlookfile import Emailbox


def outlook_signin(driver, country):
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=159&ct=1725283997&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3den-us%26country%3dus%26RpsCsrfState%3d3a1a22f2-6fdf-0e3e-5c33-f8ae8c77b7fa&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
    time.sleep(3)
    email = Emailbox(driver)
    email_address = country.get('email_id')
    email.input_email_id().send_keys(email_address)
    time.sleep(2)
    email.click_next().click()
    time.sleep(5)
    email.input_password().send_keys("9Hh-.}4u/+fisiF.@E.HT6hYF>a`<H")
    time.sleep(2)
    email.click_signin().click()
    time.sleep(2)
    totp = pyotp.TOTP(country['otp_secret_key'])
    otp_code = totp.now()
    print(otp_code)
    email.input_otp().send_keys(otp_code)
    email.input_verify().click()
    time.sleep(2)
    email.input_Yes().click()


def set_password(driver , cred):
    emails = Emails(driver)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(Emails.Sandbox))
    emails.click_sandbox().click()
    wait.until(EC.visibility_of_element_located(Emails.password_button))
    emails.click_password().click()
    time.sleep(5)
    window_handles = driver.window_handles
    if len(window_handles) > 1:
        driver.switch_to.window(window_handles[-1])
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(Emails.change_password))
    url=driver.current_url
    print(url)
    title=driver.title
    print(title)
    # text=emails.verify_changepassword().text
    # print(text)
    password = cred["password"]
    emails.type_newpassword().send_keys(password)
    emails.type_confirmpassword().send_keys(password)
    emails.click_changepassword().click()