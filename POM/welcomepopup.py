from selenium.webdriver.common.by import By


class wcpopup:

    def __init__(self, driver):
        self.driver = driver

    wc_to_vc= (By.XPATH , "//p[text()='Welcome to Volvo Connect']")
    popup_close = (By.XPATH, "//span[@part='boundary'][2]")
    close_button = (By.XPATH , "//button[text()='Close']")

    def verify_wc(self):
        return self.driver.find_element(*wcpopup.wc_to_vc)

    def click_close(self):
        return self.driver.find_element(*wcpopup.popup_close)

    def click_closebutton(self):
        return self.driver.find_element(*wcpopup.close_button)

