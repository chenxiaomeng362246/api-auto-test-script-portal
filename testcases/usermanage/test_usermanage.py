#!/usr/bin/env python
# coding=utf-8
from api_call.usermanage.client import GraphQLClient
import random
import sys
import unittest

from typing import Dict, Any, Union

import api_call.account.xq_api.xq_api_for_ybm as ybm_api
import testcases.account.xq_glb as glb
# import testcases.account.fep_glb as glb
import nd.rest.http_mot as CoHttpM
import json
from config.gbl import *
import uuid
from unittest import SkipTest
from api_call.usermanage.xq_api_for_sandox import LessonPlan01
from data_struct.request_data import RequestData
from graphql_client_master.graphqlclient.client import GraphQLClient

__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')


def item(response):
    #  data ->dict()
    data = json.loads(response['data'])
    return data


class UserTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     assert_that(ENVIRONMENT in [TEST, PRE], equal_to(True), '暂不支持该环境')

    def setUp(self):
        self.lesson_object01 = LessonPlan01(ENVIRONMENT)


    def tearDown(self):
        # 析构方法 退出登录
        '''
        '''

    def test_usermanage(self):
        '''
       1.0 usermanage
        level:1,2,4,5
        '''

        # client = GraphQLClient('https://devapi.prometheanproduct.com/mdm-portal/graphql')

        #
        # # variables = {"serialNumber":"65W25KCI18CX135000017P"}
        # result = client.execute(query)
        response = self.lesson_object01.api_post()
        result = glb.rest_o.parse_response(response, glb.CODE400, glb.message)
        print '<p>{}</p>'.format(result)

    def test_usermanage01(self):

        client = GraphQLClient('https://devapi.prometheanproduct.com/user-management/graphql')
        query ="{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        result = client.execute(query)
        # result = result.getcode()
        print '-----------------------<p>{}</p>----------------------------------'.format(result)
        self.assertEqual(result,200,'失败')





