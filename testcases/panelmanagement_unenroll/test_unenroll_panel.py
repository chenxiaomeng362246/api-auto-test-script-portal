# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/18

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_unenroll.unenroll_panel as api_pm
import data_struct.panelmanagement_enroll_sn as panel_sn
import testcases.panelmanagement_unenroll.test_enroll_panel as test_enroll
from util.txt_opera import TxtOpera
import data_struct.ramdon as randomdata
import string

class test_unenroll_panel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_pm.Unenroll_panel(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    #由于接口文档中并无参数长度校验、必填项校验、无有效性校验、无参数组合校验、故只针对场景进行分类
    #正向用例
    def test_unenroll_panel_ok(self):
        """
            [POST]将设备注册到组织
        """
        panelsn = panel_sn.panel_data.unenrollsn
        response = self.panel_object.unenroll_panel(panelsn)
        # name = ["a", "b", "c"]
        # for n in name:
        data = self.rest_o.parse_response(response, glb.CODE200, glb.message)
        print isinstance(data,dict)
        unenroll = data['data']['unenroll'][0]['unenrolled']

        #断言 判断当前状态是否变成unenroll
        self.assertTrue(unenroll,'没有uneroll成功')



    # 逆向用例 sn为空
    def test_unenroll_panel_without_params(self):
        """
            [POST]将设备注册到组织
        """
        panelsn = None
        response = self.panel_object.unenroll_panel(panelsn)
        data = self.rest_o.parse_response(response, glb.CODE400, glb.message)

    # 逆向用例 sn没有按照应有的规则或者找不到指定的设备sn
    def test_unenroll_panel_with_wrongsn(self):
        """
            [POST]将设备注册到组织
        """
        panelsn = '786T-J6210-env-dev'
        response = self.panel_object.unenroll_panel(panelsn)
        data = self.rest_o.parse_response(response, glb.CODE200, glb.message)











