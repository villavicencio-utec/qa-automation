from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.LoginPage import Login
from src.PageObject.Pages.CreateAccountPage import CreateAccount
from src.PageObject.Pages.CategoryPage import Category
from src.PageObject.Pages.CartPage import Cart
from src.PageObject.Pages.PopupPage import Popup
from src.PageObject.Pages.CheckOutPage import CheckOut
from src.PageObject.Pages.CheckOutDetailPage import CheckOutDetail

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

        # Data inputs
        data_generator = Generator(Constant.data_generator_file)
        data_generator.generate_data(1000)
        data_generator.save_json()
        user_value = data_generator.get_data_random()
        name = user_value["name"]
        email = user_value["email"]
        phone = user_value["phone"]
        password = user_value["password"]
        address = user_value["address"]
        city = user_value["city"]
        code = user_value["code"]
        products = user_value["products"]

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

        for index in range(3):
            product_value = products[str(index)]

            qty = product_value["qty"]
            size = product_value["size"]
            color = product_value["color"]
            print(index + 1, qty, size, color)

            if index == 0:
                home = Home(driver)
                home.click_shop_now()

            category = Category(driver)
            product_index = str(index + 1)
            category.click_product_by_index(product_index)
            cart = Cart(driver)
            cart.setQty(qty)
            cart.select_size(size)
            cart = Cart(driver)
            cart.select_color(color)
            cart = Cart(driver)
            cart.click_add_cart_btn()
            popup = Popup(driver)
            popup.click_cart_continue()

            cart = Cart(driver)
            cart.click_woman_icon()
            sleep(5)

        category = Category(driver)
        category.click_shop_icon()

        checkout = CheckOut(driver)
        checkout.click_chechekout_btn()

        sleep(2)
        checkout_detail = CheckOutDetail(driver)
        checkout_detail.setFullName(name)
        checkout_detail.setPhone(phone)
        checkout_detail.setAddress(address)
        checkout_detail.setCity(city)
        checkout_detail.select_country()
        sleep(2)
        checkout_detail.select_province(2)
        checkout_detail.setCode(code)
        sleep(5)
        checkout_detail.click_free_shipping()
        checkout_detail.click_continue_btn()

        sleep(10)


