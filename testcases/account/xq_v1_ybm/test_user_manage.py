# coding=utf-8
import api_call.account.xq_api.xq_api_for_usermanage as ybm_api
import testcases.account.xq_glb as glb
import json
from config.gbl import *

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
        self.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)

    def tearDown(self):
        # 析构方法 退出登录
        '''
        '''

    def test_post_list_query(self):
        '''
        1 [POST] /测试usermanagement接口是否可以通过
        level:1,2,4,5
        '''
        response = self.lesson_object.post_list_query()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_list_query_all(self):
        '''
        1 [POST] / filter all
        level:1,2,4,5
        '''
        response = self.lesson_object.post_list_query_all()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_list_query_all_des(self):
        '''
        1 [POST] / filter all order by first name des
        level:1,2,4,5
        '''
        response = self.lesson_object.post_list_query_all_des()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)


    def test_get_user_permissions(self):
        '''
        1 [POST] /测试usermanagement接口是否可以通过
        level:1,2,4,5
        '''
        response = self.lesson_object.get_user_permissions()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_set_roles_for_user(self):
        '''
         [POST] / set roles for a user
        level:1,2,4,5
        '''
        response = self.lesson_object.post_set_roles_for_user()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_filter_list(self):
        '''
         [POST] / filer list
        level:1,2,4,5
        '''
        response = self.lesson_object.post_filter_list()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_search_users(self):
        '''
         [POST] / search_users
        level:1,2,4,5
        '''
        response = self.lesson_object.post_search_users()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_remove_a_role(self):
        '''
         [POST] / remove a role from a user "Jennifer Sloan"
        level:1,2,4,5
        '''
        response = self.lesson_object.post_remove_a_role()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_post_a_role_suspended(self):
        '''
         [POST] / list roles in org
        level:1,2,4,5
        '''
        response = self.lesson_object.post_a_role_suspended()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)


    def test_post_filter_list_page(self):
        '''
         [POST] / filter list and  pagenumbger and pagesize
        level:1,2,4,5
        '''
        response = self.lesson_object.post_filter_list_page()
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    #反面案例 other error
    def test_usrmanagement_invalid_query(self):
        '''
       1 [POST] /user management Must provide query string. 400
        level:1,2,4,5
        '''
        response = self.lesson_object.post_invalid_query()
        data_dec = glb.rest_o.parse_response(response, glb.CODE500, glb.message)

    def test_no_request_body_query(self):
        '''
       1 [POST] /user management other error  500
        level:1,2,4,5
        '''
        response = self.lesson_object.post_no_request_body_query()
        data_dec = glb.rest_o.parse_response(response, glb.CODE500, glb.message)