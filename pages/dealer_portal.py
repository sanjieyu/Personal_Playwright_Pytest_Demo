# Author:Yi Sun(Tim) 2024-3-02

'''Dealer Portal Page'''

from playwright.sync_api import Page,expect
from pages.admin_portal import Admin_Page

class Deal_Portal(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "Dealer"
        self._init_locators_dp()

    def _init_locators_dp(self):
        '''loc for the dealer portal page'''
        self.find_quote_box = self.page.get_by_role("tab", name="test_sample")
        self.find_quote_btn = self.page.get_by_text("test_sample")
        self.account_dealer_loc = self.page.locator('#test_sample')

        # [Remaining 10+ locators redacted for confidentiality]
        '''loc for Add btn'''
        '''loc for Search btn'''
        '''loc for Account menu'''


    @property
    def check_dealer_url(self):
        dealer_url = self.page.url
        return dealer_url

    @property
    def check_default_values(self):
        add_quote = self.add_dealer_quote_loc.inner_text()
        search_quote = self.list_dealer_quote_loc.inner_text()
        account_menu = self.account_loc.inner_text()
        print(add_quote,search_quote,account_menu)
        return  add_quote,search_quote,account_menu

    @property
    def check_find_dealer_quote(self):
        if self.find_quote_box.is_visible():
            return  True
        else:
            return False

    @property
    def check_account_menu(self):
        self.account_loc.click()
        account_name = self.account_name_loc.inner_text()
        logoff = self.log_off_loc.inner_text()
        print(account_name,logoff)
        return  account_name,logoff


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 2048, "height": 1152}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test/")
        login = Deal_Portal(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(2000)
        login.check_dealer_url
        login.check_default_values
        login.check_find_dealer_quote
        login.check_account_menu