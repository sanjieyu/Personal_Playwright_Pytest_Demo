# Author:Yi Sun(Tim) 2025-11-05

'''Add Quote Page'''

from playwright.sync_api import Page
from pages.admin_portal import Admin_Page

class Add_Quote(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "test_sample"
        self._init_locators_add_quote()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators_add_quote(self):
        self.main_page_loc = self.page.locator('#test_sample')

        '''loc for each section in this page'''
        self.proposal_details_loc = self.page.get_by_role("button", name="test_sample")
        self.contact_details_loc = self.page.get_by_text("test_sample")
        self.site_details_loc = self.page.get_by_label("test_sample")

        # [Remaining 50+ locators redacted for confidentiality]
        '''Quote Sucessfully modified popup'''
        '''loc for each element in "Proposal Details" section'''
        '''loc for each element in "Client Contact Details" section'''
        '''loc for each element in "Site Contact Details" section'''
        '''loc for Doors'''
        '''loc for Valication page'''
        '''loc for add successfully'''


    def go_addquote(self):
        '''Switch to Add Quotes from Add Menu'''
        self.add_loc.click()
        self.quote_add_loc.click()
        self.contact_details_loc.wait_for()

    @property
    def check_addquote_url(self):
        '''check the url for Add Quote page'''
        add_quote_url = self.page.url
        print(add_quote_url)
        return add_quote_url

    @property
    def check_defaulsection(self):
        '''check the default section in Add Quotes page'''
        proposal_details = self.proposal_details_loc.inner_text()
        contact_details = self.contact_details_loc.inner_text()
        site_details = self.site_details_loc.inner_text()
        doors = self.doors_loc.inner_text()
        return proposal_details, contact_details, site_details, doors

    @property
    def check_savequote_btn(self):
        '''check the save quote buton in Add Quotes page'''
        savequote_btn = self.save_quote_btn
        if savequote_btn.is_enabled():
            return True
        else:
            return False

    @property
    def check_proposal_details(self):
        '''check each description of Proplsal Details in Add Quotes page'''
        proposal_num = self.proposal_num_loc.inner_text()
        pricing_cate = self.pricing_cate_loc.inner_text()
        user_quote = self.user_quote_loc.inner_text()
        account_type = self.account_type_loc.inner_text()
        order_date = self.order_date_loc.inner_text()
        quote_status = self.quote_status_loc.inner_text()
        account_cus = self.account_customer_loc.inner_text()
        supply_type = self.supply_type_loc.inner_text()
        return proposal_num, pricing_cate, user_quote, account_type, order_date, quote_status, account_cus, supply_type

    @property
    def check_pricing_cate_value(self):
        '''check each value in "Pricing Category" list'''
        self.pricing_cate_select.click()
        pricing_value = self.pricing_cate_select.text_content()
        print(pricing_value)
        return pricing_value

    @property
    def check_default_pricing(self):
        '''check the default value in "Pricing Category" list'''
        self.pricing_cate_select.click()
        default_pricing_value = self.pricing_cate_select.evaluate("select => select.options[select.selectedIndex]."
                                                                  "textContent").strip()
        return default_pricing_value

    @property
    def check_default_user(self):
        '''check the default value in "User" list'''
        self.user_quote_select.click()
        default_user_value = (self.user_quote_select.evaluate("select => select.options[select.selectedIndex].textContent")
                              .strip())
        return default_user_value

    @property
    def check_accounttype_value(self):
        '''check each value in "Account Type" list'''
        self.account_type_select.click()
        account_type_value = self.account_type_select.text_content()
        return account_type_value

    @property
    def check_default_accounttype(self):
        '''check the default value in "Account Type" list'''
        self.account_type_select.click()
        default_accounttype_value = self.account_type_select.evaluate("select => select.options[select.selectedIndex]."
                                                                      "textContent").strip()
        return default_accounttype_value

    @property
    def check_quotestatus_value(self):
        '''check each value in "Quote Status" list'''
        self.quote_status_select.click()
        quote_status_value = self.quote_status_select.text_content()
        return quote_status_value

    @property
    def check_supplytype_default(self):
        '''check default values in "Supply Type" list'''
        default_supplytype_value = self.supply_type_select.evaluate("select => select.options[select.selectedIndex]."
                                                                    "textContent").strip()
        print(default_supplytype_value)
        return default_supplytype_value

    @property
    def check_changeto_Account(self):
        '''The "Account Customer" list should enable after select "Account" in "Account Type" list'''
        self.account_type_select.click()
        self.account_type_select.select_option(label='test_sample')
        self.account_customer_select.wait_for(state='visible')
        is_disabled = self.account_customer_select.is_disabled
        if is_disabled:
            return True
        else:
            return False

    @property
    def check_add_quote_success(self):
        '''check Add Quote Successfully'''
        self.supply_type_select.select_option(index=1)
        self.contact_email_box.fill('test_sample')
        self.account_type_select.select_option(label="test_sample")
        self.page.wait_for_timeout(2000)
        self.account_customer_btn.click()
        self.propertygroup_customer_loc.click()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.save_quote_btn.click()
        self.page.wait_for_timeout(2000)
        self.page.evaluate("window.scrollTo(0, 0)")
        self.quote_success_created_loc.wait_for(state='visible')
        quote_success_created = self.quote_success_created_loc.inner_text()
        return quote_success_created


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test_sample")
        login = Add_Quote(page)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clicklogin()
        login.go_addquote()
        # login.check_addquote_url
        # login.check_defaulsection
        # login.check_proposal_details
        # login.check_pricing_cate_value
        # login.check_default_pricing
        # login.check_default_pricing
        login.check_supplytype_value
        # login.check_default_quotestatus



































