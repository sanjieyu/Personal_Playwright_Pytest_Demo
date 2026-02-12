# Author:Yi Sun(Tim) 2024-11-06

'''Test MYOB Quotes Page'''

import pytest
from UIModule.myob_quote import MYOB_Quotes

class Test_MYOB_Quotes():

    def test_myob_quotes_ui_001(self,myob_quote):
        '''Verify the URL'''
        assert myob_quote.check_myob_url == "https://test/Quote/MYOB"

    def test_myob_quotes_ui_002(self,myob_quote):
        '''Verify the title'''
        assert myob_quote.check_myob_title == "MYOB Quotes"

    def test_myob_quotes_ui_003(self,myob_quote):
        '''Verify client details section'''
        assert myob_quote.check_client_details == ("Client Details","Client Name","Contact Number")

    def test_myob_quotes_ui_004(self,myob_quote):
        '''Verify Location section'''
        assert myob_quote.check_location == ("Location","Suburb","Site Address")

    def test_myob_quotes_ui_005(self,myob_quote):
        '''Verify Quote Information section'''
        assert myob_quote.check_quote_info == ("Quote Information", "Proposal No", "User")

    def test_myob_quotes_ui_006(self,myob_quote):
        '''Verify the Client Name box'''
        assert myob_quote.check_client_name_box is True

    def test_myob_quotes_ui_007(self,myob_quote):
        '''Verify the Contact Number  box'''
        assert myob_quote.check_contact_num_box is True

    def test_myob_quotes_ui_008(self,myob_quote):
        '''Verify the Suburb box'''
        assert myob_quote.check_suburb_box is True

    def test_myob_quotes_ui_009(self,myob_quote):
        '''Verify the Site Address box'''
        assert myob_quote.check_site_address_box is True

    def test_myob_quotes_ui_010(self,myob_quote):
        '''Verify the Proposal No box'''
        assert myob_quote.check_proposal_no_box is True

    def test_myob_quotes_ui_011(self,myob_quote):
        '''Verify the default user in User box'''
        assert myob_quote.check_default_user == "All users"

    def test_myob_quotes_ui_012(self,myob_quote):
        '''Verify  search function in MYOB by user, ONLY for DEV'''
        assert myob_quote.search_myob_fun == "209492"