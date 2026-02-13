# Author:Yi Sun(Tim) 2024-09-12

'''Rolling Cycle Management Page'''

from playwright.sync_api import Page
from pages.admin_portal import *

class Rolling_Cycle_Management(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_rolling_cycle_management()

    def _init_locators_rolling_cycle_management(self):
        self.rolling_title_loc = self.page.locator("[name='sample']")

        '''default section'''
        self.general_settings_loc  = self.page.locator("[name='sample']")
        self.colour_cycle_settings_loc = self.page.locator("[name='sample']")
        self.temp_closed_loc = self.page.locator("[name='sample']")
        self.history_loc = self.page.locator("[name='sample']")

        '''General Settings tab'''
        self.split_doors_loc = self.page.locator("[name='sample']")
        self.lockout_settings_loc = self.page.locator("[name='sample']")
        self.default_shift_settings_loc = self.page.locator("[name='sample']")

        '''Colour Cycles Settings screen'''
        self.coil_settings_loc = self.page.locator('#sample')
        self.save_coil_btn_loc = self.page.locator('#sample')

        '''Temp closed screen'''
        self.temp_closed_cycles_loc = self.page.locator('#sample')
        self.update_cycles_btn_loc = self.page.locator('#sample')

    def go_rolling(self):
        '''Switch to Rolling Cycle Management from Account Menu'''
        self.account_loc.click()
        self.rollcycle_loc.click()
        self.rollcycle_panellift_loc.click()
        self.rolling_title_loc.wait_for(state="visible", timeout=5000)

    @property
    def check_rolling_url(self):
        '''Check the URL'''
        rolling_url = self.page.url
        print(rolling_url)
        return  rolling_url

    @property
    def check_rolling_title(self):
        '''Check the Title'''
        rolling_title = self.rolling_title_loc.inner_text()
        print(rolling_title)
        return  rolling_title

    @property
    def check_tab(self):
        '''Check each tab'''
        general_settings_title = self.general_settings_loc.inner_text()
        colour_cycles_settings_title = self.colour_cycle_settings_loc.inner_text()
        temp_closed_title = self.temp_closed_loc.inner_text()
        history_title = self.history_loc.inner_text()
        print(general_settings_title,colour_cycles_settings_title,temp_closed_title,history_title)
        return general_settings_title,colour_cycles_settings_title,temp_closed_title,history_title

    @property
    def check_general_settings(self):
        '''Check the General Settings screen'''
        split_doors = self.split_doors_loc.inner_text()
        lockout_settings = self.lockout_settings_loc.inner_text()
        default_shift_settings = self.default_shift_settings_loc.inner_text()
        print(split_doors,lockout_settings,default_shift_settings)
        return split_doors,lockout_settings,default_shift_settings

    @property
    def check_colour_cycle_settings(self):
        '''Check the Colour Cycle Settings screen'''
        self.colour_cycle_settings_loc.click()
        coil_settings = self.coil_settings_loc.inner_text()
        save_btn = self.save_coil_btn_loc.inner_text()
        print(coil_settings,save_btn)
        return coil_settings,save_btn

    @property
    def check_temp_closed(self):
        '''Check the Temp Closed  screen'''
        self.temp_closed_loc.click()
        temp_closed_cycles = self.temp_closed_cycles_loc.inner_text()
        update_cycles_btn  = self.update_cycles_btn_loc.inner_text()
        print(temp_closed_cycles,update_cycles_btn)
        return temp_closed_cycles,update_cycles_btn




if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http://test/")
        login = Rolling_Cycle_Management(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_rolling()
        # login.check_rolling_url
        login.check_rolling_title
        # login.check_tab
        # login.check_general_settings
        # login.check_colour_cycle_settings
        # login.check_temp_closed
#