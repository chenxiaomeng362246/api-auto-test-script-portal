# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/14
from util.manage_panel_http import BaseHttp


class UpdatePanelSite(BaseHttp):
    def __init__(self, env='env'):
        super(UpdatePanelSite, self).__init__(env=env)

    def update_panel_site(self, description, notes):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "updateSite",
            "variables": {
                "updateSiteInput": {
                    "name": "#GMS enabled and something",
                    "description": description,
                    "notes": notes,
                    "prn": "prn:Organization::GmsEnable"
                }
            },
            "query": "mutation updateSite($updateSiteInput: UpdateSiteInput!) {\n  updateSite(updateSiteInput: $updateSiteInput) {\n    id\n    prn\n    name\n    description\n    notes\n    __typename\n  }\n}\n"
        }
        res = self.post(url, body)
        return res

