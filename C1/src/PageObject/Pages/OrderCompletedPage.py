from selenium.webdriver.common.by import By
from C1.src.PageObject.Locator import Locator


class OrderCompleted(object):
    def __init__(self, driver):
        self.driver = driver
        # self.contact_email = driver.find_element(By.XPATH, Locator.contact_email)
        # self.payment = driver.find_element(By.XPATH, Locator.payment)
        # self.full_name = driver.find_element(By.CLASS_NAME, Locator.sa_full_name)
        # self.address_one = driver.find_element(By.CLASS_NAME, Locator.sa_address_one)
        # self.city_province_postcode = driver.find_element(By.CLASS_NAME, Locator.sa_city_province_postcode)
        # self.telephone = driver.find_element(By.CLASS_NAME, Locator.sa_telephone)

    def getContact_email(self):
        return self.driver.find_element(By.XPATH, Locator.contact_email).text
