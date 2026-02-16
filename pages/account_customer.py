# Author:Yi Sun(Tim) 2024-1-22

'''Account Customer Page'''

from playwright.sync_api import Page
from pages.admin_portal import Admin_Page

class Account_Customer(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "test_sample"
        self._init_locators_account_customer()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators_account_customer(self):
        '''loc for default values in this page'''
        self.account_title_loc = self.page.locator('test_sample')
        self.account_searchbtn_loc = self.page.get_by_role("button", name="test_sample")
        self.account_searchbox_loc = self.page.get_by_text("test_sample")
        self.account_search_loc = self.page.get_by_label("test_sample")


    def goto_account_customer(self):
        '''Go to account customer screen'''
        self.list_loc.click()
        self.account_list_loc.click()
        self.account_title_loc.wait_for()

    @property
    def check_accountcustomer_url(self):
        account_customer_url = self.page.url
        print('url is:',account_customer_url)
        return account_customer_url

    @property
    def check_accountcustomer_title(self):
        '''Check the url'''
        acocount_customer_title = self.account_title_loc.inner_text()
        return acocount_customer_title

    @property
    def check_search_btn(self):
        '''Check the search button'''
        account_btn = self.account_searchbtn_loc
        if account_btn.is_enabled():
            return True
        else:
            return False

    @property
    def check_searchbox(self):
        '''Check the search box'''
        account_box = self.account_searchbox_loc
        if account_box.is_visible():
            return True
        else:
            return False

    @property
    def check_columns(self):
        '''Check each column on the screen'''
        customer_name = self.customer_name_loc.inner_text()
        contact_name = self.contact_name_loc.inner_text()
        address = self.address_loc.inner_text()
        email = self.email_loc.inner_text()
        suburb = self.suburb_loc.inner_text()
        return customer_name,contact_name,address,email,suburb

    @property
    def check_search_result(self):
        '''Check the Search function'''
        self.account_searchbox_loc.fill('test_sample')
        self.account_searchbtn_loc.click()
        self.search_result_name_loc.wait_for()
        search_result_name = self.search_result_name_loc.inner_text()
        return search_result_name


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test_sample")
        login = Account_Customer(page)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.goto_account_customer()



