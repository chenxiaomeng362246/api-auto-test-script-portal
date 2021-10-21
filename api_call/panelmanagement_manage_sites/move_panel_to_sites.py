# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/14
from util.manage_panel_http import BaseHttp


class MovePanelsToSites(BaseHttp):
    def __init__(self, env='env'):
        super(MovePanelsToSites, self).__init__(env=env)

    def move_panels_to_sites(self, site_id, serial_numbers):
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
        res = self.post(url, body)
        return res


