# Author:Yi Sun(Tim) 2024-3-02

import pytest
import re
from playwright.sync_api import expect
from pages.dealer_portal import Deal_Portal


@pytest.fixture(scope="class")
def dealer_quote(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    dealer_quote_page = Deal_Portal(page_in_class)
    expect(page_in_class).to_have_url(re.compile(f".*{dealer_quote_page.url_path}.*"))
    return dealer_quote_page

