# Author:Yi Sun(Tim) 2024-11-06

'''Production Page for Panel Lift doors'''

from playwright.sync_api import Page
from pages.production import Production

class Panel_lift_Safe(Production):

    def __init__(self,page:Page):
        super().__init__(page)
        self.url_path = "Production"
        self._init_locators_panel_lift()

    def _init_locators_panel_lift(self):

        '''loc for each section in this page'''
        self.order_loc = self.page.locator('#sample')
        self.rollforming_loc = self.page.locator('#sample')
        self.assembly_loc = self.page.locator('#sample')
        self.modifications_loc = self.page.locator('#sample')
        self.extras_orders_loc = self.page.locator('#sample')
        self.paint_loc = self.page.locator('#sample')
        self.painted_loc = self.page.locator('#sample')
        self.qc_loc = self.page.locator('#sample')

        '''loc for "Order" section in this page'''
        self.number_doors_loc = self.page.locator("[name='sample']")
        self.proposal_no_loc = self.page.locator("[name='sample']")
        self.client_name_loc = self.page.locator("[name='sample']")
        self.supply_type_loc = self.page.locator("[name='sample']")
        self.door_no_loc = self.page.locator("[name='sample']")
        self.status_loc = self.page.locator("[name='sample']")
        self.extraorders_doc_loc = self.page.locator("[name='sample']")
        self.save_changes_order_btn_loc = self.page.locator('#saveSingleSkinOrderData')
        self.first_orderid_loc = self.page.locator("[name='sample']")
        self.search_order_box_loc = self.page.locator('#SingleSkinOrderSearchInput')
        self.searched_order_status_loc =  self.page.locator("xpath=//select[contains(@id, '_status')]")

        '''loc for "Rollforming" section in this page'''
        self.number_doors_roll_loc = self.page.locator("[name='sample']")
        self.reschedule_loc = self.page.locator("[name='sample']")
        self.date_filter_loc = self.page.locator('#reschedule-from')
        self.apply_btn = self.page.locator("[name='sample']")
        self.search_job_box = self.page.locator('#search-door')
        self.search_job_btn = self.page.locator("[name='sample']")
        self.save_changes_rollforming_btn = self.page.locator('#saveSingleSkinRollingData')
        self.table_frame_loc = self.page.locator("[name='sample']")
        self.proposal_num_searched_loc = self.page.locator("[name='sample']")
        self.searched_popup_loc = self.page.locator('.modal-dialog')
        self.searched_result_job_loc = self.page.locator("[name='sample']")
        self.actual_height_loc = self.page.locator("[name='sample']")


        '''loc for "Assembly" section in this page'''
        self.number_doors_assembly_loc = self.page.locator("[name='sample']")
        self.prop_no_loc = self.page.locator("[name='sample']")
        self.door_no_assembly_loc = self.page.locator("[name='sample']")
        self.status_assembly_loc = self.page.locator("[name='sample']")

        '''loc for "Modification" section in this page'''
        self.number_doors_modification_loc = self.page.locator("[name='sample']")
        self.prop_no_modification_loc = self.page.locator("[name='sample']")
        self.door_colour_loc = self.page.locator("[name='sample']")
        self.extradoc_modification_loc = self.page.locator("[name='sample']")

        '''loc for "Extra Orders" section in this page'''
        self.number_doors_extra_loc = self.page.locator("[name='sample']")
        self.prop_no_extra_loc = self.page.locator("[name='sample']")
        self.colour_category_loc = self.page.locator("[name='sample']")
        self.extradoc_extra_loc = self.page.locator("[name='sample']")

        '''loc for "Paint" section in this page'''
        self.number_doors_paint_loc = self.page.locator("[name='sample']")
        self.prop_no_paint_loc = self.page.locator("[name='sample']")
        self.actual_height_loc = self.page.locator("[name='sample']")
        self.status_paint_loc = self.page.locator("[name='sample']")

        '''loc for "Painted" section in this page'''
        self.number_doors_painted_loc = self.page.locator("[name='sample']")
        self.prop_no_painted_loc = self.page.locator("[name='sample']")
        self.number_panels_loc = self.page.locator("[name='sample']")
        self.status_painted_loc = self.page.locator("[name='sample']")

        '''loc for "QC" section in this page'''
        self.number_doors_qc_loc = self.page.locator("[name='sample']")
        self.prop_no_qc_loc = self.page.locator("[name='sample']")
        self.actual_width_loc = self.page.locator("[name='sample']")
        self.status_qc_loc = self.page.locator("[name='sample']")
        self.qc_fail_loc = self.page.locator("[name='sample']")
        self.qc_pass_loc = self.page.locator("[name='sample']")
        self.qc_fail_radiobox_loc = self.page.locator('#SSQCFailRadiobutton')
        self.qc_pass_radiobox_loc = self.page.locator('#SSQCPassRadiobutton')

    def go_panel_lift_safe(self):
        '''Switch to Panel Lift Safe section in Production'''
        self.panel_lift_loc.click()
    def go_rollforming(self):
        '''Switch to Rollforming screen'''
        self.rollforming_loc.click()

    @property
    def check_panel_lift_section(self):
        '''check each section in Panel Lift Safe page'''
        order = self.order_loc.inner_text()
        rollforming = self.rollforming_loc.inner_text()
        assembly = self.assembly_loc.inner_text()
        modifications = self.modifications_loc.inner_text()
        extras_orders = self.extras_orders_loc.inner_text()
        paint = self.paint_loc.inner_text()
        painted = self.painted_loc.inner_text()
        qc = self.qc_loc.inner_text()
        print (order,rollforming,assembly,modifications,extras_orders,paint,painted,qc)
        return order,rollforming,assembly,modifications,extras_orders,paint,painted,qc

    @property
    def get_first_orderid(self):
        '''get the first order's job id, this fun is for change_quote_status module'''
        first_order_id = self.first_orderid_loc.inner_text()
        print(first_order_id)
        return  first_order_id
    @property
    def check_order_table(self):
        '''check each column in Order table'''
        number_doors = self.number_doors_loc.inner_text()
        proposal_no = self.proposal_no_loc.inner_text()
        client_name = self.client_name_loc.inner_text()
        supply_type = self.supply_type_loc.inner_text()
        door_no = self.door_no_loc.inner_text()
        status = self.status_loc.inner_text()
        extraorders_doc = self.extraorders_doc_loc.inner_text()
        print (number_doors,proposal_no,client_name,supply_type,door_no,status,extraorders_doc)
        return number_doors,proposal_no,client_name,supply_type,door_no,status,extraorders_doc
    @property
    def check_rollforming_table(self):
        '''check each elements in Rollforming table'''
        self.rollforming_loc.click()
        self.number_doors_roll_loc.wait_for(state="visible", timeout=2000)
        number_doors_roll = self.number_doors_roll_loc.inner_text()
        reschedule = self.reschedule_loc.inner_text()
        print (number_doors_roll,reschedule)
        return  number_doors_roll,reschedule

    @property
    def check_rollforming_date_filter(self):
        '''check Date Filter fun in Rollforming table'''
        # self.rollforming_loc.click()
        date_filter = self.date_filter_loc
        if date_filter.is_visible(timeout=2000):
            return True
        else:
            return False

    @property
    def check_rollforming_save(self):
        '''check Save Changes button in Rollforming table'''
        save_changes_btn = self.save_changes_rollforming_btn
        if save_changes_btn.is_visible(timeout=2000):
            if save_changes_btn.is_enabled():
                print("Button is present, visible and enabled")
                return True
            else:
                print("Button is visible but DISABLED")
                return False
        else:
            print('Button is not visible within 50s')
            return False
    @property
    def check_rollforming_tableframe(self):
        '''check Table display in Rollforming screen'''
        if self.table_frame_loc.is_visible(timeout=2000):
            print('yes')
            return True
        else:
            print('no')
            return False
    @property
    def check_assembly_table(self):
        '''check each elements in Assembly table'''
        self.assembly_loc.click()
        number_doors_assembly = self.number_doors_assembly_loc.inner_text()
        prop_no = self.prop_no_loc.inner_text()
        door_no_assembly = self.door_no_assembly_loc.inner_text()
        status_assembly = self.status_assembly_loc.inner_text()
        print (number_doors_assembly,prop_no,door_no_assembly,status_assembly)
        return  number_doors_assembly,prop_no,door_no_assembly,status_assembly
    @property
    def check_modification_table(self):
        '''check each elements in Modification table'''
        self.modifications_loc.click()
        number_doors_modification = self.number_doors_modification_loc.inner_text()
        prop_no_modification = self.prop_no_modification_loc.inner_text()
        door_colour = self.door_colour_loc.inner_text()
        extradoc_modification = self.extradoc_modification_loc.inner_text()
        print (number_doors_modification,prop_no_modification,door_colour,extradoc_modification)
        return  number_doors_modification,prop_no_modification,door_colour,extradoc_modification

    @property
    def check_extraorder_table(self):
        '''check each elements in Extra Order table'''
        self.extras_orders_loc.click()
        number_doors_extraorder = self.number_doors_extra_loc.inner_text()
        prop_no_extra = self.prop_no_extra_loc.inner_text()
        colour_category = self.colour_category_loc.inner_text()
        extradoc_extra = self.extradoc_extra_loc.inner_text()
        print (number_doors_extraorder,prop_no_extra,colour_category,extradoc_extra)
        return  number_doors_extraorder,prop_no_extra,colour_category,extradoc_extra
    @property
    def check_paint_table(self):
        '''check each elements in Paint table'''
        self.paint_loc.click()
        number_doors_paint = self.number_doors_paint_loc.inner_text()
        prop_no_paint = self.prop_no_paint_loc.inner_text()
        actual_height = self.actual_height_loc.inner_text()
        status_paint = self.status_paint_loc.inner_text()
        print (number_doors_paint,prop_no_paint,actual_height,status_paint)
        return  number_doors_paint,prop_no_paint,actual_height,status_paint

    @property
    def check_painted_table(self):
        '''check each elements in Painted table'''
        self.painted_loc.click()
        number_doors_painted = self.number_doors_painted_loc.inner_text()
        prop_no_painted = self.prop_no_painted_loc.inner_text()
        number_panels = self.number_panels_loc.inner_text()
        status_painted = self.status_painted_loc.inner_text()
        print (number_doors_painted,prop_no_painted,number_panels,status_painted)
        return  number_doors_painted,prop_no_painted,number_panels,status_painted

    @property
    def check_qc_table(self):
        '''check each elements in QC table'''
        self.qc_loc.click()
        number_doors_qc = self.number_doors_qc_loc.inner_text()
        prop_no_qc = self.prop_no_qc_loc.inner_text()
        actual_width = self.actual_width_loc.inner_text()
        status_qc = self.status_qc_loc.inner_text()
        print (number_doors_qc,prop_no_qc,actual_width,status_qc)
        return  number_doors_qc,prop_no_qc,actual_width,status_qc

    @property
    def check_qc_table_new(self):
        '''check qc pass and qc fail radio box in QC table'''
        qc_fail = self.qc_fail_loc.inner_text()
        qc_pass = self.qc_pass_loc.inner_text()
        print (qc_fail,qc_pass)
        return  qc_fail,qc_pass

    @property
    def check_qc_fail(self):
        '''check qc fail radio box status'''
        if qc_fail_radiobox_loc.is_checked():
            print('selected, correct')
            return  True
        else:
            print("not selected, wrong")
            return False

    @property
    def check_qc_pass(self):
        '''check qc pass radio box status'''
        if self.qc_pass_radiobox_loc.is_checked():
            print('selected, wrong')
            return  False
        else:
            print("not selected, correct")
            return True


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http://test/")
        login = Panel_lift_Safe(page)
        login.typeUserName('test')
        login.typePassword('test')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.go_production()
        login.go_panel_lift_safe()
        # login.check_panel_lift_section
        login.check_order_table
        # login.check_rollforming_table
        # login.check_rollforming_date_filter
        # login.check_rollforming_tableframe
        # login.check_rollforming_save
        # login.check_assembly_table
        # login.check_modification_table
        # login.check_extraorder_table
        # login.check_paint_table
        # login.check_painted_table
        # login.check_qc_table
        # login.check_qc_table_new
        # login.check_qc_fail
        # login.check_qc_pass