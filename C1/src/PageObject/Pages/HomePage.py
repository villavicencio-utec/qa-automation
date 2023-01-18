from selenium.webdriver.common.by import By
from C1.src.PageObject.Locator import Locator


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element(By.CLASS_NAME, Locator.logo)
        self.login_icon = driver.find_element(By.XPATH, Locator.login_icon_btn)
        self.shop_icon = driver.find_element(By.CLASS_NAME, Locator.shop_icon_btn)
        self.men_icon = driver.find_element(By.LINK_TEXT, Locator.men_icon)
        self.woman_icon = driver.find_element(By.XPATH, Locator.woman_icon)
        self.kids_icon = driver.find_element(By.LINK_TEXT, Locator.kids_icon)
        self.shop_now_btn = driver.find_element(By.XPATH, Locator.shop_now_btn)


    def click_shop_now(self):
        self.shop_now_btn.click()

    def click_Login_icon(self):
        self.login_icon.click()

    def click_Shop_icon(self):
        self.shop_icon.click()

    def click_Logo(self):
        self.logo.click()

    def click_men_icon(self):
        self.men_icon.click()

    def click_kid_icon(self):
        self.kids_icon.click()

    def click_woman_icon(self):
        self.woman_icon.click()


