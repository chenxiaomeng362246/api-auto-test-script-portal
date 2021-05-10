# coding=utf-8
import testcases.account.xq_glb as glb
from config.gbl import *
import unittest
import api_call.jin.api_panelManagement as api_panelManagement



class PmTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lesson_object = api_panelManagement.LessonPlan(SANDBOX)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    # panel manage site
    def test_manageSite(self):
        """
            [POST]panel manage site
        """
        site_id = "d0bcaa84-cb5a-be61-4d97-28259a69b805"
        serial_numbers = "APISN-J9HL9E9999901"
        err_message = 'manage site失败'
        response = self.lesson_object.api_manageSite(site_id, serial_numbers)
        glb.rest_o.parse_response(response, glb.CODE200, err_message)
