# Author:Yi Sun(Tim) 2023-11-13

'''Test Add Serivce Page'''

import pytest
from UIModule.add_service import Add_Service

class Test_Add_Service():

    def test_addservice_ui_001(self,add_service):
        '''Verify the url for Add Service page'''
        assert add_service.check_add_service_url == "http://xxxx/Service/Create?QuoteId=0"

    def test_addservice_ui_002(self,add_service):
        '''Verify each section in Add Service page'''
        assert add_service.check_sections == ('Doors','Service Details  ','Site Contact Details','Service Items',
                          'Service Documents')

    def test_addservice_ui_003(self,add_service):
        '''Verify each section in Add Service page'''
        assert add_service.check_buttons == 'Back to Services'

    def test_addservice_ui_004(self,add_service):
        '''Verify each elements in "Doors" section'''
        assert add_service.check_doors_section == ('Door Type','Please Select\nCustom Door\nInsulated Sectional\n'
                                                               'anel Lift-Safe\nRoller Door\nSingle Skin Sectional',
                                                   'Additional Door Information')

    def test_addservice_ui_005(self,add_service):
        '''Verify he Additional Door Infomation box in "Doors" section'''
        assert add_service.check_addition_box is True

    def test_addservice_ui_006(self,add_service):
        '''Verify  each elements in "Service Details" section'''
        assert add_service.check_service_details == ('Service Type','Service Area','Service Status','Invoice No.',
                          'Account Type','Account Customer','Order Date','Service Date','Customer PO',
                          'User','Service Tech','Service Tech Name','Description')
