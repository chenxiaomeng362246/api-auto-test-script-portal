# coding=utf-8

from config.gbl import *
import unittest
import config.information_glb as glb
import api_call.panelmanagement_login.get_token as get_token
from util.txt_opera import TxtOpera
import unittest


class TokenTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token_object = get_token.Tokenget()
        cls.rest_o = Restful()

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    def test_getToken(self):
        """
            [POST] /获取登录token
        """
        err_message = '获取token失败'
        response = self.token_object.get_right_token()
        data = self.rest_o.parse_response(response, glb.CODE200, err_message)

        idtoken = data['AuthenticationResult']['IdToken']
        AuthorizationToken = "Bearer " + idtoken
        print(AuthorizationToken)
        TxtOpera().write_txt_authorizationToken(AuthorizationToken)

