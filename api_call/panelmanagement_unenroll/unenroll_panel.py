# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/18
from util.manage_panel_http import BaseHttp


class Unenroll_panel(BaseHttp):
    def __init__(self, env='env'):
        super(Unenroll_panel, self).__init__(env=env)

    def unenroll_panel(self, panelsn):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "unenroll",
            "variables": {
                "serialNumbers": [
                    panelsn
                    # "786T-J62L3R9760010-env-dev"
                ]
            },
            "query": "mutation unenroll($serialNumbers: [String!]!) {\n  unenroll(serialNumbers: $serialNumbers) {\n    serialNumber\n    unenrolled\n    error\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res
