from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.LoginPage import Login
from src.PageObject.Pages.CreateAccountPage import CreateAccount
from src.PageObject.Pages.CategoryPage import Category

import unittest
from time import sleep
from src.Data.Generator import Generator
from src.TestBase.Constant import Constant

class Test_CreateOrder(WebDriverSetup):
    def test_create_order(self):
        driver = self.driver
        self.driver.get(Constant.url)
        self.driver.set_page_load_timeout(30)

        home = Home(driver)
        sleep(5)

        data_generator = Generator(Constant.data_generator_file)
        user_value = data_generator.get_data_random()
        email = user_value["email"]
        password = user_value["password"]
        name = user_value["name"]

        home.click_Login_icon()

        login = Login(driver)
        login.setEmail(email)
        login.setPassword(password)
        login.click_create_account_btn()

        account = CreateAccount(driver)
        account.setFullName(name)
        account.setEmail(email)
        account.setPassword(password)
        account.click_SignUp_btn()

        home = Home(driver)
        home.click_shop_now()
        sleep(5)

        category = Category(driver)
        # category.select_sort_by_value("price")
        category.select_item(1)
        # category.check_size(1)
        # category.check_color(1)
        # category.check_brand(1)

        sleep(10)


