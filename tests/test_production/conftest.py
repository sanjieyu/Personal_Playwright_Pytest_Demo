# Author:Yi Sun(Tim) 2024-11-06

import pytest
import re
from playwright.sync_api import expect
from pages.production import Production


@pytest.fixture(scope="class")
def production(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    production_page = Production(page_in_class)
    production_page.go_production()
    expect(page_in_class).to_have_url(re.compile(f".*{production_page.url_path}.*"))
    return production_page

