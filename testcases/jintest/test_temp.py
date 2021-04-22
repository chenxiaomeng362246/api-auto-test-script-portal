# coding=utf-8
import testcases.account.xq_glb as glb
from config.gbl import *
import unittest
import api_call.jin.api_temp as jinapi


class JinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lesson_object = jinapi.Jin(DEV)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    def test_case_get_org_details(self):
        """
            [POST]获取某个组织的组织详情
        """
        org_name = "prn:Organization::ApiTest"
        # 获取组织详情  //ApiTest
        err_message = '获取组织详情失败'
        response = self.lesson_object.jin2_api_get_org_details(org_name)
        glb.rest_o.parse_response(response, glb.CODE200, err_message)
