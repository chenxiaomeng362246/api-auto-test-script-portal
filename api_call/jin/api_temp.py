# coding=utf-8
import json
from config.gbl import *
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp
import testcases.jintest.test_get_token as test_token
from api_call.base.txt_opera import TxtOpera



class LessonPlan(BaseHttp):
    def __init__(self, env='env'):
        super(LessonPlan, self).__init__(env=env)
        self.tokenId = ''
        my_txt = TxtOpera()
        self.tokenId = my_txt.jin_read_txt_authorizationToken()

        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "8k7m8b5d5fe4uainvosm1ph3aaw1kgvgh4toixcx"
            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "uvw9493jpylxyzoww77c6pdhzo445mu82b9h03ja"
            }
        elif self.env == 'staging':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "lvs656pldskhp2b9ryxz00ng4yo8f3rajv4f8kd8"
            }
        elif self.env == 'prod':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "d8e8wkdumnxcrx74htsfowj9bx5xqy5f1995xq62"
            }

        # 初始化http，设置header
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)
        self.http_obj.set_header(self.header)
    # ============================================公共部分========================================


    def api_get_org_details(self, org_name):
        url = '/org-support/graphql'
        body = {
            "operationName": "getOrgDetails",
            "variables": {
                "prn": org_name
            },
            "query": "query getOrgDetails($prn: String!) {\n  getOrgDetails(prn: $prn) {\n    prn\n    name\n    description\n    address\n    address2\n    city\n    region\n    postalCode\n    country\n    domains {\n      name\n      userCount\n      __typename\n    }\n    admins {\n      firstName\n      lastName\n      email\n      disabled\n      __typename\n    }\n    userCount\n    adminCount\n    status\n    createdOn\n    lastUpdatedOn\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        body = json.dumps(body)
        res = self.http_obj.post(url, body)
        return res
