# coding=utf-8

import api_call.account.xq_api.xq_api_for_profile as ybm_api
from api_call.account.xq_api.xq_api_for_gis import LessonPlan
import testcases.account.xq_glb as glb
# import testcases.account.fep_glb as glb
import nd.rest.http_mot as CoHttpM
import json
from config.gbl import *
import unittest
import random
import sys
import uuid
from unittest import SkipTest

from data_struct.request_data import RequestData

__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')


def item(response):
    #  data ->dict()
    data = json.loads(response['data'])
    return data


class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)
        cls.lp = LessonPlan(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_learningStore_login_0(self):
        """
            1.0[POST] /登录 反向案例 密码为空
        """
        response = self.lp.post_login_Ls(glb.email, glb.password_0)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_learningStore_login_1(self):
        """
            1.1 [POST] /登录 反向案例 密码输入错误
            level:1,2,4,5
        """
        response = self.lp.post_login_Ls(glb.email, glb.password_1)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_learningStore_login_2(self):
        """
            1.2 [POST] /登录 反向案例 密码少于8个字符
            level:1,2,4,5
        """
        response = self.lp.post_login_Ls(glb.email, glb.password_2)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_learningStore_login_3(self):
        """
            1.2 [POST] /登录 反向案例 密码格式错误
            level:1,2,4,5
        """
        response = self.lp.post_login_Ls(glb.email, glb.password_3)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_learningStore_login_4(self):
        """
            1.3 [POST] /登录 反向案例 用户输入为空
            level:1,2,4,5
        """
        response = self.lp.post_login_Ls(glb.email_0, glb.password)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_learningStore_login_5(self):
        '''
           1.2 [POST] /登录 反向案例 用户输入email格式错误
            level:1,2,4,5
        '''
        response = self.lp.post_login_Ls(glb.email_1, glb.password)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_learningStore_login_6(self):
        '''
           1.2 [POST] /登录 反向案例 用户输入email不存在
            level:1,2,4,5
        '''
        response = self.lp.post_login_Ls(glb.email_1, glb.password)
        glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_edit_profile(self):
        '''
       1 [POST] /编辑用户语言切换到传统中文
        level:1,2,4,5
        '''

        response = self.lesson_object.post_list_query()
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_edit_profile_01(self):
        '''
       2 [POST] /编辑用户 名字 first name lian-liantest
        level:1,2,4,5
        '''

        response = self.lesson_object.post_list_query_01()
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_edit_profile_reserve_01(self):
        '''
       2.0 [POST] /编辑用户 名字 first name 又编辑回来 liantest-lian
        level:1,2,4,5
        '''

        response = self.lesson_object.post_list_query_010()
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    # def test_edit_profile_02(self):
    #     """
    #         [post]3.0 修改密码与原始密码一致     //Qazxsw1234--Qazxsw123456
    #          wyz 情况不明朗
    #     """
    #     # error_code = "PROMETHEAN.IDENTITY.CHANGE_PASSWORD_ERROR"
    #
    #     response = self.lesson_object.post_edit_password(glb.password_pre, glb.password_new)
    #     glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_edit_profile_03(self):
        '''
       3.1 [POST]
       1.编辑个人信息 修改密码 Qazxsw1234--Qazxsw123456
       2.改回密码
        level:1,2,4,5
        '''
        # 400
        error_code = "PROMETHEAN.IDENTITY.CHANGE_PASSWORD_ERROR"
        # 修改密码
        response_01 = self.lesson_object.post_edit_password(glb.password_pre, glb.password_new)
        time.sleep(2.0)  # 等待第一次修改
        data = item(response_01)

        if response_01.get('code') == 200:
            # 重登,修改回原密码,再次跑接口
            self.lp.post_login_Ls(glb.user_name, glb.password_new)
            self.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)  # 重置新headers

            response_02 = self.lesson_object.post_edit_password_01(glb.password_pre_01, glb.password_new_01)

            # 再次判断修改后的状态
            if response_02.get('code') == 400 and data["errorCode"] == error_code:
                glb.rest_o.parse_response(response_01, glb.CODE400, glb.message)
                print('<p>Cookie 失效或被多次修改密码？ {}</p>'.format(response_01.get('code')))
            else:
                glb.rest_o.parse_response(response_02, glb.CODE200, glb.message)

        elif response_01.get('code') == 400 and data["errorCode"] == error_code:
            glb.rest_o.parse_response(response_01, glb.CODE400, glb.message)
            print('<p>Cookie 失效或被多次修改密码？ {}</p>'.format(response_01.get('code')))

        else:
            raise BaseException('接口报错code {}'.format(response_01.get('code')))
        glb.rest_o.parse_response(response_01, glb.CODE200, glb.message)


