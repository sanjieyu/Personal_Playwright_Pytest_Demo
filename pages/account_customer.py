# Author:Yi Sun(Tim) 2024-1-22

'''Account Customer Page'''

from playwright.sync_api import Page
from pages.admin_portal import Admin_Page

class Account_Customer(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "Customer/List"
        self._init_locators_account_customer()

    def _init_locators_account_customer(self):
        '''loc for default values in this page'''
        self.account_title_loc = self.page.locator('h1.header')
        self.account_searchbtn_loc = self.page.locator('button.btn-primary')
        self.account_searchbox_loc = self.page.locator('#searchCustomerName')
        self.customer_name_loc = self.page.locator("xpath=//span[text()='Customer Name']")
        self.contact_name_loc = self.page.locator("xpath=//span[text()='Contact Name']")
        self.address_loc = self.page.locator("xpath=//span[text()='Address']")
        self.email_loc = self.page.locator("xpath=//span[text()='Email']")
        self.suburb_loc = self.page.locator("xpath=//span[text()='Suburb']")
        self.search_result_name_loc = self.page.locator("a[href*='/Customer/Edit/']")

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
        print('title is:',acocount_customer_title)
        return acocount_customer_title

    @property
    def check_search_btn(self):
        '''Check the search button'''
        account_btn = self.account_searchbtn_loc
        if account_btn.is_enabled():
            print('is there')
            return True
        else:
            print('is missing')
            return False

    @property
    def check_searchbox(self):
        '''Check the search box'''
        account_box = self.account_searchbox_loc
        if account_box.is_visible():
            print('is there')
            return True
        else:
            print('is missing')
            return False

    @property
    def check_columns(self):
        '''Check each column on the screen'''
        customer_name = self.customer_name_loc.inner_text()
        contact_name = self.contact_name_loc.inner_text()
        address = self.address_loc.inner_text()
        email = self.email_loc.inner_text()
        suburb = self.suburb_loc.inner_text()
        print(customer_name,contact_name,address,email,suburb)
        return customer_name,contact_name,address,email,suburb

    @property
    def check_search_result(self):
        '''Check the Search function'''
        self.account_searchbox_loc.fill('tim2')
        self.account_searchbtn_loc.click()

        self.search_result_name_loc.wait_for()
        search_result_name = self.search_result_name_loc.inner_text()
        print(search_result_name)
        return search_result_name


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://xxx/")
        login = Account_Customer(page)
        login.typeUserName('yxxx')
        login.typePassword('xxxx')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.goto_account_customer()
        # login.check_accountcustomer_url
        # login.check_accountcustomer_title
        # login.check_search_btn
        # login.check_searchbox
        # login.check_columns
        login.check_search_result



