from selenium.webdriver.common.by import By
from C1.src.PageObject.Locator import Locator


class CreateAccount(object):
    def __init__(self, driver):
        self.driver = driver
        self.full_name = driver.find_element(By.NAME, Locator.full_name)
        self.account_email = driver.find_element(By.NAME, Locator.account_email)
        self.account_password = driver.find_element(By.NAME, Locator.account_password)
        self.sign_up_btn = driver.find_element(By.XPATH, Locator.sign_up_btn)
        self.login_btn = driver.find_element(By.PARTIAL_LINK_TEXT, Locator.account_login_btn)

    def getFullName(self):
        return self.full_name

    def setFullName(self, full_name):
        self.full_name.send_keys(full_name)

    def getAccountEmail(self):
        return self.account_email

    def setEmail(self, email):
        self.account_email.send_keys(email)

    def getAccountPassword(self):
        return self.account_password

    def setPassword(self, password):
        self.account_password.send_keys(password)

    def getSignUp_btn(self):
        return self.sign_up_btn

    def click_SignUp_btn(self):
        self.sign_up_btn.click()

    def getLogin_btn(self):
        return self.login_btn

    def click_login_btn(self):
        self.login_btn.click()
