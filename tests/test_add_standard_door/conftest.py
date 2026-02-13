# Author:Yi Sun(Tim) 2024-11-30

import pytest
import re
from playwright.sync_api import expect
from pages.add_standar_door import Add_Standard_Door

@pytest.fixture(scope="class")
def add_standard_door(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    add_standard_door_page = Add_Standard_Door(page_in_class)
    add_standard_door_page.go_addquote()
    add_standard_door_page.go_addstandarddoor()
    expect(page_in_class).to_have_url(re.compile(f".*{add_standard_door_page.url_path}.*"))
    return add_standard_door_page

