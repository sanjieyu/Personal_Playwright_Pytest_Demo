# Author:Yi Sun(Tim) 2024-1-22

import pytest
import re
from playwright.sync_api import expect
from pages.add_quote import Add_Quote

@pytest.fixture(scope="class")
def add_quote(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    add_quote_page = Add_Quote(page_in_class)
    add_quote_page.go_addquote()
    expect(page_in_class).to_have_url(re.compile(f".*{add_quote_page.url_path}.*"))
    return add_quote_page

