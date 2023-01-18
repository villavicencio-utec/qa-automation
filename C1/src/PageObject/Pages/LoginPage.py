from selenium.webdriver.common.by import By
from C1.src.PageObject.Locator import Locator


class Login(object):
    def __init__(self, driver):
        self.driver = driver
        self.email = driver.find_element(By.NAME, Locator.email)
        self.password = driver.find_element(By.NAME, Locator.password)
        self.signin_btn = driver.find_element(By.XPATH, Locator.signin_btn)
        self.create_accoutn_btn = driver.find_element(By.LINK_TEXT, Locator.create_account)

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email.send_keys(email)

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password.send_keys(password)

    def getSignIn_btn(self):
        return self.signin_btn

    def click_Sigin_btn(self):
        self.signin_btn.click()

    def getCreate_account_btn(self):
        return self.create_accoutn_btn

    def click_create_account_btn(self):
        self.create_accoutn_btn.click()




