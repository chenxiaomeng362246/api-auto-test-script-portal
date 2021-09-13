# coding=utf-8
import json
from config.gbl import *
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp
from api_call.base.txt_opera import TxtOpera


class LessonPlan(BaseHttp):
    def __init__(self, env='env'):
        super(LessonPlan, self).__init__(env=env)
        self.tokenId = ''
        my_txt = TxtOpera()
        self.tokenId = my_txt.read_txt_authorizationToken()

        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "8k7m8b5d5fe4uainvosm1ph3aaw1kgvgh4toixcx",
                "x-auth-organization-id": "d4b70d67-9287-49de-4973-a143cf00f052"
            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "uvw9493jpylxyzoww77c6pdhzo445mu82b9h03ja",
                "x-auth-organization-id": "f0bca5c7-1945-1b97-d6ac-806d88e62ebe"
            }
        elif self.env == 'staging':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "lvs656pldskhp2b9ryxz00ng4yo8f3rajv4f8kd8",
                "x-auth-organization-id": "d2bcaa83-062d-af1d-e778-c796397f024d"
            }
        elif self.env == 'prod':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "d8e8wkdumnxcrx74htsfowj9bx5xqy5f1995xq62",
                "x-auth-organization-id": "d6bcaa82-23c4-53e7-d96b-563703ce543c"
            }

        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)

    # ============================================公共部分========================================

    def api_getOrgDetails(self, org_prn):
        url = '/org-support/graphql'
        body = {
            "variables": {
                "prn": org_prn
            },
            "query": "query getOrgDetails($prn: String!) {getOrgDetails(prn: $prn) {id name status}}"
        }
        body = json.dumps(body)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, body)
        return res
