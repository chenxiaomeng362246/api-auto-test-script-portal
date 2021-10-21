# coding=utf-8
#import config.xq_glb as glb
#__author:chenxiaomeng
#date:2021/10/14

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_manage_sites.move_panel_to_sites as api_pm


class test_update_panel_site(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_pm.MovePanelsToSites(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    # 正向用例
    def test_update_panel_site_ok(self):
        """
            [POST]panel manage site
        """
        site_id = "d0bcaa84-cb5a-be61-4d97-28259a69b805"
        serial_numbers = "APISN-J9HL9E9999901"

        err_message = 'update_panel_site失败'
        response = self.panel_object.move_panels_to_sites(site_id, serial_numbers)
        self.rest_o.parse_response(response, glb.CODE200, err_message)

    # 逆向用例  没有参数
    def test_update_panel_site_without_params(self):
        """
            [POST]panel manage site
        """
        site_id = None
        serial_numbers = None

        err_message = 'update_panel_site失败，没有参数'
        response = self.panel_object.move_panels_to_sites(site_id, serial_numbers)
        self.rest_o.parse_response(response, glb.CODE400, err_message)

    # 逆向用例  site id序列存在问题，不存在
    def test_update_panel_site_siteid_not_exit(self):
        """
            [POST]panel manage site
        """
        site_id = "d0bcaa84-cb5a-be61-4d97"
        serial_numbers = "APISN-J9HL9E9999901"

        err_message = 'update_panel_site失败，site_id不存在'
        response = self.panel_object.move_panels_to_sites(site_id, serial_numbers)
        self.rest_o.parse_response(response, glb.CODE200, err_message)

     # 逆向用例  sn存在问题，sn不存在
    def test_update_panel_site_sn_not_exit(self):
        """
            [POST]panel manage site
        """
        site_id = "d0bcaa84-cb5a-be61-4d97-28259a69"
        serial_numbers = "APISN-J9HL9E"

        err_message = 'update_panel_site失败，serial_numbers不存在'
        response = self.panel_object.move_panels_to_sites(site_id, serial_numbers)

        self.rest_o.parse_response(response, glb.CODE200, err_message)
