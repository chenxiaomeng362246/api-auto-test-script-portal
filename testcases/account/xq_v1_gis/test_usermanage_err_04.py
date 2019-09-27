# coding=utf-8
import sys
import unittest
import api_call.account.xq_api.xq_api_for_gis as gis_api
import api_call.account.xq_api.xq_api_for_usermanage_auth_err_04 as ybm_api
import config.gbl as g
import testcases.account.xq_glb as glb
# import testcases.account.fep_glb as glb
import nd.rest.http_mot as CoHttpM
import json
import re
from config.gbl import *
from unittest import SkipTest
from api_call.base.txt_opera import TxtOpera
from data_struct.request_data import RequestData
# from selenium import webdriver
from api_call.base.txt_opera import TxtOpera
import time,json
__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')


class UserTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     assert_that(ENVIRONMENT in [TEST, PRE], equal_to(True), '暂不支持该环境')

    def setUp(self):
        self.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)

    def tearDown(self):
        # 析构方法 退出登录
        '''
        '''



    def test_usrmanagement_403(self):
        '''
       1 [POST] /user management other error An invalid or missing x-api-key header in request 403
        level:1,2,4,5
        '''
        response = self.lesson_object.post_list_query()
        data_dec = glb.rest_o.parse_response(response, glb.CODE403, glb.message)



if __name__ == "__main__":
    unittest.main()
