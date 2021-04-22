# coding=utf-8
import testcases.account.xq_glb as glb
from config.gbl import *
import unittest
import api_call.jin.get_token as api_token


class JinTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lesson_object = api_token.JinToken(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    def test_gettoken(self):
        """
            [POST] /获取登录token
        """
        err_message = '获取token失败'
        response = self.lesson_object.jin_gettoken()
        glb.rest_o.parse_response(response, glb.CODE200, err_message)
