# Author:Yi Sun(Tim) 2024-10-30

'''Add a Standard Door'''

from playwright.sync_api import Page
from pages.standard_door import *

class Add_Standard_Door(Standard_Door):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "Quote/Creat"
        self._init_locators_add_standard_door()

    def _init_locators_add_standard_door(self):
        self.new_door_page_loc = self.page.locator('#quickDoorAddModalBody')
        self.new_door_title= self.page.locator('xpath=//*[@id="door"]/div/div[2]/span')
        self.new_door_duplicate = self.page.locator( '.duplicat')
        self.new_door_delete = self.page.locator('#delete')

        '''loc for validation'''
        self.validation_msgbox_loc = self.page.locator('#doorerrormsgs_body')

    '''Check the input validateiong'''
    @property
    def validation_input(self):
        self.new_door_page_loc.scroll_into_view_if_needed()
        self.add_standarddoor_btn.click()
        msg_error = self.validation_msgbox_loc.inner_text()
        print(msg_error)
        return msg_error

    '''for wall_button class'''
    def add_door_opener(self):
        self.door_type_select.select_option(label='Panel Lift-Safe')
        self.opener_select.select_option(label='ECO1000N Belt Drive')

    '''Input the necesary details for a door'''
    def add_door(self):
        self.install_type_select.select_option(label='Commercial Cat 1')
        self.door_type_select.select_option(label='Panel Lift-Safe')
        self.design_select.select_option(label='Classic panel')
        self.colour_category_select.select_option(label='ColorBond')
        self.door_colour_select.select_option(label='Monument')
        self.door_finish_select.select_option(label='Woodgrain Texture')
        self.opensize_lh_select.clear()
        self.opensize_lh_select.fill('2000')
        self.opensize_rh_select.clear()
        self.opensize_rh_select.fill('2000')
        self.opensize_width_select.clear()
        self.opensize_width_select.fill('2500')
        self.sr_left_select.clear()
        self.sr_left_select.fill('200')
        self.hr_select.clear()
        self.hr_select.fill('300')
        self.sr_right_select.clear()
        self.sr_right_select.fill('200')
        self.opener_select.select_option(label='Use Existing')
        self.new_door_page_loc.scroll_into_view_if_needed()
        self.add_standarddoor_btn.click()

    @property
    def new_added_door(self):
        door_title = self.new_door_title.inner_text()
        print(door_title)
        return door_title

    @property
    def duplicate_btn(self):
        if self.new_door_duplicate.is_visible():
            return True
        else:
            return False
    @property
    def delete_btn(self):
        if self.new_door_delete.is_visible():
            return True
        else:
            return False
if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 2048, "height": 1152}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test")
        login = Add_Standard_Door(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(2000)
        login.go_addquote()
        login.go_addstandarddoor()
        login.validation_input
        login.add_door()
        login.new_added_door
        login.duplicate_btn
        login.delete_btn



