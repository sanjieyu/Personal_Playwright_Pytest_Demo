# Author:Yi Sun(Tim) 2024-1-22

'''Admin Portal Page'''

from playwright.sync_api import Page
from pages.login_admin import Admin_Portal

class Admin_Page(Admin_Portal):

    def __init__(self,page:Page):
        super().__init__(page)
        self.page = page
        self._init_locators()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators(self):
        '''loc for default values in this page'''
        self.eco_icon_loc = self.page.locator('test_sample')
        self.add_loc = self.page.get_by_role("button", name="test_sample")
        self.list_loc = self.page.get_by_text("test_sample")
        self.findquote_box_loc = self.page.get_by_label("test_sample")

        # [Remaining 20+ locators redacted for confidentiality]
        '''Add Menu'''
        '''List Menu'''
        '''Account Menu'''

    @property
    def getURL(self):
        '''get the url of Admin login portal'''
        self.copyright_loc.wait_for()
        return self.page.url

    @property
    def check_defaultmenu(self):
        '''check the default values in Admin Login page'''
        add_menu = self.add_loc.inner_text().strip()
        list_menu = self.list_loc.inner_text().strip()
        account_menu = self.account_loc.inner_text().strip()
        return add_menu,list_menu,account_menu

    @property
    def check_findquote(self):
        if self.findquote_box_loc.is_visible():
            return True
        else:
            return False

    @property
    def check_findclient(self):
        '''check the Find Client in Admin Login page'''
        if self.findclient_box_loc.is_visible():
            return True
        else:
            return False

    @property
    def add_menu(self):
        self.add_loc.click()
        quote_add = self.quote_add_loc.inner_text().strip()
        lead_add = self.lead_add_loc.inner_text().strip()
        account_add = self.account_add_loc.inner_text().strip()
        install_add = self.installer_add_loc.inner_text().strip()
        return quote_add,lead_add,account_add,install_add

    @property
    def check_copyright(self):
        copyright = self.copyright_loc.text_content().strip()
        terms = self.terms_loc.text_content().strip()
        return copyright,terms


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test_sample/")
        login = Admin_Page(page)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clicklogin()
        login.getURL
        # login.check_defaultmenu
        # login.check_findquote
        login.check_copyright


