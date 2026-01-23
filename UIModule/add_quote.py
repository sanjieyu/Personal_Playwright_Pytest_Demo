# Author:Yi Sun(Tim) 2025-11-05

'''Add Quote Page'''

from playwright.sync_api import Page,expect
from UIModule.admin_portal import Admin_Page

class Add_Quote(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_add_quote()

    def _init_locators_add_quote(self):
        self.main_page_loc = self.page.locator('xpath=//*[@id="main"]')

        '''loc for each section in this page'''
        self.proposal_details_loc = self.page.locator("[name='proposalinfo']")
        self.contact_details_loc = self.page.locator("[name='contactinfo']")
        self.site_details_loc = self.page.locator("[name='siteinfo']")
        self.doors_loc = self.page.locator("[aria-label='doors']")
        self.add_door_btn = self.page.locator('#btnAddQuote')
        self.save_quote_btn = self.page.locator('#btnSaveQuote')
        self.proceed_quote_btn = self.page.locator('#btnProceedFinal')

        '''Quote Sucessfully modified popup'''
        self.proceed_ok_btn_loc = self.page.locator('#btnProceedOk')
        self.save_ok_btn_loc = self.page.locator('#btnSaveOk')

        '''loc for each element in "Proposal Details" section'''
        self.proposal_num_loc = self.page.locator("[name='proposalnum']")
        self.pricing_cate_loc = self.page.locator("[name='pricingcate']")
        self.user_quote_loc = self.page.locator("[name='userquote']")
        self.account_type_loc = self.page.locator("[name='accounttype']")
        self.order_date_loc = self.page.locator("[name='orderdate']")
        self.quote_status_loc = self.page.locator("[name='quotestatus']")
        self.account_customer_loc = self.page.locator("[name='accountname']")
        self.supply_type_loc = self.page.locator("[name='supplytype']")
        self.proplsal_num_box = self.page.locator('#ProposalNo')
        self.pricing_cate_select = self.page.locator('#PricingCategoryId')
        self.user_quote_select = self.page.locator('#UserAssignedId')
        self.account_type_select = self.page.locator('#PaymentTypeId')
        self.order_date_select = self.page.locator('#OrderDate')
        self.quote_status_select = self.page.locator( '#QuoteStatusId')
        self.account_customer_btn = self.page.locator("#btnAccountk")
        self.propertygroup_customer_loc = self.page.locator("[name='propertygroup']")
        self.account_customer_select1 = self.page.locator('#account_customer_list_part')
        self.account_customer_select = self.page.locator('xpath=//*[@id="accountCustomerData"]/div/div[1]/span')
        self.supply_type_select = self.page.locator('#SupplyTypeId')

        '''loc for each element in "Client Contact Details" section'''
        self.client_contact_details_loc = self.page.locator('xpath=//*[@id="clientContact"]/div/div[2]/span')
        self.client_name_loc = self.page.locator('xpath=//*[@id="clientName"]/div/div[3]/span')
        self.customer_purchase_order_loc = self.page.locator('xpath=//*[@id="purchaseOrder"]/div/div[4]/span')
        self.contact_name_loc = self.page.locator('xpath=//*[@id="contactName"]/div/div[5]/span')
        self.contact_mobile_loc = self.page.locator('xpath=//*[@id="contactMobile"]/div/div[6]/span')
        self.contact_email_loc = self.page.locator('xpath=//*[@id="contactEmail"]/div/div[7]/span')
        self.contact_address_loc = self.page.locator('xpath=//*[@id="contactAddress"]/div/div[8]/span')
        self.contact_suburb_loc = self.page.locator('xpath=//*[@id="contactSuburb"]/div/div[9]/span')
        self.contact_postcode_loc = self.page.locator('xpath=//*[@id="contactPostcode"]/div/div[10]/span')

        self.client_name_box = self.page.locator( '#ClientName')
        self.order_num_box = self.page.locator( '#ClientPurchaseOrderNumber')
        self.contact_name_box = self.page.locator('#ContactName')
        self.contact_mobile_box = self.page.locator('#ContactMobile')
        self.contact_email_box = self.page.locator('#ContactEmail')
        self.contact_address_box = self.page.locator('#ContactAddress')
        self.contact_suburb_box = self.page.locator('#ContactSuburb')
        self.contact_postcode_box = self.page.locator('#ContactPostcode')

        '''loc for each element in "Site Contact Details" section'''
        self.site_contact_details_loc = self.page.locator('xpath=//*[@id="siteContact"]/div/div[2]/span')
        self.copy_client_details = self.page.locator('xpath=//*[@id="siteDetail"]/div/div[3]/span')
        self.site_contact_name = self.page.locator('xpath=//*[@id="siteName"]/div/div[4]/span')
        self.site_phone_loc = self.page.locator('xpath=//*[@id="siteMobile"]/div/div[5]/span')
        self.site_email_loc = self.page.locator('xpath=//*[@id="sitetEmail"]/div/div[6]/span')
        self.site_address_loc = self.page.locator('xpath=//*[@id="siteAddress"]/div/div[7]/span')
        self.site_suburb_loc = self.page.locator('xpath=//*[@id="siteSuburb"]/div/div[9]/span')
        self.site_postcode_loc = self.page.locator('xpath=//*[@id="sitePostcode"]/div/div[10]/span')

        self.copy_checkbox_loc = self.page.locator('#chkcopyclientdetails')
        self.site_contactname_box = self.page.locator( '#SiteContactName')
        self.site_phone_box = self.page.locator('#SitePhone')
        self.site_email_box = self.page.locator('#SiteEmail')
        self.site_address_box = self.page.locator( '#SiteAddress')
        self.site_suburb_box = self.page.locator('#SiteSuburb')
        self.site_postcode_box = self.page.locator( '#SitePostcode')

        '''loc for Doors'''
        self.add_door_btn = self.page.locator('#btnAddDoor')
        self.add_door_menu = self.page.locator('.dropdown-menu')    # 用class name定位，前面加.

        '''loc for Valication page'''
        self.validation_error_loc = self.page.locator( 'xpath=/html/body/div[3]/div[2]/div[7]/div/div/div[1]/h4')
        self.validation_1_loc = self.page.locator( 'xpath=/html/body/div[3]/div[2]/div[7]/div/div/div[1]/div[1]/ul/li[1]')
        self.validation_2_loc = self.page.locator( 'xpath=/html/body/div[3]/div[2]/div[7]/div/div/div[1]/div[1]/ul/li[2]')
        self.validation_ok_btn = self.page.locator('#btnCommentAdd') #用ID定位，加一个‘#’

        '''loc for add successfully'''
        self.quote_success_created_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[1]/div/form/div/h1[1]/'
                                                           'span/b')
        self.success_btn_loc = self.page.locator('xpath=/html/body/div[86]/div/div[6]/button[1]')

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
        print(proposal_details, contact_details, site_details, doors)
        return proposal_details, contact_details, site_details, doors

    @property
    def check_savequote_btn(self):
        '''check the save quote buton in Add Quotes page'''
        savequote_btn = self.save_quote_btn
        if savequote_btn.is_enabled():
            print('enabled')
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
        print(proposal_num, pricing_cate, user_quote, account_type, order_date, quote_status, account_cus, supply_type)
        return proposal_num, pricing_cate, user_quote, account_type, order_date, quote_status, account_cus, supply_type

    @property
    def check_pricing_cate_value(self):
        '''check each value in "Pricing Category" list'''
        self.pricing_cate_select.click()
        pricing_value = self.pricing_cate_select.text_content()  #取dropdown list的里面的各项
        print(pricing_value)
        return pricing_value

    @property
    def check_default_pricing(self):
        '''check the default value in "Pricing Category" list'''
        self.pricing_cate_select.click()
        default_pricing_value = self.pricing_cate_select.evaluate("select => select.options[select.selectedIndex]."
                                                                  "textContent").strip()
        print(default_pricing_value)
        return default_pricing_value

    @property
    def check_default_user(self):
        '''check the default value in "User" list'''
        self.user_quote_select.click()
        default_user_value = (self.user_quote_select.evaluate("select => select.options[select.selectedIndex].textContent")
                              .strip())
        print(default_user_value)
        return default_user_value

    @property
    def check_accounttype_value(self):
        '''check each value in "Account Type" list'''
        self.account_type_select.click()
        account_type_value = self.account_type_select.text_content()
        print(account_type_value)
        return account_type_value

    @property
    def check_default_accounttype(self):
        '''check the default value in "Account Type" list'''
        self.account_type_select.click()
        default_accounttype_value = self.account_type_select.evaluate("select => select.options[select.selectedIndex]."
                                                                      "textContent").strip()
        print(default_accounttype_value)
        return default_accounttype_value

    @property
    def check_quotestatus_value(self):
        '''check each value in "Quote Status" list'''
        self.quote_status_select.click()
        quote_status_value = self.quote_status_select.text_content()
        print(quote_status_value)
        return quote_status_value

    @property
    def check_default_quotestatus(self):
        '''check the default value in "Quote Status" list'''
        self.quote_status_select.click()
        default_quotestatus_value = self.quote_status_select.evaluate("select => select.options[select.selectedIndex]."
                                                                      "textContent").strip()
        print(default_quotestatus_value)
        return default_quotestatus_value

    @property
    def check_supplytype_value(self):
        '''check all values in "Supply Type" list'''
        self.supply_type_select.click()
        supplytype_value = self.supply_type_select.text_content()
        print(supplytype_value)
        return supplytype_value

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
        self.account_type_select.select_option(label='Account')
        self.account_customer_select.wait_for(state='visible')
        is_disabled = self.account_customer_select.is_disabled
        if is_disabled:
            print("Account Customer is disabled")
            return True
        else:
            print("Account Customer is enabled")
            return False

    @property
    def check_add_quote_success(self):
        '''check Add Quote Successfully'''
        self.supply_type_select.select_option(index=1)
        self.contact_email_box.fill('ysun@ecogaragedoors.com.au')
        self.account_type_select.select_option(label="Account")
        self.page.wait_for_timeout(2000)
        self.account_customer_btn.click()
        self.propertygroup_customer_loc.click()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.save_quote_btn.click()
        self.page.wait_for_timeout(2000)
        self.page.evaluate("window.scrollTo(0, 0)")
        self.quote_success_created_loc.wait_for(state='visible')
        quote_success_created = self.quote_success_created_loc.inner_text()
        print(quote_success_created)
        return quote_success_created


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://xxx.com/")
        login = Add_Quote(page)
        # 登录
        login.typeUserName('xxxx')
        login.typePassword('xxxx')
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



































