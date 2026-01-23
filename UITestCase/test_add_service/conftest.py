# Author:Yi Sun(Tim) 2024-1-22

import pytest
from UIModule.add_service import Add_Service


@pytest.fixture(scope="class")
def add_service(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    add_service_page = Add_Service(page_in_class)
    try:
        add_service_page.go_addservice()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return add_service_page

