from selenium.webdriver.common.by import By
from C1.src.PageObject.Locator import Locator


class Cart(object):
    def __init__(self, driver):
        self.driver = driver
        self.qty = driver.find_element(By.NAME, Locator.qty_name)
        self.size = None
        self.color = None
        self.add_cart_btn = driver.find_element(By.XPATH, Locator.add_cart_btn)
        self.woman_icon = driver.find_element(By.XPATH, Locator.woman_icon)

    def click_woman_icon(self):
        self.woman_icon.click()

    def setQty(self, qty):
        self.qty.clear()
        self.qty.send_keys(qty)

    def select_size(self, size):
        if size == "S":
            self.size = self.driver.find_element(By.LINK_TEXT, Locator.size_s)
        elif  size == "X":
            self.size = self.driver.find_element(By.LINK_TEXT, Locator.size_x)
        elif size == "L":
            self.size = self.driver.find_element(By.LINK_TEXT, Locator.size_l)
        elif size == "XL":
            self.size = self.driver.find_element(By.LINK_TEXT, Locator.size_xl)
        elif size == "M":
            self.size = self.driver.find_element(By.LINK_TEXT, Locator.size_m)

        self.size.click()

    def select_color(self, color):

        if color == "White":
            self.color = self.driver.find_element(By.LINK_TEXT, Locator.color_white)
        elif color == "Black":
            self.color = self.driver.find_element(By.LINK_TEXT, Locator.color_black)
        elif color == "Purple":
            self.color = self.driver.find_element(By.LINK_TEXT, Locator.color_purple)
        elif color == "Red":
            self.color = self.driver.find_element(By.LINK_TEXT, Locator.color_red)
        else:
            self.color = self.driver.find_element(By.LINK_TEXT, Locator.color_blue)
        self.color.click()

    def click_add_cart_btn(self):
        self.add_cart_btn.click()


