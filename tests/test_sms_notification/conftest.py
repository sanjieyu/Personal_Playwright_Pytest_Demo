# Author:Yi Sun(Tim) 2024-05-21

import pytest
import re
from playwright.sync_api import expect
from pages.sms_notification import SMS_Notification


@pytest.fixture(scope="class")
def account_customer(page_in_class, credentials):
    """
    Fixture to navigate to Account Customer page and return the page object.
    """
    page_in_class.goto(credentials["egd_url"])
    page_in_class.wait_for_load_state("domcontentloaded")
    customer_page = Account_Customer(page_in_class)
    customer_page.goto_account_customer()
    expect(page_in_class).to_have_url(re.compile(f".*{customer_page.url_path}.*"))
    return customer_page

