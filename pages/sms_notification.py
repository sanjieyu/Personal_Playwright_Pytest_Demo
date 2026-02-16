# Author:Yi Sun(Tim) 2024-05-21

'''SMS Notification Page'''

from playwright.sync_api import Page
from pages.admin_portal import *

class SMS_Notification(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_sms()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators_sms(self):
        self.sms_title_loc = self.page.locator('#test_sample')
        self.apikey_box_loc = self.page.get_by_text("test_sample")
        self.mlb_tab_loc = self.page.get_by_role("tab", name="test_sample")

        # [Remaining 10+ locators redacted for confidentiality]
        '''mlb install tab'''

    def go_sms_notification(self):
        '''Switch to SMS Notification Page from Account Menu'''
        self.account_loc.click()
        self.sms_loc.click()
        self.sms_title_loc.wait_for(state="visible", timeout=5000)

    @property
    def check_sms_url(self):
        '''Check the URL'''
        sms_url = self.page.url
        return  sms_url

    @property
    def check_sms_title(self):
        '''Check the Title'''
        sms_title = self.sms_title_loc.inner_text()
        return  sms_title

    @property
    def check_default_value(self):
        '''Check the default value'''
        apikey_value = self.apikey_box_loc.input_value(timeout=1000)
        pwd_value = self.pwd_box_loc.input_value(timeout=1000)
        from_value = self.from_box_loc.input_value(timeout=1000)
        return apikey_value,pwd_value,from_value

    @property
    def check_apikey_disable(self):
        '''Check the apikey box status'''
        self.page.wait_for_load_state("networkidle")
        is_disabled = self.apikey_box_loc.evaluate("el => el.disabled")
        return not is_disabled

    @property
    def check_apikey_disable_same(self):
        '''Check the apikey box status'''
        try:
            self.apikey_box_loc.wait_for(state="attached")
            self.page.wait_for_timeout(1000)
            html_content = self.apikey_box_loc.evaluate("el => el.outerHTML")
            return self.apikey_box_loc.is_enabled()
        except:
            return False

    @property
    def check_pwd_disable(self):
        '''Check the pwd box status'''
        return self.pwd_box_loc.is_editable()

    @property
    def check_from_disable(self):
        '''Check the from box status'''
        return  self.from_box_loc.is_editable()

    @property
    def check_tab(self):
        '''Check the tab screen'''
        mlb_tab = self.mlb_tab_loc.inner_text()
        syd_tab = self.syd_tab_loc.inner_text()
        return mlb_tab,syd_tab

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http://test/")
        login = SMS_Notification(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_sms_notification()
        # login.check_sms_url
        # login.check_sms_title
        # login.check_default_value
        login.check_apikey_disable
        # login.check_pwd_disable
        # login.check_from_disable
        # login.check_tab
        # login.check_mlb_enter
        # login.check_mlb_rollforming
        # login.check_mlb_qcpass