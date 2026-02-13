# Author:Yi Sun(Tim) 2024-1-22

import pytest
import re
from playwright.sync_api import expect
from pages.add_service import Add_Service

@pytest.fixture(scope="class")
def add_service(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    add_service_page = Add_Service(page_in_class)
    add_service_page.go_addservice()
    expect(page_in_class).to_have_url(re.compile(f".*{add_service_page.url_path}.*"))
    return add_service_page

