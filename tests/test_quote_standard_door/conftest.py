# Author:Yi Sun(Tim) 2024-11-03

import pytest
from pages.quote_standard_door import Quote_Standard_Door


@pytest.fixture(scope="class")
def quote_standard_door(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    quote_standard_door_page = Quote_Standard_Door(page_in_class)
    try:
        quote_standard_door_page.add_door_fun()
        prop_no =quote_standard_door_page.get_proposal_number
        quote_standard_door_page.search_new_quote(prop_no)
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return quote_standard_door_page

