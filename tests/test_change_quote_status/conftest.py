# Author:Yi Sun(Tim) 2024-11-09

import pytest
import re
from playwright.sync_api import expect
from pages.change_quote_status import Change_Quote_Status


@pytest.fixture(scope="class")
def change_quote_status(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    change_quote_status_page = Change_Quote_Status(page_in_class)
    change_quote_status_page.goto_status_page()
    change_quote_status_page.change_status_order()
    expect(page_in_class).to_have_url(re.compile(f".*{change_quote_status_page.url_path}.*"))
    return change_quote_status_page

