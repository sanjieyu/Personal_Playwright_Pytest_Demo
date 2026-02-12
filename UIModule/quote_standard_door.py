# Author:Yi Sun(Tim) 2024-11-03

'''Add a New Quote with a Standard Door'''

from playwright.sync_api import Page,expect
from UIModule.add_standar_door import Add_Standard_Door
from UIModule.add_quote import Add_Quote

class Quote_Standard_Door(Add_Standard_Door):

    def __init__(self,page:Page):
        super().__init__(page)
        self.page = page
        self.add_quote1 = Add_Quote(self.page)
        self._init_locators_quote_standard_door()

    def _init_locators_quote_standard_door(self):
        self.proposal_number_loc = self.page.locator('#ProposalNo')   #get the proposal number for the edit box
        self.find_quote_input = self.page.locator('#search-quote')
        self.find_quote_btn = self.page.locator('#search-btn')
        self.searched_proposal_no_loc = self.page.locator( "a.dark-text[href^='/Quote/Edit/']")
        self.searched_door_no_loc = self.page.locator("xpath=//span[text()='Door 1(A1)']")
        self.searched_door_status_loc = self.page.locator("xpath=//span[text()='Quote']")

    def add_door_fun(self):
        self.add_quote1.go_addquote()
        self.go_addstandarddoor()
        self.add_door()
        self.page.wait_for_load_state("networkidle")
        self.add_quote1.check_add_quote_success

    @property
    def get_proposal_number(self):
        proposal_number = self.proposal_number_loc.input_value()
        print(f'number is: {proposal_number}')
        return proposal_number

    def search_new_quote(self,prop_no):
        self.page.reload()
        self.find_quote_input.fill(prop_no)
        self.find_quote_btn.click()

    @property
    def verify_new_quote(self):
        searched_proposal_no = self.searched_proposal_no_loc.inner_text()
        searched_door_no = self.searched_door_no_loc.inner_text()
        searched_door_status = self.searched_door_status_loc.inner_text()
        print(searched_door_no,searched_door_status)
        return searched_door_no,searched_door_status

    def change_to_cash(self):
        '''Check the payment Net percentage in Payment section,should be "100%"'''
        self.add_quote1.change_quote_detail()


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 2048, "height": 1152}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http://test")
        login = Quote_Standard_Door(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        login.add_door_fun()
        prop_no = login.get_proposal_number
        login.search_new_quote(prop_no)
        login.verify_new_quote