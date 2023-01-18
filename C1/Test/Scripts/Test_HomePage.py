from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import Home
from src.TestBase.Constant import Constant
import unittest


class EverShopHomePage(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        self.driver.get(Constant.url)
        self.driver.set_page_load_timeout(30)

        web_page_title = "An Amazing EverShop Store"

        try:
            if driver.title == web_page_title:
                print("Homepage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "Homepage failed to load")

        home_page = Home(driver)


if __name__ == '__main__':
    unittest.main()