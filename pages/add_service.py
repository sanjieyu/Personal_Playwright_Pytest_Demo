# Author:Yi Sun(Tim) 2024-11-27

'''Add Service Page'''

from playwright.sync_api import Page
from pages.admin_portal import Admin_Page

class Add_Service(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "Service/Create"
        self._init_locators_add_service()

    def _init_locators_add_service(self):
        self.search_service_title_loc = self.page.locator('xpath=//*[@id="serviceTitle"]/div/div[1]/span')
        self.search_service_loc = self.page.locator('xpath=//*[@id="serviceId"]/div/div[2]/span')
        self.add_new_service_btn = self.page.locator('#btnServiceAdd')
        self.success_confirm_btn = self.page.locator('#btnServiceConfirm')

        '''loc for each section in this page'''
        self.doors_section_loc = self.page.locator( "[aria-label='doorsection']")
        self.service_details_loc = self.page.locator("[aria-label='servicedetails']")
        self.site_contact_details_loc = self.page.locator( "[aria-label='sitecontact']")
        self.service_item_loc = self.page.locator( "[aria-label='serviceitem']")
        self.service_documents_loc = self.page.locator("[aria-label='document']")
        self.back_service_btn = self.page.locator('#btnBackToQuote')
        self.save_service_btn = self.page.locator( '#btnSaveService')
        self.add_service_item_btn = self.page.locator( '#btnServiceItem')
        self.add_attachement_btn_loc = self.page.locator( '#servicenewfiles')

        '''loc for each element in "Doors" section"'''
        self.door_type_loc = self.page.locator("[aria-label='doortype']")
        self.door_type_select = self.page.locator( '#serviceDoorType')
        self.additional_info_loc = self.page.locator("[aria-label='additionalinfo']")
        self.additional_info_box = self.page.locator('#serviceAdditionalDoorInfo')

        '''loc for each element in "Service Details" section"'''
        self.service_type_loc = self.page.locator("[aria-label='servicetype']")
        self.service_type_select = self.page.locator('#serviceSupplyType')
        self.service_area_loc = self.page.locator( "[aria-label='servicearea']")
        self.service_area_select = self.page.locator('#serviceTypeValue')
        self.service_status_loc = self.page.locator("[aria-label='status']")
        self.service_status_select = self.page.locator('#serviceStatusId')
        self.invoice_no_loc = self.page.locator("[aria-label='invoice']")
        self.invoice_no_box = self.page.locator('#serviceInvoiceNo')
        self.account_type_loc = self.page.locator("[aria-label='accountype']")
        self.account_type_select = self.page.locator('#servicePaymentTypeId')
        self.account_customer_loc = self.page.locator( "[aria-label='accountcustomer']")
        self.account_customer_select = self.page.locator( '#serviceAccountCustomer')
        self.order_date_loc = self.page.locator("[aria-label='orderdate']")
        self.order_date_filter = self.page.locator('#serviceOrderDate')
        self.service_date_loc = self.page.locator( "[aria-label='servicedate']")
        self.service_date_filter = self.page.locator( '#serviceServiceDate')
        self.customer_po_loc = self.page.locator("[aria-label='customerpo']")
        self.customer_po_box = self.page.locator( '#serviceCustomerPO')
        self.user_loc = self.page.locator("[aria-label='userid']")
        self.user_select = self.page.locator( '#serviceUserAssigned')
        self.service_tech_loc = self.page.locator("[aria-label='servicetech']")
        self.service_tech_select = self.page.locator('#serviceInstaller')
        self.service_tech_name_loc = self.page.locator("[aria-label='techname']")
        self.service_tech_name_box = self.page.locator('#serviceTechName')
        self.description_loc = self.page.locator("[aria-label='description']")
        self.description_box = self.page.locator('#serviceDescription')

        '''loc for each element in "Site Contact Details" section"'''
        self.client_name_box = self.page.locator( '#ClientNameTextBox')
        self.contact_address_box = self.page.locator('#ContactAddressTextBox')
        self.contact_suburbb_box = self.page.locator('#ContactSuburbTextBox')
        self.contact_mobile_box = self.page.locator('#ContactMobileTextBox')

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
        print(add_service_url)
        return add_service_url

    @property
    def check_sections(self):
        '''check each section in Add Service page'''
        doors_section = self.doors_section_loc.inner_text()
        service_details = self.service_details_loc.inner_text()
        site_contact_details = self.site_contact_details_loc.inner_text()
        service_items = self.service_item_loc.inner_text()
        service_documents = self.service_documents_loc.inner_text()
        print(doors_section, service_details, site_contact_details, service_items, service_documents)
        return doors_section, service_details, site_contact_details, service_items, service_documents

    @property
    def check_buttons(self):
        '''check each button in Add Service page'''
        back_service = self.back_service_btn.inner_text()
        save_service = self.save_service_btn.inner_text()
        print(back_service, save_service)
        return back_service

    @property
    def check_doors_section(self):
        '''check each elements in "Doors" section'''
        door_type = self.door_type_loc.inner_text()
        self.door_type_select.click()
        door_type_select = self.door_type_select.inner_text()
        additional_info = self.additional_info_loc.inner_text()
        print(door_type, door_type_select, additional_info)
        return door_type, door_type_select, additional_info

    @property
    def check_addition_box(self):
        '''check the Additional Door Infomation box in "Doors" section'''
        additional_info_box = self.additional_info_box
        if additional_info_box.is_visible():
            print('yes')
            return True
        else:
            print('no')
            return False

    @property
    def check_service_details(self):
        '''check each elements in "Service Details" section'''
        service_type = self.service_type_loc.inner_text()
        service_area = self.service_area_loc.inner_text()
        service_status = self.service_status_loc.inner_text()
        invoice_no = self.invoice_no_loc.inner_text()
        account_type = self.account_type_loc.inner_text()
        account_customer = self.account_customer_loc.inner_text()
        order_date = self.order_date_loc.inner_text()
        service_date = self.service_date_loc.inner_text()
        customer_po = self.customer_po_loc.inner_text()
        user = self.user_loc.inner_text()
        service_tech = self.service_tech_loc.inner_text()
        service_tech_name = self.service_tech_name_loc.inner_text()
        description = self.description_loc.inner_text()
        print(service_type, service_area, service_status, invoice_no, account_type, account_customer, order_date,
              service_date, customer_po, user, service_tech, service_tech_name, description)
        return (service_type, service_area, service_status, invoice_no, account_type, account_customer, order_date,
                service_date, customer_po, user, service_tech, service_tech_name, description)

    def add_service_func(self):
        '''put details and add a new service'''
        self.door_type_select.select_option(label='Custom Door')
        self.additional_info_box.fill('Custom1000x3000 by Automation')
        self.service_type_select.select_option(label='Residential')
        self.service_area_select.select_option(label='Vic Metro')
        self.client_name_box.fill('Add_by_Automation')
        self.contact_address_box.fill('99 Auto added')
        self.contact_suburbb_box.fill('Kew')
        self.contact_mobile_box.fill('0400999999')

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
        page.goto("http://xxx/")
        login = Add_Service(page)
        login.typeUserName('xxxxx')
        login.typePassword('xxxxx')
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

