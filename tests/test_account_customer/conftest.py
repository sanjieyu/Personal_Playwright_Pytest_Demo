# Author:Yi Sun(Tim) 2024-1-22

import pytest
from pages.account_customer import Account_Customer

@pytest.fixture(scope="class")
def account_customer(page_in_class,credentials):

    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("networkidle")
    customer_page = Account_Customer(page_in_class)
    try:
        customer_page.goto_account_customer()
    except Exception as e:
        print(f"fail to goto the correct URL: {page_in_class.url}")
        raise e
    return customer_page

