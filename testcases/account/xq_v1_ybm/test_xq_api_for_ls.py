# coding=utf-8
import random
import sys
from api_call.account.xq_api.xq_api_for_ls import NotePlan
import testcases.account.xq_glb as glb
# import testcases.account.fep_glb as glb
import nd.rest.http_mot as CoHttpM
import json
from config.gbl import *
import uuid
from unittest import SkipTest
import unittest
from data_struct.request_data import RequestData

__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')


def item(response):
    #  data ->type dict
    data = json.loads(response['data'])
    return data


class UserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.npl = NotePlan(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_user_info(self):
        self.npl.get_user_info()

    def test_get_user_resource_note(self):
        """
            获取用户资源  //[GET]/gls/users/{user_id}/resources/{resource_id}/note
        """
        # 资源搜索与排序
        response = self.npl.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 获取用户资源
        resource_id = data["items"][0]["id"]
        response_code = self.npl.get_user_resource_note(self.npl.userId, resource_id).get('code')
        self.assertEqual(response_code, 200)
        # glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_list_collection_user_id(self):
        '''
       4.9. 获取某个用户下的所有collection列表[GET]
        '''
        response = self.npl.get_list_collection_library(self.npl.userId)
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)
