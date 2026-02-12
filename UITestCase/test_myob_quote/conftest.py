# Author:Yi Sun(Tim) 2024-11-06

import pytest
from UIModule.myob_quote import MYOB_Quotes


@pytest.fixture(scope="class")
def myob_quote(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    myob_quote_page = MYOB_Quotes(page_in_class)
    try:
        myob_quote_page.go_myob_quotes()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return myob_quote_page

