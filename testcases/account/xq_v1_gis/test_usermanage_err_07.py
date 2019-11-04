# coding=utf-8

import api_call.account.xq_api.xq_api_for_usermanage_auth_err_07 as ybm_api
import testcases.account.xq_glb as glb
from config.gbl import *
import unittest
import random
import ddt
import datetime

__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')

@ddt.ddt
class UserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    # 获取组织名称
    def get_org_name(self):
        # 搜索获取组织唯一名称
        _search_message = '搜索获取组织失败'
        response = self.lesson_object.search_orgs()  # 请求搜索组织 //ApiTest
        data = glb.rest_o.parse_response(response, glb.CODE200, _search_message)

        # 获取名称
        org_name = "prn:Organization::08A62000OOOk"  # 默认强制给一个平台存在'08A62000OOOk'
        orgs_list = data.get('data').get('searchOrgs').get('orgs')
        for i in orgs_list:  # [{}]  //只循环1次
            if i['prn'] == 'prn:Organization::ApiTest':
                org_name = i['prn']
            else:
                raise ValueError(' Org ApiTest is deleted or is alter')
        return org_name

    # 获取email
    def get_email_info(self):

        emails = list()
        _message = "获取活动日志user和活动信息失败"
        response = self.lesson_object.get_user_and_admin_info()
        data = glb.rest_o.parse_response(response, glb.CODE200, _message)
        admins = data.get('data').get('searchPromAdmins').get('admins')
        for admin in admins:
            emails.append(admin.get('email'))
        return emails


    def test_get_org_list(self):
        """
            获取列表详情[POST]
        """
        message = '获取列表失败'
        response = self.lesson_object.get_org_list()
        glb.rest_o.parse_response(response, glb.CODE200, message)

    def test_org_status_list(self):
        """
            状态获取列表[POST]
        """
        message = '状态获取列表'
        response = self.lesson_object.org_status_list()
        glb.rest_o.parse_response(response, glb.CODE200, message)

    def test_search_orgs(self):
        """
            搜索获取列表[POST]
        """
        message = '搜索获取列表'
        response = self.lesson_object.search_orgs()
        glb.rest_o.parse_response(response, glb.CODE200, message)

    def test_get_org_details(self):
        """
            获取某个组织详情[POST]
        """
        org_name = self.get_org_name()
        # 获取组织详情  //ApiTest
        _message = '获取组织详情失败'
        response = self.lesson_object.get_org_details(org_name)
        glb.rest_o.parse_response(response, glb.CODE200, _message)

    def test_add_domain_info(self):
        """
            添加domian[POST]
        """
        org_name = self.get_org_name()

        domain_name = "api_test_01.com"
        _message = '添加domain失败'
        response = self.lesson_object.add_domain_info(org_name, domain_name)
        glb.rest_o.parse_response(response, glb.CODE200, _message)

    def test_del_domain_info(self):
        """
            删除domain[POST]
        """
        # 获取{api test}组织详情
        org_name = self.get_org_name() # "prn:Organization::ApiTest"
        _message = '获取组织详情失败'
        response = self.lesson_object.get_org_details(org_name)
        data = glb.rest_o.parse_response(response, glb.CODE200, _message)

        # 获取domains
        domains = data.get('data').get('getOrgDetails').get('domains')
        print("<p>{}</p>\n".format(domains))
        _del_message = '删除domain失败'
        if domains:
            for domain in domains: # 删除所有domain
                response = self.lesson_object.del_domain_info(org_name, domain.get("name"))
                glb.rest_o.parse_response(response, glb.CODE200, _del_message)
                time.sleep(1.0)
        else:
            # 添加domain后再删除
            org_name = self.get_org_name()
            domain_name = "api_test_01.com"
            _message = '添加domain失败'
            response = self.lesson_object.add_domain_info(org_name, domain_name)
            glb.rest_o.parse_response(response, glb.CODE200, _message)

            # 重跑删除domain
            self.test_del_domain_info()

    # 添加组织管理员
    def test_add_org_admin(self):
        """
            添加组织管理员[POST]
        """
        # 获取{api test}组织详情
        org_name = self.get_org_name()  # "prn:Organization::ApiTest"
        _message = '获取组织详情失败'
        response = self.lesson_object.get_org_details(org_name)
        data = glb.rest_o.parse_response(response, glb.CODE200, _message)

        # 获取已添加的admins
        admins_exist = data.get('data').get('getOrgDetails').get('admins')

        # 剔除已添加的admin
        admins = self.get_email_info()
        if not admins_exist:
            for admin_exist in admins_exist:
                if admin_exist.get('email') in admins:
                    admins.remove(admin_exist.get('email'))


        org_name = self.get_org_name()  # "prn:Organization::ApiTest"
        _message = '添加组织管理员失败'

        for i in xrange(0, random.randint(1, 3)):  # 暂时最多添加4个，admins剔除4个剩16，不管先跑删除，还是先跑添加，第2天跑都能通过
            admin = random.choice(admins)
            response = self.lesson_object.add_org_admin(org_name, admin)
            glb.rest_o.parse_response(response, glb.CODE200, _message)
            time.sleep(1.5)
            admins.remove(admin) # 新添加过剔除，不在添加

    # 删除组织管理员
    def test_del_org_admins(self):
        """
            删除组织管理员[POST]
        """
        # 获取{api test}组织详情
        org_name = self.get_org_name()  # "prn:Organization::ApiTest"
        _message = '获取组织详情失败'
        response = self.lesson_object.get_org_details(org_name)
        data = glb.rest_o.parse_response(response, glb.CODE200, _message)

        # 获取已添加的admins
        admins_exist = data.get('data').get('getOrgDetails').get('admins')

        admins = self.get_email_info()

        _message_del = '删除组织管理员失败'
        _message_add = '添加组织管理员失败'

        if len(admins_exist) == 0: # 先添加组织管理员  // 但不存在此逻辑，会先跑添加
            admin = random.choice(admins)
            response = self.lesson_object.add_org_admin(org_name, admin)
            glb.rest_o.parse_response(response, glb.CODE200, _message_add)
            time.sleep(2.0)

            # 删除admin
            response = self.lesson_object.del_org_admins(org_name, admin)
            glb.rest_o.parse_response(response, glb.CODE200, _message_del)

        elif len(admins_exist) < 4:  # 少于4个随机删除个数
            admin = list()
            for i in range(0, random.randint(1, len(admins_exist))):
                admin.append(admins_exist[i].get('email'))

            response = self.lesson_object.del_org_admins(org_name, admin)
            glb.rest_o.parse_response(response, glb.CODE200, _message_del)

        else:
            # 请场所有admin
            admin = list()
            for i in range(0, len(admins_exist)):
                admin.append(admins_exist[i].get('email'))
            response = self.lesson_object.del_org_admins(org_name, admin)
            glb.rest_o.parse_response(response, glb.CODE200, _message_del)

    # 获取活动日志列表
    def test_activity_log_list(self):
        """
           获取活动日志列表[POST]
        """
        page_size = random.choice([25, 50, 100])
        _message = "获取活动日志列表失败"
        response = self.lesson_object.activity_log_list(page_size=page_size)
        data = glb.rest_o.parse_response(response, glb.CODE200, _message)

        # 获取页数，随机请求第N页的资源
        total_pages = data.get('data').get('searchAudits').get('totalPages')
        response = self.lesson_object.activity_log_list(random.randint(0, total_pages-1), page_size)
        glb.rest_o.parse_response(response, glb.CODE200, _message)

    # 搜索活动日志
    @ddt.data(*[{"search_string": "api test"},{"search_string": "renjin"}])
    def test_search_activity_log(self, data):
        """
            搜索活动日志[POST]
        """
        _message = "搜索活动日志失败"
        search_string = data["search_string"]
        response = self.lesson_object.activity_log_list(search_string=search_string)
        glb.rest_o.parse_response(response, glb.CODE200, _message)

    # 获取活动日志user和活动信息
    def test_get_user_and_admin_info(self):
        """
            获取活动日志user和活动信息[POST]
        """
        _message = "获取活动日志user和活动信息失败"
        response = self.lesson_object.get_user_and_admin_info()
        glb.rest_o.parse_response(response, glb.CODE200, _message)

    # 筛选活动日志
    def test_filter_activity_log(self):
        """
            筛选活动日志[POST]
        """

        _message = "获取活动日志user和活动信息失败"
        response = self.lesson_object.get_user_and_admin_info()
        data = glb.rest_o.parse_response(response, glb.CODE200, _message)
        time.sleep(1.0)

        # 获取actor_ids和event_names
        event_names = []
        actor_ids = data.get('data').get('getAuditEventNames')
        admins = data.get('data').get('searchPromAdmins').get("admins")
        for admin in admins:
            event_names.append(admin.get('id'))

        # 处理筛选的actor_id
        actor_id_order = random.sample(actor_ids, random.randint(0, len(actor_ids)))  # ["",""]
        if actor_id_order :
            actor_id = None
        else:
            actor_id = actor_id_order

        # 处理筛选的event_name
        if len(event_names) >= 5:
            munber = 5
        else:
            munber = len(event_names)
        event_name_order = random.sample(event_names, random.randint(0, munber)) # ["",""]
        if event_name_order:
            event_name = None
        else:
            event_name = event_name_order

        # 处理日期
        time_type = random.choice(["today", "past day", "past week", "past 30 days", "past year", None])

        if time_type == "today":
            log_time = {
                "from": (datetime.datetime.now() +
                         datetime.timedelta(days=-1, minutes=0)).strftime("%Y-%m-%dT%H:00:00.000Z"),
                "to": (datetime.datetime.now() +
                       datetime.timedelta(days=0, minutes=-60)).strftime("%Y-%m-%dT%H:59:59.999Z")
            }
        elif time_type == "past day":
            log_time = {
                "from": (datetime.datetime.now() +
                         datetime.timedelta(days=-2, minutes=0)).strftime("%Y-%m-%dT%H:00:00.000Z"),
                "to": (datetime.datetime.now() +
                       datetime.timedelta(days=-1, minutes=-60)).strftime("%Y-%m-%dT%H:59:59.999Z")
            }
        elif time_type == "past week":
            log_time = {
                "from": (datetime.datetime.now() +
                       datetime.timedelta(days=-8, minutes=0)).strftime("%Y-%m-%dT%H:00:00.000Z"),
                "to": (datetime.datetime.now() +
                       datetime.timedelta(days=0, minutes=-60)).strftime("%Y-%m-%dT%H:59:59.999Z")
            }
        elif time_type == "past 30 days":
            log_time = {
                "from": (datetime.datetime.now() +
                       datetime.timedelta(days=-31, minutes=0)).strftime("%Y-%m-%dT%H:00:00.000Z"),
                "to": (datetime.datetime.now() +
                       datetime.timedelta(days=0, minutes=-60)).strftime("%Y-%m-%dT%H:59:59.999Z")
            }
        elif time_type == "past year":
            year = datetime.datetime.now().year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                log_time = {
                    "from": (datetime.datetime.now() +
                             datetime.timedelta(days=-365, minutes=0)).strftime("%Y-%m-%dT%H:00:00.000Z"),
                    "to": (datetime.datetime.now() +
                           datetime.timedelta(days=0, minutes=-60)).strftime("%Y-%m-%dT%H:59:59.999Z")
                }
            else:
                log_time = {
                    "from": (datetime.datetime.now() +
                             datetime.timedelta(days=-365, minutes=0)).strftime("%Y-%m-%dT%H:00:00.000Z"),
                    "to": (datetime.datetime.now() +
                           datetime.timedelta(days=0, minutes=-60)).strftime("%Y-%m-%dT%H:59:59.999Z")
                }
        else:
            log_time = None

        _message_filter = "筛选活动日志失败"
        response = self.lesson_object.activity_log_list(actor_id=actor_id, event_name=event_name, event_time=log_time)
        glb.rest_o.parse_response(response, glb.CODE200, _message_filter)



if __name__ == "__main__":
    unittest.main()
