# coding=utf-8

#__author:chenxiaomeng
#date:2021/10/14

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_manage_sites.update_panel_site as api_pm
from util.txt_opera import TxtOpera
import data_struct.ramdon as randomdata
import string

class test_add_panel_site(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_pm.UpdatePanelSite(ENVIRONMENT)


    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    #由于接口文档中并无参数长度校验、必填项校验、无有效性校验、无参数组合校验、故只针对场景进行分类
    #正向用例
    def test_update_panel_site_ok(self):
        """
            [POST]panel manage site
        """
        description = randomdata.Random().getramdondata()
        note = randomdata.Random().getramdondata()
        response = self.panel_object.update_panel_site(description,note)

        err_message = "更新panelsite失败"
        data = self.rest_o.parse_response(response, glb.CODE200, err_message)
        sitename = data['data']['updateSite']['name']
        sitedescription = data['data']['updateSite']['description']
        sitenote = data['data']['updateSite']['notes']

        # 断言 增加的site和返回增加的site的name一致 说明有正确添加成功
        self.assertItemsEqual("#GMS enabled and something", sitename)
        self.assertItemsEqual(sitedescription, description)
        self.assertItemsEqual(sitenote, note)



    #逆向用例
    #传递参数为空
    def test_update_panel_site_withoutparams(self):
        """
            [POST]panel manage site
        """
        err_message = "添加panelsite失败"
        site_name = None
        site_description =None
        site_note =None

        response = self.panel_object.update_panel_site(site_description,site_note)
        self.rest_o.parse_response(response, glb.CODE200, err_message)







