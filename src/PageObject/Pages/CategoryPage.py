from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.PageObject.Locator import Locator

class Category(object):
    def __init__(self, driver):
        self.driver = driver
        self.sort_by = driver.find_element(By.XPATH, Locator.sort_by)
        self.size = driver.find_elements(By.XPATH, Locator.size_path)
        self.color = driver.find_elements(By.XPATH, Locator.color_path)
        self.brand = driver.find_elements(By.XPATH, Locator.brand_path)
        self.products = driver.find_elements(By.CLASS_NAME, Locator.product_table)


    def select_sort_by_value(self, index):
        dropdown = Select(self.sort_by)
        dropdown.select_by_value(index)

    def check_size(self, index):
        return 1
        # items = self.size.find_elements_by_tag_name("li")
        # print(self.size)
        # items[index].click()

    def check_color(self, index):
        return 1
        # items = self.color.find_elements_by_tag_name("li")
        # items[index].click()

    def check_brand(self, index):
        return 1
        # items = self.brand.find_elements_by_tag_name("li")
        # items[index].click()

    def select_item(self, index):
        partidos = [match.text for match in self.products]
        value = partidos[index]
        print(value)
        products_link = self.products.find_elements(By.LINK_TEXT, value)
        print("encontrado", products_link)
        products_link.click()
