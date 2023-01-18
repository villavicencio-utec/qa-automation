from selenium.webdriver.common.by import By
from src.PageObject.Locator import Locator

class Popup(object):
    def __init__(self, driver):
        self.driver = driver
        self.cart_continue = driver.find_element(By.LINK_TEXT, Locator.cart_continue)

    def click_cart_continue(self):
        self.cart_continue.click()