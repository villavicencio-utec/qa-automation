from selenium.webdriver.common.by import By
from src.PageObject.Locator import Locator


class Billing(object):
    def __init__(self, driver):
        self.driver = driver
        self.cash_rb = driver.find_element(By.XPATH, Locator.cash)
        self.paypal_rb = driver.find_element(By.XPATH, Locator.paypal)
        self.visa_rb = driver.find_element(By.XPATH, Locator.visa)
        self.place_order_btn = driver.find_element(By.XPATH, Locator.pace_order)

    def select_cash(self):
        self.cash_rb.click()

    def select_paypal(self):
        self.paypal_rb.click()

    def select_visa(self):
        self.visa_rb.click()

    def click_place_order_btn(self):
        self.place_order_btn.click()