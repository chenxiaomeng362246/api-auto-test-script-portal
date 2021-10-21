# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/14
from util.manage_panel_http import BaseHttp

class RemovePanelSite(BaseHttp):
    def __init__(self, env='env'):
        super(RemovePanelSite, self).__init__(env=env)

    def remove_panel_site(self,prn,siteid):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "removeSite",
            "variables": {
                "prn": prn,
                "siteId": siteid
            },
            "query": "mutation removeSite($prn: String!, $siteId: String!) {\n  removeSite(prn: $prn, siteId: $siteId)\n}\n"
        }

        res = self.post(url, body)
        return res
