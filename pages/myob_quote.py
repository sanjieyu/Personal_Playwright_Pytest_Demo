# Author:Yi Sun(Tim) 2024-11-06

'''MYOB Quotes Page'''

from playwright.sync_api  import Page
from pages.admin_portal import Admin_Page

class MYOB_Quotes(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "Quote/"
        self._init_locators_myob_quotes()

    def _init_locators_myob_quotes(self):
        self.myob_title_loc = self.page.locator("[name='title_myob']")
        self.search_btn_loc = self.page.locator('#btnMYOBQuoteSearch')
        self.searched_proposal_loc = self.page.locator('#proposalnumber')
        self.save_btn_loc = self.page.locator('#saveMYOBListData')
        self.door_status_dropdown_loc = self.page.locator("//select[contains(@id, '_status')]")

        '''client details'''
        self.client_details_loc = self.page.locator('#sample')
        self.client_name_loc = self.page.locator('#sample')
        self.contact_num_loc = self.page.locator('#sample')
        self.client_name_box_loc = self.page.locator('#ClientName')
        self.contact_num_box_loc = self.page.locator('#ContactNumber')

        '''Location'''
        self.location_loc = self.page.locator('#sample')
        self.suburb_loc = self.page.locator('#sample')
        self.site_address_loc = self.page.locator('#sample')
        self.suburb_box_loc = self.page.locator('#Suburb')
        self.site_address_box_loc = self.page.locator('#SiteAddress')

        '''Quote Information'''
        self.quote_info_loc = self.page.locator('#sample')
        self.proposal_no_loc = self.page.locator('#sample')
        self.user_loc = self.page.locator('#sample')
        self.proposal_no_box_loc = self.page.locator('#ProposalNo')
        self.user_select_loc = self.page.locator('#UserAssignedId')

    def go_myob_quotes(self):
        '''Switch to MYOB Quotes page'''
        self.list_loc.click()
        self.myob_list_loc.click()

    @property
    def check_myob_url(self):
        '''Check the URL'''
        myob_quotes_url = self.page.url
        print(myob_quotes_url)
        return myob_quotes_url

    @property
    def check_myob_title(self):
        '''Check the title'''
        myob_quotes_title = self.myob_title_loc.inner_text()
        print(myob_quotes_title)
        return myob_quotes_title

    @property
    def check_client_details(self):
        '''Check the client details section'''
        client_details = self.client_details_loc.inner_text()
        client_name = self.client_name_loc.inner_text()
        contact_num = self.contact_num_loc.inner_text()
        return client_details,client_name,contact_num

    @property
    def check_location(self):
        '''Check the Location section'''
        location = self.location_loc.inner_text()
        suburb = self.suburb_loc.inner_text()
        site_address = self.site_address_loc.inner_text()
        return location,suburb,site_address

    @property
    def check_quote_info(self):
        '''Check the Quote Information section'''
        quote_info = self.quote_info_loc.inner_text()
        proposal_no = self.proposal_no_loc.inner_text()
        user = self.user_loc.inner_text()
        return quote_info,proposal_no,user

    @property
    def check_client_name_box(self):
        '''Check the Client Name box'''
        client_name_box = self.client_name_box_loc
        if client_name_box.is_visible():
            return True
        else:
            return False

    @property
    def check_contact_num_box(self):
        '''Check the Contact Number box'''
        contact_num_box = self.contact_num_box_loc
        if contact_num_box.is_visible():
            return True
        else:
            return False

    @property
    def check_suburb_box(self):
        '''Check the Suburb box'''
        suburb_box = self.suburb_box_loc
        if suburb_box.is_visible():
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
    def check_proposal_no_box(self):
        '''Check the Proposal No box'''
        proposal_no_box = self.proposal_no_box_loc
        if proposal_no_box.is_visible():
            return True
        else:
            return False

    @property
    def check_default_user(self):
        '''Check the default value in User box'''
        user_name = self.user_select_loc.evaluate(
            "sel => sel.options[sel.selectedIndex].text"
        )
        print(user_name)
        return user_name

    @property
    def search_myob_fun(self):
        '''Check search function in MYOB by user'''
        self.user_select_loc.select_option(label="Yi_Account Sun")
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
        page.goto("http://test/")
        login = MYOB_Quotes(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_myob_quotes()
        login.check_myob_url
        login.check_myob_title
        login.check_client_details
        login.check_location
        login.check_quote_info
        login.check_client_name_box
        login.check_contact_num_box
        login.check_suburb_box
        login.check_site_address_box
        login.check_proposal_no_box
        login.check_default_user
        login.search_myob_fun
