# Author:Yi Sun(Tim) 2024-11-09

'''Test Change Quote Status'''

import pytest
from pages.change_quote_status import Change_Quote_Status

class Test_Change_Quote_Status():

    def test_status_change_ui_001(self,change_quote_status):
        '''Verify the status change function, change a quote status to "MYOB Ready"'''
        result = change_quote_status.check_myob_status()
        assert result is True

    def test_status_change_ui_002(self,change_quote_status):
            '''Verify the status change function, change a quote status to "Order" then check if
            it is listed in Order Screen'''
            result = change_quote_status.check_order_status()
            assert result is True

    def test_status_change_ui_003(self,change_quote_status):
        '''Verify the status change function, change a quote status to "Rollforming"'''
        result = change_quote_status.check_rollforming_status()
        assert result is True