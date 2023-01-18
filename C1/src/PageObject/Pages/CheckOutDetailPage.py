from selenium.webdriver.common.by import By
from C1.src.PageObject.Locator import Locator
from selenium.webdriver.support.select import Select


class CheckOutDetail(object):
    def __init__(self, driver):
        self.driver = driver
        self.full_name = driver.find_element(By.XPATH, Locator.ck_full_name)
        self.phone = driver.find_element(By.XPATH, Locator.ck_phone)
        self.address = driver.find_element(By.XPATH, Locator.ck_address)
        self.city = driver.find_element(By.XPATH, Locator.ck_city)
        self.country = driver.find_element(By.ID, Locator.ck_country_id)
        self.province = None
        self.code = driver.find_element(By.XPATH, Locator.ck_code)
        self.free_shipping = None
        self.continue_btn = driver.find_element(By.XPATH, Locator.continue_btn)

    def click_continue_btn(self):
        self.continue_btn.click()

    def setFullName(self, name):
        self.full_name.send_keys(name)

    def setPhone(self, phone):
        self.phone.send_keys(phone)

    def setAddress(self, address):
        self.address.send_keys(address)

    def setCity(self, city):
        self.city.send_keys(city)

    def select_country(self):

        dropdown = Select(self.country)
        dropdown.select_by_value("US")

    def select_province(self, index):
        self.province = self.driver.find_element(By.ID, Locator.ck_province_id)
        dropdown = Select(self.province)
        dropdown.select_by_index(index)

    def setCode(self, code):
        self.code.send_keys(code)

    def click_free_shipping(self):
        self.free_shipping = self.driver.find_element(By.XPATH, Locator.ck_free_shipping)
        self.free_shipping.click()
