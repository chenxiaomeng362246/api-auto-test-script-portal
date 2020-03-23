# coding=utf-8
import sys
import unittest
import api_call.account.xq_api.xq_api_for_gis as gis_api
import api_call.account.xq_api.xq_api_for_ybm as ybm_api
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
import time, json
from api_call.base.josn_opera import JsonOpera

__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')


class UserTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     assert_that(ENVIRONMENT in [TEST, PRE], equal_to(True), '暂不支持该环境')

    def setUp(self):
        self.lesson_object = gis_api.LessonPlan(ENVIRONMENT)
        self.jop = JsonOpera()

    def tearDown(self):
        # 析构方法 退出登录
        '''
        '''


    def test_sso_login(self):
        '''
       1 [POST] /sso单点登录
        level:1,2,4,5
        '''
        response = self.lesson_object.post_login_Ls(glb.user_name, glb.password_ds)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        time.sleep(5.0)
        cookie = dict(response.get('response_header')).get('set-cookie')
        print "<p>{}</p>".format('=' * 20)

        # 正则表达式抽取XSRF-TOKEN=的值 .*? 是懒惰匹配
        XSRF_TOKEN = re.findall(r"XSRF-TOKEN=(.+?);", cookie)

        print "<p>{}</p>".format('=' * 20)
        cookie_1 = re.findall(r"prom:sess=(.+?);", cookie)
        print "<p>{}</p>".format('-' * 20)
        print "<p>{}</p>".format(cookie)
        # 把数组【】转为字符串
        print "<p>{}</p>".format(''.join(XSRF_TOKEN))
        print "<p>{}</p>".format(''.join(cookie_1))
        # print "<p>{}</p>".format(''.join(cookie_1))
        print "<p>{}</p>".format(response)
        print "<p>{}</p>".format(type(response))

        # TxtOpera().write_txt(''.join(XSRF_TOKEN))
        # cookie = data_dec.get()
        TxtOpera().write_txt_cookies(cookie)
        TxtOpera().write_txt_cookies_p(''.join(cookie_1))
        TxtOpera().write_txt_cookies_x(''.join(XSRF_TOKEN))





if __name__ == "__main__":
    unittest.main()
