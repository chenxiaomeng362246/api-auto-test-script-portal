# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/16

from config.gbl import *
import config.information_glb as glb
import unittest
import data_struct.ramdon as randomdata
import api_call.panelmanagement_manage_tags.delete_tag as api_pm_dt
import api_call.panelmanagement_manage_sites.add_panel_site as api_pm_amp
from util.txt_opera import TxtOpera

class test_remove_panel_site(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        # 前置条件，先添加一个site
        cls.panel_object = api_pm_dt.DeleteTag(ENVIRONMENT)

        # name = randomdata.Random().getramdondata()
        # response = cls.panel_object.add_panel_site(name, "descriptiondescription", "notesnotes")
        # data = cls.rest_o.parse_response(response, glb.CODE200,glb.message)
        #
        # cls.siteid = data['data']['createSite']['id']
        # cls.prn = data['data']['createSite']['prn']
        # cls.sitename = data['data']['createSite']['name']
        #
        # print('siteid=' + cls.siteid)
        # print('prn=' + cls.prn)


        #TxtOpera().write_panel_site_id(siteid)


    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    # def test_remove_panel_site(self):
    #     self.panel_object = api_pm_rmp.RemovePanelSite(ENVIRONMENT)
    #     response = self.panel_object.remove_panel_site(self.prn,self.siteid)
    #     self.rest_o.parse_response(response, glb.CODE200, glb.message)


    def test_delete_tag(self):
        tagid = TxtOpera().read_tag_id()
        print '删除tagid为'+tagid

        response = self.panel_object.delete_tag(tagid)
        self.rest_o.parse_response(response, glb.CODE200, glb.message)