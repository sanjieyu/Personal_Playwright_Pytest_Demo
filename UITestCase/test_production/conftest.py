# Author:Yi Sun(Tim) 2024-11-06

import pytest
from UIModule.production import Production


@pytest.fixture(scope="class")
def production(page_in_class,credentials):
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    production_page = Production(page_in_class)
    try:
        production_page.go_production()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return production_page

