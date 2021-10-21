# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/15
from util.manage_panel_http import BaseHttp


class GetPanelSiteDetailById(BaseHttp):
    def __init__(self, env='env'):
        super(GetPanelSiteDetailById, self).__init__(env=env)

    def get_panel_site_details(self, siteid):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "getSiteDetailsById",
            "variables": {
                # "id": "20baa791-615d-b1a7-142b-c3e0cf1e8c19"
                "id":siteid
            },
            "query": "query getSiteDetailsById($id: String!) {\n  getSiteDetailsById(id: $id) {\n    id\n    prn\n    name\n    description\n    panelCount\n    siteManagers {\n      prn\n      firstName\n      lastName\n      email\n      disabled\n      __typename\n    }\n    childOrgPrns\n    siteManagerCount\n    notes\n    __typename\n  }\n}\n"
        }
        res = self.post(url, body)
        return res
