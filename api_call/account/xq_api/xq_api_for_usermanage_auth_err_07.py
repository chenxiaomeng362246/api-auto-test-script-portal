# coding=utf-8

__author__ = 'Administrator'
# update_time = 2019/10/29

import json
import time
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp
from api_call.base.josn_opera import JsonOpera
import random


class LessonPlan(BaseHttp):
    def __init__(self, env='dev'):
        super(LessonPlan, self).__init__(env=env)
        self.jop = JsonOpera()

        # token
        self.xsrf_token = self.jop.read_josn().get("org_xsrf_token")
        self.tokenId = self.jop.read_josn().get("org_tokenId")

        self.header = {
            "Content-Type": "application/json",
            "Authorization": self.xsrf_token,
            "Cookie": "XSRF-TOKEN=" + self.xsrf_token + ";prom:sess=" + self.tokenId
        }

        # 判断环境 添加x-api-key --> value
        if self.env == 'dev':
            self.header["x-api-key"] = "8k7m8b5d5fe4uainvosm1ph3aaw1kgvgh4toixcx"

        elif self.env == 'sandbox':
            self.header["x-api-key"] = "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp"

        else:
            self.header["x-api-key"] = "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw"

        # 初始化http，设置header
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)
        self.http_obj.set_header(self.header)

    # ============================================公共部分========================================

    # 获取组织列表
    def get_org_list(self):
        url = '/org-support/graphql'
        param = {
            "operationName": "SearchOrgs",
            "variables": {
                "pageNumber": 0,
                "pageSize": random.choice([25, 50, 100]),
                "sortDirection": "ASC",
                "sortField": "name",
                "searchString": ""
            },
            "query": "query SearchOrgs($pageNumber: Int, $pageSize: Int, $sortDirection: SortDirection, $sortField: SortField, $filter: SearchFilter, $searchString: String) {\n  searchOrgs(searchRequest: {pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, filters: $filter, searchString: $searchString}) {\n    orgs {\n      prn\n      name\n      status\n      description\n      address\n      address2\n      country\n      city\n      region\n      postalCode\n      domains {\n        name\n        userCount\n        __typename\n      }\n      admins {\n        firstName\n        lastName\n        email\n        __typename\n      }\n      createdOn\n      lastUpdatedOn\n      userCount\n      __typename\n    }\n    totalPages\n    totalElements\n    isLastPage\n    isFirstPage\n    currentPage\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        # print(json.dumps(res, ensure_ascii=False))
        return res

    # 组织状态列表  //后去优化成可按照Status  Data last Modified Location 进行筛选
    def org_status_list(self):
        url = '/org-support/graphql'
        param = {
            "operationName": "SearchOrgs",
            "variables": {
                "pageNumber": 0,
                "pageSize": 25,
                "sortDirection": "ASC",
                "sortField": "name",
                "filter": {
                    "status": ["active", "incomplete", "archived"]
                },
                "searchString": ""
            },
            "query": "query SearchOrgs($pageNumber: Int, $pageSize: Int, $sortDirection: SortDirection, $sortField: SortField, $filter: SearchFilter, $searchString: String) {\n  searchOrgs(searchRequest: {pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, filters: $filter, searchString: $searchString}) {\n    orgs {\n      prn\n      name\n      status\n      description\n      address\n      address2\n      country\n      city\n      region\n      postalCode\n      domains {\n        name\n        userCount\n        __typename\n      }\n      admins {\n        firstName\n        lastName\n        email\n        __typename\n      }\n      createdOn\n      lastUpdatedOn\n      userCount\n      __typename\n    }\n    totalPages\n    totalElements\n    isLastPage\n    isFirstPage\n    currentPage\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 搜索组织
    def search_orgs(self):

        _searchString = "api test"  # 先固定搜索 //'api test'
        url = '/org-support/graphql'
        param = {
            "operationName": "SearchOrgs",
            "variables": {
                "pageNumber": 0,
                "pageSize": 25,
                "sortDirection": "ASC",
                "sortField": "name",
                "searchString": _searchString
            },
            "query": "query SearchOrgs($pageNumber: Int, $pageSize: Int, $sortDirection: SortDirection, $sortField: SortField, $filter: SearchFilter, $searchString: String) {\n  searchOrgs(searchRequest: {pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, filters: $filter, searchString: $searchString}) {\n    orgs {\n      prn\n      name\n      status\n      description\n      address\n      address2\n      country\n      city\n      region\n      postalCode\n      domains {\n        name\n        userCount\n        __typename\n      }\n      admins {\n        firstName\n        lastName\n        email\n        __typename\n      }\n      createdOn\n      lastUpdatedOn\n      userCount\n      __typename\n    }\n    totalPages\n    totalElements\n    isLastPage\n    isFirstPage\n    currentPage\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 获取组织详情
    def get_org_details(self, org_name):
        url = '/org-support/graphql'
        param = {
            "operationName": "getOrgDetails",
            "variables": {
                "prn": org_name
            },
            "query": "query getOrgDetails($prn: String!) {\n  getOrgDetails(prn: $prn) {\n    prn\n    name\n    description\n    address\n    address2\n    city\n    region\n    postalCode\n    country\n    domains {\n      name\n      userCount\n      __typename\n    }\n    admins {\n      firstName\n      lastName\n      email\n      disabled\n      __typename\n    }\n    userCount\n    adminCount\n    status\n    createdOn\n    lastUpdatedOn\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 新建domain
    def add_domain_info(self, org_name, domain_name):

        # 　domain_name　eg // "api_test.com"
        url = '/org-support/graphql'
        param = {
            "operationName": "manageDomainsForOrg",
            "variables": {
                "prn": org_name,
                "addDomains": [domain_name]
            },
            "query": "mutation manageDomainsForOrg($prn: String!, $addDomains: [String], $removeDomains: [RemoveDomain]) {\n  manageDomainsForOrg(addRemoveDomainsForOrg: {prn: $prn, addDomains: $addDomains, removeDomains: $removeDomains}) {\n    domains {\n      name\n      isAdd\n      success\n      usersAdded\n      usersDisabled\n      error\n      userCount\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 新建domain
    def auto_add_domain_info(self, org_name):

        # 　domain_name　eg // "api_test.com"
        url = '/org-support/graphql'
        param = {
                "operationName": "createOrg",
                "variables": {
                    "createOrgInput": {
                        "country": "",
                        "name": org_name,
                        "city": "",
                        "postalCode": ""
                    }
                },
                "query": "mutation createOrg($createOrgInput: CreateOrgInput!) {\n  createOrg(createOrgInput: $createOrgInput) {\n    ...OrgParts\n    __typename\n  }\n}\n\nfragment OrgParts on Organization {\n  prn\n  name\n  description\n  address\n  address2\n  city\n  region\n  postalCode\n  country\n  timezone\n  domains {\n    name\n    userCount\n    __typename\n  }\n  admins {\n    firstName\n    lastName\n    email\n    disabled\n    __typename\n  }\n  createdOn\n  lastUpdatedOn\n  userCount\n  adminCount\n  status\n  __typename\n}\n"
            }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res
    # 删除domain
    def del_domain_info(self, org_name, domain_name):
        url = '/org-support/graphql'
        param = {
            "operationName": "manageDomainsForOrg",
            "variables": {
                "prn": org_name,
                "removeDomains": [{
                    "name": domain_name,
                    "disableUsersFromRemovedDomains": True
                }]
            },
            "query": "mutation manageDomainsForOrg($prn: String!, $addDomains: [String], $removeDomains: [RemoveDomain]) {\n  manageDomainsForOrg(addRemoveDomainsForOrg: {prn: $prn, addDomains: $addDomains, removeDomains: $removeDomains}) {\n    domains {\n      name\n      isAdd\n      success\n      usersAdded\n      usersDisabled\n      error\n      userCount\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 添加组织管理员
    def add_org_admin(self, org_name, admin):

        url = '/org-support/graphql'
        param = {
            "operationName": "manageAdminsForOrg",
            "variables": {
                "prn": org_name,
                "addAdmins": [admin], # ""
                "removeAdmins": []
            },
            "query": "mutation manageAdminsForOrg($prn: String!, $addAdmins: [String]!, $removeAdmins: [String]!) {\n  manageAdminsForOrg(addRemoveAdminsForOrg: {prn: $prn, addAdmins: $addAdmins, removeAdmins: $removeAdmins}) {\n    userRole {\n      isAdd\n      success\n      user\n      rolePrn\n      error\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 删除组织管理员
    def del_org_admins(self, org_name, admins):
        url = '/org-support/graphql'
        param = {
            "operationName": "manageAdminsForOrg",
            "variables": {
                "prn": org_name,
                "addAdmins": [],
                "removeAdmins": admins
            },
            "query": "mutation manageAdminsForOrg($prn: String!, $addAdmins: [String]!, $removeAdmins: [String]!) {\n  manageAdminsForOrg(addRemoveAdminsForOrg: {prn: $prn, addAdmins: $addAdmins, removeAdmins: $removeAdmins}) {\n    userRole {\n      isAdd\n      success\n      user\n      rolePrn\n      error\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    def activity_log_list(self, page_number=0, page_size=25,
                          search_string="", actor_id=None,
                          event_name=None, event_time=None):
        url = '/org-support/graphql'
        param = {
            "operationName": "SearchAudits",
            "variables": {
                "pageNumber": page_number,
                "pageSize": page_size,
                "sortDirection": "DESC",
                "sortField": "EVENT_TIME",
                "filter": {
                    "eventSource": ["ORG_SUPPORT"]
                },
                "searchString": search_string
            },
            "query": "query SearchAudits($pageNumber: Int, $pageSize: Int, $sortDirection: SortDirection, $sortField: AuditSortField, $filter: AuditSearchFilter, $searchString: String) {\n  searchAudits(auditSearchInput: {pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, filters: $filter, searchString: $searchString}) {\n    audits {\n      actor {\n        id\n        email\n        givenName\n        familyName\n        __typename\n      }\n      eventTime\n      eventName\n      eventSource\n      i18n\n      targets {\n        userId\n        email\n        givenName\n        familyName\n        orgId\n        orgName\n        details\n        __typename\n      }\n      __typename\n    }\n    totalPages\n    totalElements\n    isLastPage\n    isFirstPage\n    currentPage\n    __typename\n  }\n}\n"
        }

        # User筛选
        if actor_id is not None:
            param.get('variables').get('filter')["actorId"] = actor_id  # ["",""]

        # Activity筛选
        if event_name is not None:
            param.get('variables').get('filter')["eventName"] = event_name  # ["",""]

        # Data/Time筛选
        if event_time is not None:
            param.get('variables').get('filter')["eventTime"] = event_time  # {"from":"","to":""}

        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

    # 获取活动日志user和活动信息
    def get_user_and_admin_info(self):
        url = '/org-support/graphql'
        param = {
            "operationName": "GetAuditFilters",
            "variables": {},
            "query": "query GetAuditFilters {\n  getAuditEventNames\n  searchPromAdmins {\n    admins {\n      id\n      email\n      firstName\n      lastName\n      __typename\n    }\n    totalElements\n    __typename\n  }\n}\n"
        }

        param = json.dumps(param)
        res = self.http_obj.post(url, param)
        return res

if __name__ == '__main__':
    Admins = ["accounts-admin@prometheanworld.com", "17689406280@163.com", "tuilly.morita@prometheanworld.com",
              "290930710@qq.com", "rolando.santos@prometheanworld.com", "roberthud+5@gmail.com",
              "vipul.20190412@mailinator.com", "jennifer.sloan@prometheanproduct.com", "matt1@matt.com",
              "todd.giacometti@prometheanworld.com", "mchrist13+demo@gmail.com", "julie.bergen@prometheanworld.com",
              "xiaoyong.zhou@gmail.com", "matthew.christian@prometheanworld.com", "elizurhzxu@163.com",
              "nvzhuanlian@gmail.com", "joehong@nd.com.cn"]
    # print(len(Admins))
    # Admin = random.choice(Admins)
    # print(type(Admin))
    # Admins.remove(Admin)
    # print(Admins)
    #
    # print(random.randint(1, 1))

    # Admins = random.sample(Admins, random.randint(0, len(Admins)))
    print(','.join(Admins))
    global_title = {"pt-BR": "Valores-Ética-Moral-Caráter"}
    print(type(global_title.values()[0]))

    type_description = {1: "Inappropriate content",
                        2: "Copyright infringement",
                        3: "Resource unavailable or unable to access resource",
                        4: "Other (please explain with additional information)"}
    print(type_description[2])
    aa = ["1","2","4"]
    type(','.join(aa))

