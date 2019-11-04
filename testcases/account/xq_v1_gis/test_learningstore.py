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

    # def test_learningStore_login(self):
    #     '''
    #    1 [POST] /登录
    #     level:1,2,4,5
    #     '''
    #     response = self.lesson_object.post_login_Ls(glb.email, glb.password)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #     token = data_dec.get('AuthenticationResult').get('IdToken', 'not token')
    #     token_access = data_dec.get('AuthenticationResult').get('AccessToken', 'not token')
    #     TxtOpera().write_txt(token)
    #     TxtOpera().write_txt_access(token_access)
    #
    # def test_learningStore_login_0(self):
    #     '''
    #    1.0 [POST] /登录 反向案例密码输入错误
    #     level:1,2,4,5
    #     '''
    #     response = self.lesson_object.post_login_Ls(glb.email, glb.password_0)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE400, glb.message)
    #     # token = data_dec.get('AuthenticationResult').get('IdToken','not token')
    #     # TxtOpera().write_txt(token)
    #
    # def test_learningStore_login_1(self):
    #     '''
    #    1.1 [POST] /登录 密码sql语言 or 1=1
    #     level:1,2,4,5
    #     '''
    #     response = self.lesson_object.post_login_Ls(glb.email, glb.password_1)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE400, glb.message)
    #     # token = data_dec.get('AuthenticationResult').get('IdToken','not token')
    #     # TxtOpera().write_txt(token)
    #
    # def test_learningStore_login_2(self):
    #     '''
    #    1.2 [POST] /登录 用户输入大小字母不是email格式
    #     level:1,2,4,5
    #     '''
    #     response = self.lesson_object.post_login_Ls(glb.email_0, glb.password)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE400, glb.message)
    #     # token = data_dec.get('AuthenticationResult').get('IdToken', 'not token')
    #     # TxtOpera().write_txt(token)
    #
    # def test_learningStore_refresh(self):
    #     '''
    #    2 [POST] /刷新登录
    #     level:1,2,4,5
    #     '''
    #     response = self.lesson_object.post_login_Ls(glb.email, glb.password)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #     RefreshToken = data_dec['AuthenticationResult']['RefreshToken']
    #     IdToken = data_dec['AuthenticationResult']['IdToken']
    #     response = self.lesson_object.post_loginrefresh_ls(RefreshToken, IdToken)
    #     print response
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
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

    # def test_login(self):
    #     txt_o = TxtOpera()
    #     driver = webdriver.Firefox()
    #     driver.get("https://dev-user-management.prometheanproduct.com/")
    #     time.sleep(5.0)
    #     driver.find_element_by_xpath(
    #         '//*[@id="loginInModalContainer"]/div/div/div/form/div[1]/div/div/span/div/input').send_keys(
    #         "nl5882112@126.com")
    #     driver.find_element_by_xpath(
    #         '//*[@id="loginInModalContainer"]/div/div/div/form/div[2]/div/div/span/div/input').send_keys("Chen123456")
    #     driver.find_element_by_xpath('//*[@id="loginInModalContainer"]/div/div/div/button').click()
    #     time.sleep(30.0)
    #     cookies = driver.get_cookies()
    #     # for item in cookies:
    #     #     print 'Name = ' + item.name
    #     #     print 'Value = ' + item.value
    #
    #
    #     # for cookies =cookies[0]
    #     # print json.loads(cookies)
    #     # print type(cookies)
    #     txt_o.write_txt_cookies(json.dumps(cookies))
    #     driver.quit()

    def test_org_login(self):
        """
            1 [POST] //org sso单点登录 level:1,2,4,5
        """
        response = self.lesson_object.post_login_Ls(glb.ORG_USER_NAME, glb.ORG_PASSWORD)
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        time.sleep(5.0)
        cookie = dict(response.get('response_header')).get('set-cookie')

        # 正则表达式抽取XSRF-TOKEN=的值 .*? 是懒惰匹配
        org_xsrf_token = re.findall(r"XSRF-TOKEN=(.+?);", cookie)
        org_tokenId = re.findall(r"prom:sess=(.+?);", cookie)

        # 保存到json
        org_user_info = dict()
        org_user_info["org_tokenId"] = ''.join(org_tokenId)
        org_user_info["org_xsrf_token"] = ''.join(org_xsrf_token)

        self.jop.write_json(org_user_info)



if __name__ == "__main__":
    unittest.main()
