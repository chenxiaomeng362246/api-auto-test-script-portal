# coding=utf-8
import json
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
                "x-api-key": "bv6d45mobai6lk31l9sw6s9argxn42x0x35j7jlt",
                "x-auth-organization-id": "d4b70d67-9287-49de-4973-a143cf00f052"
            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "ffk2es1wc2q36r91uq79o4ow65qfkaqn8xhl5ml3",
                "x-auth-organization-id": "f0bca5c7-1945-1b97-d6ac-806d88e62ebe"
            }
        elif self.env == 'staging':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "0i3gc7uttwvhfvgbfiqhtftbm0v2t2f05b20ulfy",
                "x-auth-organization-id": "d2bcaa83-062d-af1d-e778-c796397f024d"
            }
        elif self.env == 'prod':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": self.tokenId,
                "x-api-key": "9e7dl5dtxel8h5c41c40akxxf47qcr0rbjg06m0n",
                "x-auth-organization-id": "d6bcaa82-23c4-53e7-d96b-563703ce543c"
            }

        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)

    # ============================================公共部分========================================

    def api_manageSite(self, site_id, serial_numbers):
        url = '/mdm-portal/graphql'
        body = {
            "variables": {
                "updatePanelSiteInputs": {
                    "operation": "update",
                    "updateAll": True,
                    "siteId": site_id,
                    "serialNumbers": [serial_numbers]
                }
            },
            "query": "mutation movePanelsToSites($updatePanelSiteInputs: [IUpdatePanelSiteInput]) {movePanelsToSites(updatePanelSiteInputs:$updatePanelSiteInputs) {success}}"
        }
        body = json.dumps(body)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, body)
        return res

