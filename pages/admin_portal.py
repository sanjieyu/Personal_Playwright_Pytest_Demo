# Author:Yi Sun(Tim) 2024-1-22

'''Admin Portal Page'''

from playwright.sync_api import Page
from pages.login_admin import Admin_Portal

class Admin_Page(Admin_Portal):

    def __init__(self,page:Page):
        super().__init__(page)
        self.page = page
        self._init_locators()

    def _init_locators(self):
        '''loc for default values in this page'''
        self.eco_icon_loc = self.page.locator('xpath=/html/body/div[2]/div/div[1]/a/img')
        self.add_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[1]/a')
        self.list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/a')
        self.findquote_box_loc = self.page.locator('#search-quote')
        self.findquote_button_loc = self.page.locator('#btnFindQuote')
        self.findaddress_box_loc = self.page.locator('#search-address')
        self.findaddress_button_loc = self.page.locator('#btnFindAddress')
        self.findclient_box_loc = self.page.locator('#search-client')
        self.findclient_button_loc = self.page.locator('#btnFindClient')
        self.account_loc = self.page.locator("[aria-label='account']")
        self.copyright_loc = self.page.locator("[aria-label='copyright']")
        self.terms_loc = self.page.locator("[aria-label='terms']")
        self.copyright_selector = 'xpath=/html/body/footer/div/p'

        '''Add Menu'''
        self.quote_add_loc = self.page.locator("[aria-label='quote_add']")
        self.lead_add_loc = self.page.locator("[aria-label='lead_add']")
        self.account_add_loc = self.page.locator("[aria-label='account_add']")
        self.installer_add_loc = self.page.locator("[aria-label='installer_add']")

        '''List Menu'''
        self.quote_list_loc = self.page.locator('#quotelist')
        self.services_list_loc = self.page.locator('#servicelist')
        self.account_list_loc = self.page.locator('#accountlist')
        self.report_list_loc = self.page.locator('#reportlist')
        self.installer_list_loc = self.page.locator('#installerlist')
        self.myob_list_loc = self.page.locator('#myoblist')
        self.jobaccept_list_loc = self.page.locator('#jobacceptlist')
        self.onhold_list_loc = self.page.locator('#onholdlist')
        self.neworder_list_loc = self.page.locator('#neworderlist')
        self.production_list_loc = self.page.locator('#productionlist')
        self.productionWA_list_loc = self.page.locator('#walist')
        self.schedule_list_loc = self.page.locator('#schedulelist')
        self.pipeline_list_loc = self.page.locator('#pipelinelist')
        self.activepipeline_list_loc = self.page.locator('#activepipelinelist')

        '''Account Menu'''
        self.changepwd_loc = self.page.locator('#pwdchange')
        self.updateprofile_loc = self.page.locator('#profileupdate')
        self.updateemail_loc = self.page.locator('#emailupdate')
        self.usermanage_loc = self.page.locator('#usermanager')
        self.travel_area_loc = self.page.locator('#travelarea')
        self.rollcycle_loc = self.page.locator('#rollcyclepanel')
        self.rollcycle_panellift_loc = self.page.locator('#rollcycleroll')
        self.rollcycle_rollerdoors_loc = self.page.locator('#rollcycleoptilift'')
        self.rollcycle_optiliftdoors_loc = self.page.locator('#rollcycleoptiroll'')
        self.sms_loc = self.page.locator('#sms')
        self.logoff_loc = self.page.locator('#logoff')


    @property
    def getURL(self):
        '''get the url of Admin login portal'''
        self.copyright_loc.wait_for()
        print('url is:',self.page.url)
        return self.page.url

    @property
    def check_defaultmenu(self):
        '''check the default values in Admin Login page'''
        add_menu = self.add_loc.inner_text().strip()
        list_menu = self.list_loc.inner_text().strip()
        account_menu = self.account_loc.inner_text().strip()
        print(add_menu,list_menu,account_menu)
        return add_menu,list_menu,account_menu

    @property
    def check_findquote(self):
        if self.findquote_box_loc.is_visible():
            print('true')
            return True
        else:
            return False

    @property
    def check_findclient(self):
        '''check the Find Client in Admin Login page'''
        if self.findclient_box_loc.is_visible():
            print('true')
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
        print(quote_add,lead_add,account_add,install_add)
        return quote_add,lead_add,account_add,install_add

    @property
    def check_copyright(self):
        copyright = self.copyright_loc.text_content().strip()
        terms = self.terms_loc.text_content().strip()
        print(copyright,terms)
        return copyright,terms


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://cxxx.com/")
        login = Admin_Page(page)
        login.typeUserName('xxxxxx')
        login.typePassword('xxx')
        login.clicklogin()
        login.getURL
        # login.check_defaultmenu
        # login.check_findquote
        login.check_copyright


