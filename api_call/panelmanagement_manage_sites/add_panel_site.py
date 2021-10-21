# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/14
from util.manage_panel_http import BaseHttp


class AddPanelSite(BaseHttp):
    def __init__(self, env='env'):
        super(AddPanelSite, self).__init__(env=env)

    def add_panel_site(self,name,description,notes):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "createSite",
            "variables": {
                "createSiteInput": {
                    "parentOrgPrn": "prn:Organization::PrometheanTest",
                    "name": name,
                    "description": description,
                    "notes": notes
                }
            },
            "query": "mutation createSite($createSiteInput: CreateSiteInput!) {\n  createSite(createSiteInput: $createSiteInput) {\n    id\n    prn\n    name\n    description\n    notes\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res