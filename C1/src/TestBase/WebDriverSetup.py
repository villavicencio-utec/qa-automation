import unittest
from selenium import webdriver
from C1.src.TestBase.Constant import Constant
import urllib3


class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome(Constant.path)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            print("Clean up of Test Environment")
        self.driver.close()
        self.driver.quit()
