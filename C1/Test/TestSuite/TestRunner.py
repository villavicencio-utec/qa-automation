from unittest import TestLoader, TestSuite, TextTestRunner
from C1.Test.Scripts.Test_HomePage import EverShopHomePage
from C1.Test.Scripts.Test_LoginPage import EverShopLoginPage
from C1.Test.Scripts.Test_CreateOrder import Test_CreateOrder
import testtools as tt

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Test_CreateOrder),
        # test_loader.loadTestsFromTestCase(EverShopLoginPage),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = tt.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(tt.StreamResult())
    # self.driver.set_page_load_timeout(30))