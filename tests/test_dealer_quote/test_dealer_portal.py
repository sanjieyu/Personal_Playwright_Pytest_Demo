# Author:Yi Sun(Tim) 2024-03-02

'''Test the Dealer Portal Page'''

import pytest
from pages.dealer_portal import Deal_Portal

# Logis as dealer user role
@pytest.mark.role("dealer")
class Test_DealerPortal_UI_Test():

    def test_dealer_portal_ui_001(self,dealer_quote):
        assert "test_sample" in dealer_quote.check_dealer_url

    def test_dealer_portal_ui_002(self,dealer_quote):
        assert dealer_quote.check_default_values ==("test_sample","test_sample","test_sample")

    def test_dealer_portal_ui_003(self,dealer_quote):
        assert dealer_quote.check_find_dealer_quote is True

    def test_dealer_portal_ui_004(self,dealer_quote):
        assert dealer_quote.check_account_menu == ("test_sample","test_sample")
