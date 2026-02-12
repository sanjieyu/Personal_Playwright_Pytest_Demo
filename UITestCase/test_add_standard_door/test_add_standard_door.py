# Author:Yi Sun(Tim) 2024-11-30

'''Test Add a Standard Door Functian'''

import pytest
from UIModule.add_standar_door import *


class Test_Add_StandardDoor_Fun():

    def test_add_standarddoor_fun_001(self,add_standard_door):
        '''Verify the input validation when add a new door'''
        expected = ['Errors','Door type is required','Door design is required','Door finish is required',
                    'Door color is required','Packaging Type must be selected.',
                    'If SR (left) is less than 89mm, LH Jamb should be minimum 90mm.',
                    'If SR (right) is less than 89mm, RH Jamb should be minimum 90mm.']
        raw_actual = add_standard_door.validation_input
        actual = [item.strip() for item in raw_actual.split('\n') if item.strip()]
        assert actual == expected

    def test_add_standarddoor_fun_002(self,add_standard_door):
        '''Verify the add door function'''
        add_standard_door.add_door()
        assert add_standard_door.new_added_door ==('1   Panel Lift-Safe, Classic panel, Woodgrain Texture, '
                                                   'Monument (2010 x 2560)')

    def test_add_standarddoor_fun_003(self,add_standard_door):
        '''Verify the duplicate button for the new added door'''
        assert add_standard_door.duplicate_btn is True

    def test_add_standarddoor_fun_004(self,add_standard_door):
        '''Verify the delete button for the new added door'''
        assert  add_standard_door.delete_btn is True