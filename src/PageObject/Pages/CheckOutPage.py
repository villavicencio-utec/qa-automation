from selenium.webdriver.common.by import By
from src.PageObject.Locator import Locator


class CheckOut(object):
    def __init__(self, driver):
        self.driver = driver
        self.chekout_btn = driver.find_element(By.XPATH, Locator.checkout_btn)

    def click_chechekout_btn(self):
        self.chekout_btn.click()