# Author:Yi Sun(Tim) 2024-11-06

'''Production Page'''

from playwright.sync_api import Page,expect
from UIModule.admin_portal import Admin_Page


class Production(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_production()

    def _init_locators_production(self):
        self.production_title_loc = self.page.locator('#sample')

        '''loc for each section in this page'''
        self.roller_doors_loc = self.page.locator('#sample')
        self.panel_lift_loc = self.page.locator('#sample')
        self.insulated_doors_loc = self.page.locator('#sample')
        self.custom_doors_loc = self.page.locator('#sample')
        self.roller_shutters_loc = self.page.locator('#sample')
        self.all_doors_loc = self.page.locator('#sample')

    def go_production(self):
        '''Switch to Production from LIST Menu'''
        self.list_loc.click()
        self.production_list_loc.click()

    @property
    def check_production_url(self):
        '''check the url for Production page'''
        production_url = self.page.url
        print(production_url)
        return production_url

    @property
    def check_production_title(self):
        '''check the title for Production page'''
        production_title = self.production_title_loc.inner_text()
        print(production_title)
        return production_title
    @property
    def check_production_section(self):
        '''check each section in Production page'''
        roller_doors = self.roller_doors_loc.inner_text()
        panel_lift_safe = self.panel_lift_loc.inner_text()
        insulated_doors = self.insulated_doors_loc.inner_text()
        custom_doors = self.custom_doors_loc.inner_text()
        roller_shutters = self.roller_shutters_loc.inner_text()
        all_doors = self.all_doors_loc.inner_text()
        print (roller_doors,panel_lift_safe,insulated_doors,custom_doors,roller_shutters,all_doors)
        return roller_doors,panel_lift_safe,insulated_doors,custom_doors,roller_shutters,all_doors

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http://test/")
        login = Production(page)
        # 登录
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_production()
        login.check_production_url
        login.check_production_section
        login.check_production_title