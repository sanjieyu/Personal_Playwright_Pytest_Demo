# Author:Yi Sun(Tim) 2024-09-12

'''Test Rolling Cycle Management Page'''

import pytest
from UIModule.rolling_cycle_management import *

class Test_Rolling_Cycle():

    def test_rolling_management_ui_001(self,rolling_cycle_management):
        '''Verify the url of Rolling Cycle Management Page'''
        assert rolling_cycle_management.check_rolling_url == 'https://test'

    def test_rolling_management_ui_002(self,rolling_cycle_management):
        '''Verify the title of Rolling Cycle Management Page'''
        assert rolling_cycle_management.check_rolling_title == 'Rolling Cycle Management  '

    def test_rolling_management_ui_003(self,rolling_cycle_management):
        '''Verify the tab of Rolling Cycle Management Page'''
        expected =('General Settings','Colour Cycles Settings','Temporary Closed','History')
        actual = rolling_cycle_management.check_tab
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_rolling_management_ui_004(self,rolling_cycle_management):
        '''Verify the General Settings screen'''
        expected =('Split Doors','Lockout Settings','Default Shift Settings')
        actual = rolling_cycle_management.check_general_settings
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_rolling_management_ui_005(self,rolling_cycle_management):
        '''Verify the Colour Cycle Settings screen'''
        expected =('Coil Settings','Save Coil Settings')
        actual = rolling_cycle_management.check_colour_cycle_settings
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_rolling_management_ui_006(self,rolling_cycle_management):
        '''Verify the Temp Closed screen'''
        expected =('Temporary Closed Colour Cycles','Update Cycles')
        actual = rolling_cycle_management.check_temp_closed
        assert actual == expected,f"Expected:{expected},but got: {actual}"
