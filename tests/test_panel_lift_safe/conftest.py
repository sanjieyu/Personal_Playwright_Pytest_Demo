# Author:Yi Sun(Tim) 2024-11-06

import pytest
import re
from playwright.sync_api import expect
from pages.panel_left_safe import Panel_lift_Safe


@pytest.fixture(scope="class")
def panel_lift_safe(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    panel_lift_safe_page = Panel_lift_Safe(page_in_class)
    panel_lift_safe_page.go_production()
    panel_lift_safe_page.go_panel_lift_safe()
    expect(page_in_class).to_have_url(re.compile(f".*{panel_lift_safe_page.url_path}.*"))
    return panel_lift_safe_page

