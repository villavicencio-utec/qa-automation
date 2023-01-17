import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

website = 'https://demo.evershop.io/'

path = '/Users/villavant/PycharmProjects/2023/qa-automation/chromedriver'

class Evershop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(website)
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

website = 'https://demo.evershop.io/'


# Sign in
# Preconditions
# * Generated customer with all customer data
# Test steps
# * Open [Home page](https://demo.evershop.io/)
# * Click *Sign in* button
# * Fill *Email address* and *Password* to create an account
# * Click *Create an account*
# * Log in
# * Select 3 differents products and add it to the cart with different quantities
# * Go to Checkout page and click on Checkout
# * Fill the shipping address and submit
# * Click on success to get correct card information
# * Fill payment information
# * Click Place Order