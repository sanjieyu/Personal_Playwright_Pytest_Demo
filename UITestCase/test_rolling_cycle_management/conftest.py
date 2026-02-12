# Author:Yi Sun(Tim) 2024-09-12

import pytest
from UIModule.rolling_cycle_management import Rolling_Cycle_Management


@pytest.fixture(scope="class")
def rolling_cycle_management(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    rolling_cycle_management_page = Rolling_Cycle_Management(page_in_class)
    try:
        rolling_cycle_management_page.go_rolling()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return rolling_cycle_management_page

