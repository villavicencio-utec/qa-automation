from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.LoginPage import Login
import unittest
from time import sleep
from src.Data.Generator import Generator
from src.TestBase.Constant import Constant

class EverShopLoginPage(WebDriverSetup):



    def test_Login_Page(self):


        driver = self.driver
        self.driver.get(Constant.url)
        self.driver.set_page_load_timeout(30)
        home = Home(driver)

        home.click_Login_icon()
        sleep(5)

        data_generator = Generator(Constant.data_generator_file)
        user_value = data_generator.get_data_random()
        self.email = user_value["email"]
        self.password = user_value["password"]

        login = Login(driver)
        login.setEmail(self.email)
        login.setPassword(self.password)
        login.click_create_account_btn()

if __name__ == '__main__':
    unittest.main()