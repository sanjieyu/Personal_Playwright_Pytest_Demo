# Author:Yi Sun(Tim) 2024-11-09

import pytest
from UIModule.change_quote_status import Change_Quote_Status


@pytest.fixture(scope="class")
def change_quote_status(page_in_class,credentials):   #credentials
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    change_quote_status_page = Change_Quote_Status(page_in_class)
    try:
        change_quote_status_page.goto_status_page()
        change_quote_status_page.change_status_order()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return change_quote_status_page

