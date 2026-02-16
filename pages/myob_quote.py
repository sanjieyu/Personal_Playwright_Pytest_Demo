# Author:Yi Sun(Tim) 2024-11-06

'''MYOB Quotes Page'''

from playwright.sync_api  import Page
from pages.admin_portal import Admin_Page

class MYOB_Quotes(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "test_sample/"
        self._init_locators_myob_quotes()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators_myob_quotes(self):
        self.myob_title_loc = self.page.locator('#test_sample')
        self.search_btn_loc = self.page.get_by_role("button", name="test_sample")
        self.searched_proposal_loc = self.page.get_by_text("test_sample")
        self.save_btn_loc = self.page.get_by_label("test_sample")

        # [Remaining 20+ locators redacted for confidentiality]
        '''client details'''
        '''Location'''
        '''Quote Information'''

    def go_myob_quotes(self):
        '''Switch to MYOB Quotes page'''
        self.list_loc.click()
        self.myob_list_loc.click()

    @property
    def check_myob_url(self):
        '''Check the URL'''
        myob_quotes_url = self.page.url
        return myob_quotes_url

    @property
    def check_myob_title(self):
        '''Check the title'''
        myob_quotes_title = self.myob_title_loc.inner_text()
        return myob_quotes_title

    @property
    def check_client_details(self):
        '''Check the client details section'''
        client_details = self.client_details_loc.inner_text()
        client_name = self.client_name_loc.inner_text()
        contact_num = self.contact_num_loc.inner_text()
        return client_details,client_name,contact_num

    @property
    def check_client_name_box(self):
        '''Check the Client Name box'''
        client_name_box = self.client_name_box_loc
        if client_name_box.is_visible():
            return True
        else:
            return False

    @property
    def check_site_address_box(self):
        '''Check the Site Address box'''
        site_address_box = self.site_address_box_loc
        if site_address_box.is_visible():
            return True
        else:
            return False


    @property
    def check_default_user(self):
        '''Check the default value in User box'''
        user_name = self.user_select_loc.evaluate(
            "sel => sel.options[sel.selectedIndex].text"
        )
        return user_name

    @property
    def search_myob_fun(self):
        '''Check search function in MYOB by user'''
        self.user_select_loc.select_option(label="test_sample")
        search_btn_des = self.search_btn_loc.inner_text()
        self.search_btn_loc.click()
        searched_result = self.searched_proposal_loc.inner_text()
        print(search_btn_des,searched_result)
        return searched_result

    def input_proposal(self,prop_no):
        '''Used by change_quote_status module'''
        self.proposal_no_box_loc.fill(prop_no)
        self.page.wait_for_timeout(2000)
        self.search_btn_loc.click()
        self.page.wait_for_load_state("networkidle")

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http://test_sample/")
        login = MYOB_Quotes(page)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_myob_quotes()
