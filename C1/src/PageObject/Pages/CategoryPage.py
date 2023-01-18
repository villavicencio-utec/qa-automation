from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.PageObject.Locator import Locator

class Category(object):
    def __init__(self, driver):
        self.driver = driver
        # self.sort_by = driver.find_element(By.XPATH, Locator.sort_by)
        self.size = driver.find_elements(By.XPATH, Locator.size_path)
        self.color = driver.find_elements(By.XPATH, Locator.color_path)
        self.brand = driver.find_elements(By.XPATH, Locator.brand_path)
        self.product = None
        self.shop_icon = driver.find_element(By.CLASS_NAME, Locator.shop_icon_btn)

    def click_shop_icon(self):
        self.shop_icon.click()

    def click_product_by_index(self, index):
        self.product = self.driver.find_element(By.XPATH, Locator.product_base + index + Locator.product_end)
        self.product.click()

    # def select_sort_by_value(self, index):
    #     dropdown = Select(self.sort_by)
    #     dropdown.select_by_value(index)

    def check_size(self, index):
        items = self.size.find_elements_by_tag_name("li")
        items[index].click()

    def check_color(self, index):
        items = self.color.find_elements_by_tag_name("li")
        items[index].click()

    def check_brand(self, index):
        items = self.brand.find_elements_by_tag_name("li")
        items[index].click()

