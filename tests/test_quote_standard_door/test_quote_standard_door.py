# Author:Yi Sun(Tim) 2024-11-06

'''Test Add a Quote with a standard door function'''

import pytest
from pages.quote_standard_door import *

class Test_Quote_Standard_Door():

    def test_quote_standard_door_001(self,quote_standard_door):
        """Verify  Add a Quote with a standard door function"""
        assert quote_standard_door.verify_new_quote == ('test_sample','test_sample')