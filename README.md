# qa-automation
## C1
1.  I am using POM patron to create a class per page, it could be usefull to reuse the locators per page.
2.  The chromedriver support Chrome's version 109.0 if you have the same Chrome's version, you can run the automated functional test just running 
TestSuite >> TestRunner.py. You can download chromedriver in following link : https://chromedriver.chromium.org
3. Locatos.py is where I save the form of selection of the webelement, for example it could be by XPATH, ID , NAME.
4. I have created a class Generator which is able to create a Test data with Python library Faker, it create a .json with a key named "used", when you run the test case, the program is going to take only user's information which had never been used.
5. If we want to run all the test in another browser, we have to change only the WebDriverSetup.py and download the respective driver.


## C2
For the Challengue 2, you have to download the .json file to import into Postman.
The token has a limited quantity of intends so if you haver more than 50 request, you should create another account and change the new token in the
parameters section.
