# Author:Yi Sun(Tim) 2024-11-06

'''Test Panel Lift Safe Page'''

import pytest
from UIModule.panel_left_safe import Panel_lift_Safe


class Test_PanelLiftSafe():

    def test_panellift_ui_001(self,panel_lift_safe):
        '''Verify each section in Panel Lift Safe page'''
        expected =('Order','Rollforming','Assembly','Modifications',
                          'Extras Orders','Paint','Painted','QC')
        actual = panel_lift_safe.check_panel_lift_section
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_002(self,panel_lift_safe):
        '''Verify each column in Order table'''
        expected = ('Number of Doors:','Proposal No','Client Name','Supply Type','Door No',
                          'Status','    Extras Orders & Documents')
        actual = panel_lift_safe.check_order_table
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_003(self,panel_lift_safe):
            '''Verify each elements in Rollforming table'''
            expected = ('Number of Doors:', 'Reschedule from:')
            actual = panel_lift_safe.check_rollforming_table
            assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_004(self,panel_lift_safe):
        '''Verify Date Filter fun in Rollforming table'''
        assert panel_lift_safe.check_rollforming_date_filter is True

    def test_panellift_ui_005(self,panel_lift_safe):
        '''Verify Save Changes button in Rollforming table'''
        assert panel_lift_safe.check_rollforming_save is True

    def test_panellift_ui_006(self,panel_lift_safe):
        '''Verify Table display in Rollforming screen'''
        assert panel_lift_safe.check_rollforming_tableframe is True

    def test_panellift_ui_007(self,panel_lift_safe):
            '''Verify each elements in Assembly table'''
            expected = ('Number of Doors:', 'Prop. No','Door No','Status')
            actual = panel_lift_safe.check_assembly_table
            assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_008(self,panel_lift_safe):
        '''Verify each elements in Modification table'''
        expected = ('Number of Doors:', 'Prop. No', 'Door Colour', '    Extras Orders & Documents')
        actual = panel_lift_safe.check_modification_table
        assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_009(self,panel_lift_safe):
        '''Verify each elements in Extra Order table'''
        expected = ('Number of Doors:', 'Prop. No', 'Colour Category', '    Extras Orders & Documents')
        actual = panel_lift_safe.check_extraorder_table
        assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_010(self,panel_lift_safe):
            '''Verify each elements in Paint table'''
            expected = ('Number of Doors:', 'Proposal No', 'Actual Height', 'Status')
            actual = panel_lift_safe.check_paint_table
            assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_011(self,panel_lift_safe):
        '''Verify each elements in Painted table'''
        expected = ('Number of Doors:', 'Proposal No', 'Number of Panels', 'Status')
        actual = panel_lift_safe.check_painted_table
        assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_012(self,panel_lift_safe):
            '''Verify each elements in QC table'''
            expected = ('Number of Doors:', 'Proposal No', 'Actual Width', 'Status')
            actual = panel_lift_safe.check_qc_table
            assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_013(self,panel_lift_safe):
            '''Verify qc pass and qc fail radio box in QC table'''
            expected = ('QC Fail', 'QC Pass',)
            actual = panel_lift_safe.check_qc_table_new
            assert actual == expected, f"Expected:{expected},but got: {actual}"

    def test_panellift_ui_014(self,panel_lift_safe):
            '''Verify qc fail radio box status'''
            assert panel_lift_safe.check_qc_fail is True

    def test_panellift_ui_015(self,panel_lift_safe):
            '''Verify qc fail radio box status'''
            assert panel_lift_safe.check_qc_pass is True
