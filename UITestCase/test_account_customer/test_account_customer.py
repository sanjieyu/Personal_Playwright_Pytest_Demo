
# Author: Yi Sun(Tim) 2024-08-05

'''Test Account Customer - Pytest Version'''

import pytest
from UIModule.account_customer import Account_Customer

class Test_Account_Customer():

    def test_account_customer_001(self,account_customer):
        '''Verify the url'''
        assert "Customer/List" in account_customer.check_accountcustomer_url

    def test_account_customer_002(self,  account_customer):
        '''Verify the title'''
        assert "Account Customers Search" in account_customer.check_accountcustomer_title

    def test_account_customer_003(self,  account_customer):
        '''Verify the search button'''
        assert account_customer.check_search_btn is True

    def test_account_customer_004(self,  account_customer):
        '''Verify the search box'''
        assert account_customer.check_searchbox is True

    def test_account_customer_005(self,  account_customer):
        '''Verify each column on this screen'''
        assert account_customer.check_columns == ('Customer Name','Contact Name','Address','Email','Suburb')

    def test_account_customer_006(self,  account_customer):
        '''Verify the Search function'''
        assert "tim2 with priced items" in account_customer.check_search_result

