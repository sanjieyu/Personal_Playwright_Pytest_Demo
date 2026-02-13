# Author:Yi Sun(Tim) 2024-11-06

import pytest
import re
from playwright.sync_api import expect
from pages.myob_quote import MYOB_Quotes

@pytest.fixture(scope="class")
def myob_quote(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    myob_quote_page = MYOB_Quotes(page_in_class)
    myob_quote_page.go_myob_quotes()
    expect(page_in_class).to_have_url(re.compile(f".*{myob_quote_page.url_path}.*"))
    return myob_quote_page

