# coding=utf-8

#__author:chenxiaomeng
#date:2021/10/14

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_unenroll.enroll_panel as api_pm
from util.txt_opera import TxtOpera
import data_struct.ramdon as randomdata
import data_struct.panelmanagement_enroll_sn as panel_sn

import string

class test_enroll_panel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_pm.Enroll_panel(ENVIRONMENT)


    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    #由于接口文档中并无参数长度校验、必填项校验、无有效性校验、无参数组合校验、故只针对场景进行分类
    #正向用例
    def test_enroll_panel(self):
        """
            [POST]将设备注册到组织
        """
        panelsn = panel_sn.panel_data.panelsn
        name = randomdata.Random().getramdondata()
        response = self.panel_object.enroll_panel(panelsn,name)

        data = self.rest_o.parse_response(response, glb.CODE200, glb.message)
        print isinstance(data,dict)
        enroll = data['data']['enroll'][0]['enrolled']

        # 断言 判断当前状态是否变成unenroll
        self.assertTrue(enroll, '没有enroll成功')









