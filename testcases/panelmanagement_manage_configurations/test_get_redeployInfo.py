# coding=utf-8

#__author:chenxiaomeng
#date:2021/10/14

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_manage_configurations.get_redeployInfo as api_re

from util.txt_opera import TxtOpera
import data_struct.ramdon as randomdata
import string

class test_get_redepolyinfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_re.Redeployinfo(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    #由于接口文档中并无参数长度校验、必填项校验、无有效性校验、无参数组合校验、故只针对场景进行分类
    #正向用例
    def test_get_redepolyinfo(self):
        """
            [POST]panel manage site
        """
        response = self.panel_object.redeployinfo()
        err_message = "redepoly失败"
        data = self.rest_o.parse_response(response, glb.CODE200, err_message)


