# coding=utf-8
import random
import sys
import unittest
import api_call.account.xq_api.xq_api_for_ybm as ybm_api
import testcases.account.xq_glb as glb
# import testcases.account.fep_glb as glb
import nd.rest.http_mot as CoHttpM
import json
from config.gbl import *
from unittest import SkipTest

from data_struct.request_data import RequestData

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

    def test_post_login(self):
        '''
       4.1.1 [GET] /enrollments 预报名活动列表
        level:1,2,4,5
        '''
        # print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        # response = self.lesson_object.get_enrollments()
        # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        response = self.lesson_object.post_login(glb.userId, glb.collection)
        # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # def test_post_enrollments(self):
        #     '''
        #    4.1.2 [POST] /enrollments 创建预报名活动
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.2 [POST] /enrollments 创建预报名活动</p>"
        #     year=glb.year
        #     response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
        #     while response["code"] == 409 :
        #         print "【预报名活动】已存在"
        #         year=year-1
        #         response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
        #
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #     enrollment_id=data_dec["id"]
        #     delete="true"
        #     print "<p>4.1.5 [PATCH] /enrollments/{enrollment_id}/deleted/{deleted} 预报名删除或恢复</p>"
        #     response = self.lesson_object.patch_manage_enrollment_id_deleted(enrollment_id, delete)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #
        # def test_get_enrollments_enrollment_id(self):
        #     '''
        #     case:4.1.3 [GET] /enrollments/{enrollment_id} 获得预报名活动
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"])>0:
        #         enrollment_id=data_dec["items"][0]["id"]
        #         print "<p>4.1.3 [GET] /enrollments/{enrollment_id} 获得预报名活动</p>"
        #         response = self.lesson_object.get_enrollments_enrollment_id(enrollment_id)
        #         data_dec = glb.rest_o.parse_response(response,glb.CODE200,glb.message)
        #
        # def test_put_enrollments_enrollment_id(self):
        #     '''
        #     case:4.1.4 [PUT] /enrollments/{enrollment_id} 修改预报名活动
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments_for_xiugai()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #     i=0
        #     for i in range(len(data_dec["items"])):
        #         isDelete= data_dec["items"][i]["deleted"]
        #         ybm_status = data_dec["items"][i]["status"]
        #
        #         print "isDelete的值：",isDelete
        #         if isDelete or ybm_status == "UNDERWAY" or ybm_status == "END":
        #             i += 1
        #         else:
        #             enrollment_id = data_dec["items"][i]["id"]
        #             ybm_type = data_dec["items"][i]["type"]
        #
        #             if ybm_type == glb.ybm_type_nursery:
        #                 ybm_type=glb.ybm_type_primary
        #             else:
        #                 ybm_type=glb.ybm_type_nursery
        #             print "<p>4.1.4 [PUT] /enrollments/{enrollment_id} 修改预报名活动</p>"
        #             response = self.lesson_object.put_enrollments_enrollment_id(enrollment_id, glb.ybm_name_exchange,
        #                                                                         ybm_type)
        #             if response["code"] == 409:
        #                 print "【预报名活动】已存在"
        #             elif response["code"] == 406:
        #                 print "该活动已删除"
        #             else:
        #                 data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #             break
        #
        #
        #
        # def test_patch_manage_enrollment_id_deleted(self):
        #     '''
        #     4.1.5 [PATCH] /enrollments/{enrollment_id}/deleted/{deleted} 预报名删除或恢复
        #
        #     level:1,2,4,5
        #     '''
        #     # j = 0
        #     # for j in range(2):
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     print response
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     i = 0
        #     for i in range(len(data_dec["items"])):
        #         if data_dec["items"][i]["status"]=="UNSTART" or data_dec["items"][i]["status"]=="UNLAUNCH":
        #             enrollment_id = data_dec["items"][i]["id"]
        #             delete = data_dec["items"][i]["deleted"]
        #             if delete:
        #                 delete = "false";
        #             else:
        #                 delete = "true"
        #             print "<p>4.1.5 [PATCH] /enrollments/{enrollment_id}/deleted/{deleted} 预报名删除或恢复</p>"
        #             response = self.lesson_object.patch_manage_enrollment_id_deleted(enrollment_id, delete)
        #             if response["code"] == 409:
        #                 print "【预报名活动】已存在"
        #                 i += 1
        #             else:
        #                 data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #                 break
        # # j += 1
        #
        #
        # def test_patch_enrollments_enrollment_id_status(self):
        #     '''
        #     4.1.6 [PATCH] /enrollments/{enrollment_id}/status/{status} 预报名投放与取消投放
        #
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     i = 0
        #     for i in range(len(data_dec["items"])):
        #
        #         delete = data_dec["items"][i]["deleted"]
        #         status = data_dec["items"][i]["status"]
        #         start_time = data_dec["items"][i]["start_time"]
        #         end_time = data_dec["items"][i]["end_time"]
        #         if (not delete) and (not (status=="END"))and (start_time is not None)and (end_time is not None)and(end_time>glb.rightTime) :
        #             enrollment_id = data_dec["items"][i]["id"]
        #             status = data_dec["items"][i]["status"]
        #
        #             if status == "UNSTART" or status == "UNDERWAY":
        #                 status = "UNLAUNCH"
        #             else:
        #                 status = "UNSTART"
        #             print status
        #             print "<p>4.1.6 [PATCH] /enrollments/{enrollment_id}/status/{status} 预报名投放与取消投放</p>"
        #
        #             response = self.lesson_object.patch_enrollments_enrollment_id_status(enrollment_id, status)
        #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #             break
        #         else:
        #             i += 1
        #     # j = 0
        #     # for j in range(2):
        #     #
        #     #
        #     # j+=1
        #
        # def test_put_enrollments_enrollment_id_details(self):
        #     '''
        #     4.1.7 [PUT]/enrollments/{enrollment_id}/details 增加或修改预报名活动详情
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #     i = 0
        #     for i in range(len(data_dec["items"])):
        #         delete = data_dec["items"][i]["deleted"]
        #         status = data_dec["items"][i]["status"]
        #         if (not delete) and(status== "UNLAUNCH" or status=="UNSTART"):
        #             enrollment_id = data_dec["items"][i]["id"];
        #             print "<p>4.1.7 [PUT]/enrollments/{enrollment_id}/details 增加或修改预报名活动详情</p>"
        #             response = self.lesson_object.put_enrollments_enrollment_id_details(enrollment_id,glb.enrollments_start_time,glb.enrollments_end_time,glb.need_questionnaire_false)
        #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #             break
        #         else:
        #             i+=1
        #
        # def test_get_user_enrollments(self):
        #     '''
        #     4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
        #     response = self.lesson_object.get_user_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_post_user_enrollments_actions_query(self):
        #     '''
        #    4.1.9 [POST]]/user_enrollments/actions/query 预报名审批列表
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
        #     response = self.lesson_object.get_user_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"]) > 0:
        #         enrollment_id = data_dec["items"][0]["enrollment_id"]
        #         print "<p>4.1.9 [POST]]/user_enrollments/actions/query 预报名审批列表</p>"
        #         response = self.lesson_object.post_user_enrollments_actions_query(enrollment_id)
        #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_patch_user_enrollments_user_enrollment_id_revocation(self):
        #     '''
        #      4.1.10 [PATCH] /user_enrollments/{user_enrollment_id}/revocation 撤销报名
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
        #     response = self.lesson_object.get_user_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     i = 0
        #     for i in range(len(data_dec["items"])):
        #         accepted = data_dec["items"][i]["accepted"]
        #
        #         if accepted=="AUDIT":
        #             user_enrollment_id = data_dec["items"][i]["id"]
        #             print "user_enrollment_id:" + user_enrollment_id
        #             print "<p>4.1.10 [PATCH] /user_enrollments/{user_enrollment_id}/revocation 撤销报名</p>"
        #             response = self.lesson_object.patch_user_enrollments_user_enrollment_id_revocation(user_enrollment_id)
        #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #             break
        #     i+=1
        #
        #
        #
        #
        # def test_patch_user_enrollments_user_enrollment_id_saw(self):
        #     '''
        #      4.1.11 [PATCH] /user_enrollments/{user_enrollment_id}/saw 已读操作
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
        #     response = self.lesson_object.get_user_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"])>0:
        #         user_enrollment_id=data_dec["items"][0]["id"]
        #         print "<p>4.1.11 [PATCH] /user_enrollments/{user_enrollment_id}/saw 已读操作</p>"
        #         response = self.lesson_object.patch_user_enrollments_user_enrollment_id_saw(user_enrollment_id)
        #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #
        # def test_post_visit(self):
        #     '''
        #    4.1.12 [POST] /visit 是否首次登录
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.12 [POST] /visit 是否首次登录</p>"
        #     response = self.lesson_object.post_visit()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #
        # def test_post_user_enrollments(self):
        #     '''
        #   4.1.13 [POST] /user_enrollments 提交预报名
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     i=0
        #     for i in range(len(data_dec["items"])):
        #
        #         if(data_dec["items"][i]["status"]=="UNDERWAY")  and (not data_dec["items"][i]["deleted"]) and (not data_dec["items"][i]["need_questionnaire"]):
        #             enrollment_id=data_dec["items"][i]["id"]
        #             print "<p>4.1.13 [POST] /user_enrollments 提交预报名</p>"
        #             response = self.lesson_object.post_user_enrollments(enrollment_id,glb.id_number)
        #             if response["code"]==406:
        #                 print "该幼儿已提交了该园所的预报名信息，请勿重复提交"
        #                 data_dec = glb.rest_o.parse_response(response, glb.CODE406, glb.message)
        #             else:
        #                 data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #             break
        #         i+=1
        #
        # def test_get_user_enrollments_actions_check_repeat(self):
        #     '''
        #     4.1.14 [GET] /user_enrollments/actions/check_repeat 检查重复报名
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"])>0:
        #         enrollment_id=data_dec["items"][0]["id"]
        #         print "<p>4.1.14 [GET] /user_enrollments/actions/check_repeat 检查重复报名</p>"
        #         response = self.lesson_object.get_user_enrollments_actions_check_repeat(glb.id_number,enrollment_id)
        #         if response["code"]==406:
        #             print "该幼儿已提交了该园所的预报名信息，请勿重复提交"
        #         else:
        #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #
        # def test_get_enrollments_summaries(self):
        #     '''
        #     4.1.15 [GET] /enrollments/summaries 预报名活动概要列表(不分页)
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.15 [GET] /enrollments/summaries 预报名活动概要列表(不分页)</p>"
        #     response = self.lesson_object.get_enrollments_summaries()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_patch_user_enrollments_batch(self):
        #     '''
        #     4.1.16 [PATCH] /user_enrollments/batch审核
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
        #     response = self.lesson_object.get_user_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     i = 0
        #     for i in range(len(data_dec["items"])):
        #         accepted = data_dec["items"][i]["accepted"]
        #
        #         if accepted == "AUDIT":
        #             user_enrollment_id = data_dec["items"][i]["id"]
        #             print "user_enrollment_id:" + user_enrollment_id
        #             print "<p>4.1.16 [PATCH] /user_enrollments/batch审核</p>"
        #             response = self.lesson_object.patch_user_enrollments_batch(user_enrollment_id)
        #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #             break
        #     i += 1
        # def test_get_user_enrollments_export_payments(self):
        #     '''
        #     4.1.17 [GET]]/user_enrollments/export/payments 导出缴费列表
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"])>0:
        #         enrollment_id=data_dec["items"][0]["id"]
        #         print "<p>4.1.17 [GET]]/user_enrollments/export/payments 导出缴费列表</p>"
        #         response = self.lesson_object.get_user_enrollments_export_payments(enrollment_id)
        #         print response
        #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_post_user_enrollments_export_approvals(self):
        #     '''
        #     4.1.18 [POST]/user_enrollments/export/approvals 导出已录取审批列表
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        #     response = self.lesson_object.get_enrollments()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"])>0:
        #         enrollment_id = data_dec["items"][0]["id"]
        #         print "<p>4.1.18 [POST]]/user_enrollments/export/approvals 导出已录取审批列表</p>"
        #         response = self.lesson_object.post_user_enrollments_export_approvals(enrollment_id)
        #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_post_post_enrollments_questionnaires(self):
        #     '''
        #    4.1.19 [POST] /enrollments/questionnaires 预报名活动问卷新增
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.3.1 [POST] /questions 问题新增</p>"
        #     response = self.lesson_object.post_questions()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #     question_id = data_dec["id"]
        #
        #     print "<p>4.1.2 [POST] /enrollments 创建预报名活动</p>"
        #     year=glb.year
        #     response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
        #     while response["code"] == 409 :
        #         print "【预报名活动】已存在"
        #         year=year-1
        #         response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
        #     data_dec_1 = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #     enrollment_id=data_dec_1["id"]
        #
        #     print "<p>4.1.19 [POST] /enrollments/questionnaires 预报名活动问卷新增</p>"
        #     response = self.lesson_object.post_enrollments_questionnaires(question_id, enrollment_id)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #
        #     delete="true"
        #     print "<p>4.1.5 [PATCH] /enrollments/{enrollment_id}/deleted/{deleted} 预报名删除或恢复</p>"
        #     response = self.lesson_object.patch_manage_enrollment_id_deleted(enrollment_id, delete)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #     print "<p>4.3.3 [DELETE] /questions/{question_id}问题删除</p>"
        #     response = self.lesson_object.delete_questions_question_id(question_id)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE204, glb.message)
        #
        #
        #
        #
        #
        # def test_post_users_personal_infoes(self):
        #     '''
        #    4.2.1 [POST] /users/personal_infoes 创建用户的家长/幼儿的基本信息
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.2.1 [POST] /users/personal_infoes 创建用户的家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.post_users_personal_infoes(glb.id_number)
        #     while response["code"] == 409:
        #         id_number=''.join(str(random.choice(range(10))) for _ in range(20))
        #         response = self.lesson_object.post_users_personal_infoes(id_number)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     print "<p>4.2.3 [DELETE] /users/personal_infoes/{info_id} 删除家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.delete_users_personal_infoes_info_id(data_dec["id"])
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_put_users_personal_infoes_id(self):
        #     '''
        #    4.2.2 [PUT] /users/personal_infoes/{id} 创建/修改用户的家长/幼儿的基本信息
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.2.1 [POST] /users/personal_infoes 创建用户的家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.post_users_personal_infoes(glb.id_number)
        #     while response["code"] == 409:
        #         id_number=''.join(str(random.choice(range(10))) for _ in range(20))
        #         response = self.lesson_object.post_users_personal_infoes(id_number)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #
        #     print "<p> 4.2.2 [PUT] /users/personal_infoes/{id} 创建/修改用户的家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.put_users_personal_infoes_id(data_dec["id"],data_dec["id_number"])
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #     print "<p>4.2.3 [DELETE] /users/personal_infoes/{info_id} 删除家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.delete_users_personal_infoes_info_id(data_dec["id"])
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_delete_users_personal_infoes_info_id(self):
        #     '''
        #    4.2.3 [DELETE] /users/personal_infoes/{info_id} 删除家长/幼儿的基本信息
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.2.1 [POST] /users/personal_infoes 创建用户的家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.post_users_personal_infoes(glb.id_number)
        #     while response["code"] == 409:
        #         id_number = ''.join(str(random.choice(range(10))) for _ in range(20))
        #         response = self.lesson_object.post_users_personal_infoes(id_number)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     print "<p>4.2.3 [DELETE] /users/personal_infoes/{info_id} 删除家长/幼儿的基本信息</p>"
        #     response = self.lesson_object.delete_users_personal_infoes_info_id(data_dec["id"])
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_get_users_personal_infoes(self):
        #     '''
        #   4.2.4 [GET] /users/personal_infoes 获取用户的基本信息列表。
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.2.4 [GET] /users/personal_infoes 获取用户的基本信息列表。</p>"
        #     response = self.lesson_object.get_users_personal_infoes()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        # def test_get_users_personal_infoes_enrollments_ids(self):
        #     '''
        #    4.2.5 [GET] /users/personal_infoes/enrollments?ids={id1,id2,……} 获取用户报名活动的基本信息
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.2.4 [GET] /users/personal_infoes 获取用户的基本信息列表。</p>"
        #     response = self.lesson_object.get_users_personal_infoes()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     if len(data_dec["items"])>0:
        #         id=data_dec["items"][0]["id"]
        #         print "<p> 4.2.5 [GET] /users/personal_infoes/enrollments?ids={id1,id2,……} 获取用户报名活动的基本信息</p>"
        #         response = self.lesson_object.get_users_personal_infoes_enrollments_ids(id)
        #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #
        #
        #
        # # ============================================4.3 自评部分========================================
        #
        # def test_post_questions(self):
        #     '''
        #    4.3.1 [POST] /questions 问题新增
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.3.1 [POST] /questions 问题新增</p>"
        #     response = self.lesson_object.post_questions()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #
        # def test_put_questions_question_id(self):
        #     '''
        #    4.3.2 [PUT] /questions/{question_id} 问题更新
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.3.1 [POST] /questions 问题新增</p>"
        #     response = self.lesson_object.post_questions()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #     question_id = data_dec["id"]
        #     print "<p>4.3.2 [PUT] /questions/{question_id} 问题更新</p>"
        #     response = self.lesson_object.put_questions_question_id(question_id)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        #     print "<p>4.3.3 [DELETE] /questions/{question_id}问题删除</p>"
        #     response = self.lesson_object.delete_questions_question_id(question_id)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE204, glb.message)
        # def test_delete_questions_question_id(self):
        #     '''
        #    4.3.3 [DELETE] /questions/{question_id}问题删除
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.3.1 [POST] /questions 问题新增</p>"
        #     response = self.lesson_object.post_questions()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #     question_id = data_dec["id"]
        #     print "<p>4.3.3 [DELETE] /questions/{question_id}问题删除</p>"
        #     response = self.lesson_object.delete_questions_question_id(question_id)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE204, glb.message)
        #
        # def test_post_questions_batch_delete(self):
        #     '''
        #    4.3.4 [POST] /questions/batch_delete 问题删除--批量-pass
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.3.1 [POST] /questions 问题新增</p>"
        #     response = self.lesson_object.post_questions()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
        #     question_id = data_dec["id"]
        #     print "<p> 4.3.4 [POST] /questions/batch_delete 问题删除--批量</p>"
        #     response = self.lesson_object.post_questions_batch_delete(question_id)
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE204, glb.message)
        #
        # def test_get_questions(self):
        #     '''
        #    4.3.5 [GET] /questions 获取问题列表
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
        #     response = self.lesson_object.get_questions()
        #     data_dec = glb.rest_o.parse_response(response, glb.CODE200,glb.message)
        #
        # def test_get_user_questionnaire_answers_statistics_target_id(self):
        #     '''
        #    4.3.6 [GET] /user_questionnaire_answers/statistics?target_id={target_id} 用户问答统计
        #     level:1,2,4,5
        #     '''
        #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
        response = self.lesson_object.get_enrollments()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     i = 0
    #     for i in range(len(data_dec["items"])):
    #         delete = data_dec["items"][i]["deleted"]
    #         status = data_dec["items"][i]["status"]
    #         questionnaire_id = data_dec["items"][i]["questionnaire_id"]
    #         if (not delete) and(status== "UNDERWAY")and (questionnaire_id is not None):
    #             enrollment_id = data_dec["items"][i]["id"];
    #             break
    #         else:
    #             i+=1
    #     if i==len(data_dec["items"]):
    #         print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
    #         response = self.lesson_object.get_enrollments()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #         i = 0
    #         for i in range(len(data_dec["items"])):
    #             delete = data_dec["items"][i]["deleted"]
    #             status = data_dec["items"][i]["status"]
    #             questionnaire_id = data_dec["items"][i]["questionnaire_id"]
    #             if (not delete) and (status == "UNLAUNCH" or status == "UNSTART")and (questionnaire_id is not None):
    #                 enrollment_id = data_dec["items"][i]["id"];
    #                 print "<p>4.1.7 [PUT]/enrollments/{enrollment_id}/details 增加或修改预报名活动详情</p>"
    #                 response = self.lesson_object.put_enrollments_enrollment_id_details(enrollment_id,
    #                                                                                     glb.enrollments_start_time,
    #                                                                                     glb.enrollments_end_time,
    #                                                                                     glb.need_questionnaire_true)
    #                 data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #                 break
    #             else:
    #                 i += 1
    #         print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #         response = self.lesson_object.get_questions()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"]) > 0:
    #             key = data_dec["items"][0]["id"]
    #             print "<p>4.1.19 [POST] /enrollments/questionnaires 预报名活动问卷新增</p>"
    #             response = self.lesson_object.post_enrollments_questionnaires(key, enrollment_id)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #             questionnaire_id = data_dec["id"]
    #             print "<p>4.1.6 [PATCH] /enrollments/{enrollment_id}/status/{status} 预报名投放与取消投放</p>"
    #             status = "UNSTART "
    #             response = self.lesson_object.patch_enrollments_enrollment_id_status(enrollment_id, status)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #             print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #             response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, key)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #
    #
    #
    #     print "<p>4.3.6 [GET] /user_questionnaire_answers/statistics?target_id={target_id} 用户问答统计</p>"
    #     response = self.lesson_object.get_user_questionnaire_answers_statistics_target_id(enrollment_id)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #
    #
    #
    # def test_post_questionnaires(self):
    #     '''
    #    4.3.7 [POST] /questionnaires 入园自评问卷新增
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #     response = self.lesson_object.get_questions()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #
    #     if len(data_dec["items"])>0:
    #         question_id=data_dec["items"][0]["id"]
    #         response = self.lesson_object.get_enrollments()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"])>0:
    #             target_id=data_dec["items"][0]["id"]
    #         print "<p>4.3.7 [POST] /questionnaires 入园自评问卷新增</p>"
    #         response = self.lesson_object.post_questionnaires(question_id,target_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201,glb.message)
    #
    # def test_put_questionnaires_questionnaire_id(self):
    #     '''
    #    4.3.8 [PUT] /questionnaires/{questionnaire_id} 入园自评问卷更新
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #     response = self.lesson_object.get_questions()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #
    #     if len(data_dec["items"])>0:
    #         question_id=data_dec["items"][0]["id"]
    #         response = self.lesson_object.get_enrollments()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"])>0:
    #             target_id=data_dec["items"][0]["id"]
    #         print "<p>4.3.7 [POST] /questionnaires 入园自评问卷新增</p>"
    #         response = self.lesson_object.post_questionnaires(question_id,target_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201,glb.message)
    #         questionnaire_id=data_dec["id"]
    #         print "<p>4.3.8 [PUT] /questionnaires/{questionnaire_id} 入园自评问卷更新</p>"
    #         response = self.lesson_object.put_questionnaires_questionnaire_id(questionnaire_id,question_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    # def test_get_questionnaires_questionnaire_id(self):
    #     '''
    #    4.3.9 [GET] /questionnaires/{questionnaire_id} 获取入园自评问卷
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #     response = self.lesson_object.get_questions()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     if len(data_dec["items"]) > 0:
    #         question_id = data_dec["items"][0]["id"]
    #         response = self.lesson_object.get_enrollments()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"]) > 0:
    #             target_id = data_dec["items"][0]["id"]
    #         print "<p>4.3.7 [POST] /questionnaires 入园自评问卷新增</p>"
    #         response = self.lesson_object.post_questionnaires(question_id, target_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #         questionnaire_id = data_dec["id"]
    #         print "<p>4.3.9 [GET] /questionnaires/{questionnaire_id} 获取入园自评问卷</p>"
    #         response = self.lesson_object.get_questionnaires_questionnaire_id(questionnaire_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    # def test_post_user_questionnaire_answers(self):
    #     '''
    #    4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
    #     response = self.lesson_object.get_enrollments()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     i = 0
    #     for i in range(len(data_dec["items"])):
    #         delete = data_dec["items"][i]["deleted"]
    #         status = data_dec["items"][i]["status"]
    #         questionnaire_id = data_dec["items"][i]["questionnaire_id"]
    #         if (not delete) and(status== "UNDERWAY")and (questionnaire_id is not None):
    #             enrollment_id = data_dec["items"][i]["id"];
    #             break
    #         else:
    #             i+=1
    #     if i==len(data_dec["items"]):
    #         print "<p>4.1.2 [POST] /enrollments 创建预报名活动</p>"
    #         year = 2025
    #         response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
    #         while response["code"] == 409:
    #             print "【预报名活动】已存在"
    #             year = year - 1
    #             response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
    #
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #         enrollment_id = data_dec["id"]
    #         print "<p>4.1.7 [PUT]/enrollments/{enrollment_id}/details 增加或修改预报名活动详情</p>"
    #         response = self.lesson_object.put_enrollments_enrollment_id_details(enrollment_id,
    #                                                                             glb.enrollments_start_time,
    #                                                                             glb.enrollments_end_time,
    #                                                                             glb.need_questionnaire_true)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #         response = self.lesson_object.get_questions()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"]) > 0:
    #             key = data_dec["items"][0]["id"]
    #             print "<p>4.1.19 [POST] /enrollments/questionnaires 预报名活动问卷新增</p>"
    #             response = self.lesson_object.post_enrollments_questionnaires(key, enrollment_id)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #             questionnaire_id = data_dec["id"]
    #             print "<p>4.1.6 [PATCH] /enrollments/{enrollment_id}/status/{status} 预报名投放与取消投放</p>"
    #             status = "UNSTART "
    #             response = self.lesson_object.patch_enrollments_enrollment_id_status(enrollment_id, status)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #             print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #             response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, key)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #
    #     else:
    #         print "<p>4.3.9 [GET] /questionnaires/{questionnaire_id} 获取入园自评问卷</p>"
    #         response = self.lesson_object.get_questionnaires_questionnaire_id(questionnaire_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         i = 0
    #         idList = dict()
    #         for i in range(len(data_dec["questions"])):
    #             idList["key"] = data_dec["questions"][i]["id"]
    #             idList["value"] = "A"
    #         answers = list()
    #         answers.append(idList)
    #         print answers
    #         print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #         response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, answers)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #
    #
    # def test_put_user_questionnaire_answers_user_questionnaire_answer_id(self):
    #     '''
    #    4.3.11 [PUT] /user_questionnaire_answers/{user_questionnaire_answer_id} 更新用户问卷回答信息
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
    #     response = self.lesson_object.get_enrollments()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     i = 0
    #     for i in range(len(data_dec["items"])):
    #         delete = data_dec["items"][i]["deleted"]
    #         status = data_dec["items"][i]["status"]
    #         questionnaire_id = data_dec["items"][i]["questionnaire_id"]
    #         if (not delete) and (status == "UNDERWAY") and (questionnaire_id is not None):
    #             enrollment_id = data_dec["items"][i]["id"];
    #             break
    #         else:
    #             i += 1
    #     if i == len(data_dec["items"]):
    #         print "<p>4.1.2 [POST] /enrollments 创建预报名活动</p>"
    #         year = 2025
    #         response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
    #         while response["code"] == 409:
    #             print "【预报名活动】已存在"
    #             year = year - 1
    #             response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
    #
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #         enrollment_id = data_dec["id"]
    #         print "<p>4.1.7 [PUT]/enrollments/{enrollment_id}/details 增加或修改预报名活动详情</p>"
    #         response = self.lesson_object.put_enrollments_enrollment_id_details(enrollment_id,
    #                                                                             glb.enrollments_start_time_underway,
    #                                                                             glb.enrollments_end_time,
    #                                                                             glb.need_questionnaire_true)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #         response = self.lesson_object.get_questions()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"]) > 0:
    #             key = data_dec["items"][0]["id"]
    #             print "<p>4.1.19 [POST] /enrollments/questionnaires 预报名活动问卷新增</p>"
    #             response = self.lesson_object.post_enrollments_questionnaires(key, enrollment_id)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #             questionnaire_id = data_dec["id"]
    #             print "<p>4.1.6 [PATCH] /enrollments/{enrollment_id}/status/{status} 预报名投放与取消投放</p>"
    #             status = "UNSTART "
    #             response = self.lesson_object.patch_enrollments_enrollment_id_status(enrollment_id, status)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #             print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #             response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, key)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #             user_questionnaire_answer_id = data_dec["id"]
    #             print "<p>4.3.11 [PUT] /user_questionnaire_answers/{user_questionnaire_answer_id} 更新用户问卷回答信息</p>"
    #             response = self.lesson_object.put_user_questionnaire_answers_user_questionnaire_answer_id(
    #                 user_questionnaire_answer_id, key)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     else:
    #         print "<p>4.3.9 [GET] /questionnaires/{questionnaire_id} 获取入园自评问卷</p>"
    #         response = self.lesson_object.get_questionnaires_questionnaire_id(questionnaire_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         i = 0
    #         idList = dict()
    #         for i in range(len(data_dec["questions"])):
    #             idList["key"] = data_dec["questions"][i]["id"]
    #             idList["value"] = "A"
    #         answers = list()
    #         answers.append(idList)
    #
    #         print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #         response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, answers)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #
    #         user_questionnaire_answer_id = data_dec["id"]
    #         print "<p>4.3.11 [PUT] /user_questionnaire_answers/{user_questionnaire_answer_id} 更新用户问卷回答信息</p>"
    #         response = self.lesson_object.put_user_questionnaire_answers_user_questionnaire_answer_id(
    #             user_questionnaire_answer_id, answers)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #
    # def test_get_user_questionnaire_answers_user_questionnaire_answer_id(self):
    #     '''
    #     4.3.12 [GET] /user_questionnaire_answers/{user_questionnaire_answer_id} 获取用户问卷自评回答
    #     level:1,2,4,5
    #     '''
    #
    #     print "<p>4.1.1 [GET] /enrollments 预报名活动列表</p>"
    #     response = self.lesson_object.get_enrollments()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     i = 0
    #     for i in range(len(data_dec["items"])):
    #         delete = data_dec["items"][i]["deleted"]
    #         status = data_dec["items"][i]["status"]
    #         questionnaire_id = data_dec["items"][i]["questionnaire_id"]
    #         if (not delete) and (status == "UNDERWAY") and (questionnaire_id is not None):
    #             enrollment_id = data_dec["items"][i]["id"];
    #             print "预报名活动id "+enrollment_id
    #             break
    #         else:
    #             i += 1
    #     if i == len(data_dec["items"]):
    #         print "<p>4.1.2 [POST] /enrollments 创建预报名活动</p>"
    #         year = glb.year
    #         response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
    #         while response["code"] == 409:
    #             print "【预报名活动】已存在"
    #             year = year - 1
    #             response = self.lesson_object.post_enrollments(glb.ybm_name, glb.ybm_type_nursery, year)
    #
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #         enrollment_id = data_dec["id"]
    #         print "<p>4.1.7 [PUT]/enrollments/{enrollment_id}/details 增加或修改预报名活动详情</p>"
    #         response = self.lesson_object.put_enrollments_enrollment_id_details(enrollment_id,
    #                                                                             glb.enrollments_start_time_underway,
    #                                                                             glb.enrollments_end_time,
    #                                                                             glb.need_questionnaire_true)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         print "<p>4.3.5 [GET] /questions 获取问题列表</p>"
    #         response = self.lesson_object.get_questions()
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         if len(data_dec["items"]) > 0:
    #             key = data_dec["items"][0]["id"]
    #             print "<p>4.1.19 [POST] /enrollments/questionnaires 预报名活动问卷新增</p>"
    #             response = self.lesson_object.post_enrollments_questionnaires(key, enrollment_id)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #             questionnaire_id = data_dec["id"]
    #             print "<p>4.1.6 [PATCH] /enrollments/{enrollment_id}/status/{status} 预报名投放与取消投放</p>"
    #             status = "UNSTART "
    #             response = self.lesson_object.patch_enrollments_enrollment_id_status(enrollment_id, status)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #             print(enrollment_id,questionnaire_id)
    #             print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #             response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, key)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #             user_questionnaire_answer_id = data_dec["id"]
    #             print "<p>4.3.12 [GET] /user_questionnaire_answers/{user_questionnaire_answer_id} 获取用户问卷自评回答</p>"
    #             response = self.lesson_object.get_user_questionnaire_answers_user_questionnaire_answer_id(
    #                 user_questionnaire_answer_id)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    #     else:
    #         print "<p>4.3.9 [GET] /questionnaires/{questionnaire_id} 获取入园自评问卷</p>"
    #         response = self.lesson_object.get_questionnaires_questionnaire_id(questionnaire_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         print "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
    #         if data_dec["status"]=="UNDERWAY":
    #             i = 0
    #             idList = dict()
    #             answers = []
    #             for i in range(len(data_dec["questions"])):
    #                 idList["key"] = data_dec["questions"][i]["id"]
    #                 idList["value"] = "A"
    #                 i = i + 1
    #                 answers.append(idList)
    #                 print "xxxxxxxxxxxxxxxxxxxxxxxxx"
    #             print "<p>4.3.10 [POST] /user_questionnaire_answers 提交用户问卷回答信息</p>"
    #             response = self.lesson_object.post_user_questionnaire_answers(enrollment_id, questionnaire_id, answers)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #
    #             user_questionnaire_answer_id = data_dec["id"]
    #             print "<p>4.3.12 [GET] /user_questionnaire_answers/{user_questionnaire_answer_id} 获取用户问卷自评回答</p>"
    #             response = self.lesson_object.get_user_questionnaire_answers_user_questionnaire_answer_id(
    #                 user_questionnaire_answer_id)
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #         else:
    #             data_dec = glb.rest_o.parse_response(response, glb.CODE400, glb.message)
    #             print "不是进行中的问卷不能作答"
    #
    #
    # def test_post_user_enrollments_user_enrollment_id_payments(self):
    #     '''
    #   4.4.1 创建订单 [POST] /user_enrollments/{user_enrollment_id}/payments
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
    #     response = self.lesson_object.get_user_enrollments()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #     if len(data_dec["items"])>0:
    #         user_enrollment_id=data_dec["items"][0]["id"]
    #         print "<p>4.4.1 创建订单 [POST] /user_enrollments/{user_enrollment_id}/payments</p>"
    #         response = self.lesson_object.post_user_enrollments_user_enrollment_id_payments(user_enrollment_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #         print "<p>4.4.2 取消订单 [PUT] /order/{order_id}/actions/close</p>"
    #         order_id=data_dec["pay_params"]["order_id"]
    #         response = self.lesson_object.put_order_order_actions_close(order_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    # def test_put_order_order_actions_close(self):
    #     '''
    #   4.4.2 取消订单 [PUT] /order/{order_id}/actions/close
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.1.8 [GET]]/user_enrollments我的预报名列表/缴费列表</p>"
    #     response = self.lesson_object.get_user_enrollments()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #     if len(data_dec["items"])>0:
    #         user_enrollment_id=data_dec["items"][0]["id"]
    #         print "<p>4.4.1 创建订单 [POST] /user_enrollments/{user_enrollment_id}/payments</p>"
    #         response = self.lesson_object.post_user_enrollments_user_enrollment_id_payments(user_enrollment_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE201, glb.message)
    #         print "<p>4.4.2 取消订单 [PUT] /order/{order_id}/actions/close</p>"
    #         order_id=data_dec["pay_params"]["order_id"]
    #         response = self.lesson_object.put_order_order_actions_close(order_id)
    #         data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #
    # def test_get_cs_sessions(self):
    #     '''
    #    4.5.1 [GET] /cs/sessions 获以内容服务Session
    #     level:1,2,4,5
    #     '''
    #     print "<p>4.5.1 [GET] /cs/sessions 获以内容服务Session</p>"
    #     response = self.lesson_object.get_cs_sessions()
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)


if __name__ == "__main__":
    pass
