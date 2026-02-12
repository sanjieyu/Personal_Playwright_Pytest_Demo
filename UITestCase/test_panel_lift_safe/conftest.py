# Author:Yi Sun(Tim) 2024-11-06

import pytest
from UIModule.panel_left_safe import Panel_lift_Safe


@pytest.fixture(scope="class")
def panel_lift_safe(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    panel_lift_safe_page = Panel_lift_Safe(page_in_class)
    try:
        panel_lift_safe_page.go_production()
        panel_lift_safe_page.go_panel_lift_safe()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return panel_lift_safe_page

