# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/16

from config.gbl import *
import config.information_glb as glb
import unittest
import data_struct.ramdon as randomdata
import api_call.panelmanagement_manage_sites.remove_panel_site as api_pm_rmp
import api_call.panelmanagement_manage_sites.add_panel_site as api_pm_amp
import api_call.panelmanagement_activitylog.nopanel_activitylogs as api_pm_ac

class test_panelactivity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        # 前置条件，先添加一个site
        cls.panel_object = api_pm_ac.NoPanelActivityLogs(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    def test_remove_panel_site(self):
        response = self.panel_object.get_nopanelactivitylogs(20)
        self.rest_o.parse_response(response, glb.CODE200, glb.message)