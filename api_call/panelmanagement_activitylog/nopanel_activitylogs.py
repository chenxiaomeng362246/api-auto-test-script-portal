# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/14
from util.manage_panel_http import BaseHttp

class NoPanelActivityLogs(BaseHttp):
    def __init__(self, env='env'):
        super(NoPanelActivityLogs, self).__init__(env=env)

    def get_nopanelactivitylogs(self, pageSize):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "noPanelActivityLogs",
            "variables": {
                "searchActivityLog": {
                    "pageSize": pageSize,
                    "offset": 0,
                    "sortDirection": "DESC",
                    "filter": [
                        "prn:Organization::GmsEnable",
                        "20baa791-615d-b1a7-142b-c3e0cf1e8c19"
                    ]
                }
            },
            "query": "query noPanelActivityLogs($searchActivityLog: ISearchNoPanelActivityLog) {\n  noPanelActivityLogs(searchNoPanelActivityLog: $searchActivityLog) {\n    logs {\n      createTime\n      user\n      eventDetail\n      event\n      organization\n      status\n      stage\n      stageUpdateTime\n      __typename\n    }\n    totalCount\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res
