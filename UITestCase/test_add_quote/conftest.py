# Author:Yi Sun(Tim) 2024-1-22

import pytest
from UIModule.add_quote import Add_Quote



@pytest.fixture(scope="class")
def add_quote(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    add_quote_page = Add_Quote(page_in_class)
    try:
        add_quote_page.go_addquote()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return add_quote_page

