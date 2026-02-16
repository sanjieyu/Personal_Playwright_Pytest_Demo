# Author:Yi Sun(Tim) 2024-11-27

'''Add Service Page'''

from playwright.sync_api import Page
from pages.admin_portal import Admin_Page

class Add_Service(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "test_sample"
        self._init_locators_add_service()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators_add_service(self):
        self.search_service_title_loc = self.page.locator('#test_sample')
        self.search_service_loc = self.page.get_by_role("button", name="test_sample")
        self.add_new_service_btn = self.page.get_by_text("test_sample")
        self.success_confirm_btn = self.page.get_by_label("test_sample")

        # [Remaining 50+ locators redacted for confidentiality]
        '''loc for each section in this page'''
        '''loc for each element in "Doors" section"'''
        '''loc for each element in "Service Details" section"'''
        '''loc for each element in "Site Contact Details" section"'''


    def go_addservice(self):
        '''Switch to Add Service from LIST Menu'''
        self.list_loc.click()
        self.services_list_loc.hover()
        self.search_service_loc.click()
        self.add_new_service_btn.click(timeout=3000)

    @property
    def check_add_service_url(self):
        '''check the url for Add Service page'''
        add_service_url = self.page.url
        return add_service_url

    @property
    def check_sections(self):
        '''check each section in Add Service page'''
        doors_section = self.doors_section_loc.inner_text()
        service_details = self.service_details_loc.inner_text()
        site_contact_details = self.site_contact_details_loc.inner_text()
        service_items = self.service_item_loc.inner_text()
        service_documents = self.service_documents_loc.inner_text()
        return doors_section, service_details, site_contact_details, service_items, service_documents

    @property
    def check_buttons(self):
        '''check each button in Add Service page'''
        back_service = self.back_service_btn.inner_text()
        save_service = self.save_service_btn.inner_text()
        return back_service

    @property
    def check_addition_box(self):
        '''check the Additional Door Infomation box in "Doors" section'''
        additional_info_box = self.additional_info_box
        if additional_info_box.is_visible():
            return True
        else:
            return False

    def add_service_func(self):
        '''put details and add a new service'''
        self.door_type_select.select_option(label='test_sample')
        self.additional_info_box.fill('test_sample')
        self.service_type_select.select_option(label='test_sample')
        self.service_area_select.select_option(label='test_sample')
        self.client_name_box.fill('test_sample')
        self.contact_address_box.fill('test_sample')
        self.contact_suburbb_box.fill('test_sample')
        self.contact_mobile_box.fill('test_sample')

    def save_service(self):
        ''''click the save service'''
        self.save_service_btn.click()
        self.success_confirm_btn.click()


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440},ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test_sample/")
        login = Add_Service(page)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_addservice()
        # login.check_add_service_url
        # login.check_sections
        # login.check_buttons
        # login.check_doors_section
        # login.check_addition_box
        # login.check_service_details
        login.add_service_func()
        login.save_service()

