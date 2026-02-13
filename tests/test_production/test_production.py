# Author:Yi Sun(Tim) 2024-11-06

'''Test Production Page'''

import pytest
from pages.production import Production

class Test_Production_UI_Test():

    def test_production_ui_001(self,production):
        '''Verify the url for Production page'''
        assert production.check_production_url == 'https://test'

    def test_production_ui_002(self,production):
        '''Verify the title for Production page'''
        assert production.check_production_title == 'Production Details'

    def test_production_ui_003(self,production):
        '''Verify each section in Production page'''
        assert production.check_production_section == ('ExoRoll Doors','Panel Lift Safe','Insulated Doors','Custom Doors',
                          'Roller Shutters','[OBSOLETE] All Doors')
