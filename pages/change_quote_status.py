# Author:Yi Sun(Tim) 2024-11-09

'''Change Quote Status'''

from playwright.sync_api import Page
from pages.login_admin import Admin_Portal
from pages.panel_left_safe import Panel_lift_Safe
from pages.quote_standard_door import Quote_Standard_Door
from pages.production import Production
from pages.myob_quote import MYOB_Quotes


class Change_Quote_Status(Admin_Portal):

    def __init__(self,page:Page):
        super().__init__(page)
        self.page = page
        self.url_path = "test_sample/"
        self.go_production = Production(self.page)
        self.go_panel_lift_safe = Panel_lift_Safe(self.page)
        self.add_quote_door = Quote_Standard_Door(self.page)
        self.go_myob= MYOB_Quotes(self.page)
        self.proposal_number = None
        self._init_locators_change_quote_status()

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    def _init_locators_change_quote_status(self):
        '''loc for the status dropdown'''
        self.setting_btn_loc = self.page.locator('.test_sample')
        self.status_loc = self.page.locator('#test_sample')
        self.proposal_num_myob_loc = self.page.get_by_text("test_sample")

        # [Remaining 10+ locators redacted for confidentiality]
        '''The search result by proposal number in MYOB screen'''
        '''loc for the elements in Status page'''

    def goto_status_page(self):
        '''Add a new quote with door, then search this new quote'''
        self.add_quote_door.add_door_fun()
        self.proposal_number  = self.add_quote_door.get_proposal_number
        self.add_quote_door.search_new_quote(self.proposal_number )
        self.setting_btn_loc.click()
        self.status_loc.click()

    def change_status_new_order(self):
        '''Change the status to New Order for this new quote'''
        self.status_select_loc.select_option(label="test_sample")
        self.date_box_loc.click()
        self.date_box_loc.fill("30/12/2024")
        self.save_btn_loc.click()

    def change_status_order(self):
        '''Change the status to MYOB - Ready for this new quote'''
        self.status_select_loc.click()
        self.page.wait_for_timeout(500)
        self.status_select_loc.focus()
        self.page.keyboard.type("test_sample")
        self.page.keyboard.press("Enter")
        self.date_box_loc.click()
        self.date_box_loc.fill("02/12/2024")
        self.save_btn_loc.click()
        self.page.wait_for_load_state("networkidle")

    def check_myob_status(self):
        '''Check the quote status in MYOB Page'''
        self.go_myob.go_myob_quotes()
        if self.proposal_number:
            self.go_myob.input_proposal(self.proposal_number)
            searched_result = self.proposal_num_myob_loc.inner_text().strip()
            if searched_result == self.proposal_number.strip():
                return  True
            else:
                return False
        else:
            print("Proposal number is not available.")
            return False

    def check_order_status(self):
        '''Change the quote status from MYOB Ready to Order'''
        self.page.wait_for_timeout(1000)
        status_dropdown_loc = self.go_myob.door_status_dropdown_loc
        save_btn_loc = self.go_myob.save_btn_loc
        status_dropdown_loc.select_option(label="test_sample")
        save_btn_loc.click()    # change to order status
        self.page.wait_for_timeout(1000)
        self.go_production.go_production()
        self.go_panel_lift_safe.go_panel_lift_safe()
        first_order = self.go_panel_lift_safe.get_first_orderid
        if first_order  == self.proposal_number + "test_sample":
            return True
        else:
            return False

    def check_rollforming_status(self):
        '''Change the quote status from Order to Rollforming'''
        search_order_btn = self.go_panel_lift_safe.search_order_box_loc
        search_order_btn.fill(self.proposal_number + "test_sample")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(3000)
        searched_order_statusbox_loc = self.page.locator(f'[name="{self.proposal_number}A1"]')
        searched_order_statusbox_loc.select_option(value='9')
        save_changes_order_btn = self.go_panel_lift_safe.save_changes_order_btn_loc
        save_changes_order_btn.click()
        self.page.wait_for_timeout(2000)
        self.add_quote_door.search_new_quote(self.proposal_number)  # searched this quote from Find a quote box
        quote_status_loc = self.page.locator("[aria-label='doors']")
        quote_status = quote_status_loc.inner_text()
        if quote_status == 'In test_sample - test_sample':
            return True
        else:
            return False

    def check_rollforming_size(self):
        '''Check the Actual size of the door on Rollforming screen'''
        self.production.go_production()
        self.production_panel.go_panel_lift_safe()
        self.production_panel.go_rollforming()
        search_quote_box = self.production_panel.search_job_box
        search_quote_btn = self.production_panel.search_job_btn
        search_quote_box.fill(self.proposal_number)
        search_quote_btn.click()
        searched_job = self.production_panel.searched_result_job_loc
        searched_job.click()

if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http://test_sample")
        login = Change_Quote_Status(page)
        login.typeUserName('test_sample')
        login.typePassword('test_sample')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.goto_status_page()
        login.change_status_order()
        login.check_myob_status()
        login.check_order_status()
        login.check_rollforming_status()

