
# Author: Yi Sun(Tim) 2024-08-05

'''Test Account Customer - Pytest Version'''

import pytest
from pages.account_customer import Account_Customer

class Test_Account_Customer():

    @pytest.mark.p0
    def test_account_customer_001(self,account_customer):
        """Verify the url"""
        assert "test_sample" in account_customer.check_accountcustomer_url

    @pytest.mark.p1
    def test_account_customer_002(self,  account_customer):
        """Verify the title"""
        assert "test_sample" in account_customer.check_accountcustomer_title

    @pytest.mark.p1
    def test_account_customer_003(self,  account_customer):
        """Verify the search button"""
        assert account_customer.check_search_btn is True

    @pytest.mark.p1
    def test_account_customer_004(self,  account_customer):
        """Verify the search box"""
        assert account_customer.check_searchbox is True

    @pytest.mark.p2
    def test_account_customer_005(self,  account_customer):
        """Verify each column on this screen"""
        assert account_customer.check_columns == ('test_sample','test_sample','test_sample')

    @pytest.mark.p2
    def test_account_customer_006(self,  account_customer):
        """Verify the Search function"""
        assert "tim2 with priced items" in account_customer.check_search_result

