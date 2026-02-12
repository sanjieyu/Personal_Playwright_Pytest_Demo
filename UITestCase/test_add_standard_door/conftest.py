# Author:Yi Sun(Tim) 2024-11-30

import pytest
from UIModule.add_standar_door import Add_Standard_Door

@pytest.fixture(scope="class")
def add_standard_door(page_in_class,credentials):   # credentials
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    add_standard_door_page = Add_Standard_Door(page_in_class)
    try:
        add_standard_door_page.go_addquote()
        add_standard_door_page.go_addstandarddoor()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return add_standard_door_page

