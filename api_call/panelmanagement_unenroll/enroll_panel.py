# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/18
from util.manage_panel_http import BaseHttp


class Enroll_panel(BaseHttp):
    def __init__(self, env='env'):
        super(Enroll_panel, self).__init__(env=env)

    def enroll_panel(self, panelsn,panelname):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "enroll",
            "variables": {
                "input": [
                    {
                        "serialNumber": panelsn,
                        "panelName": panelname
                    }
                ]
            },
            "query": "mutation enroll($input: [IEnrollItemInput]!) {\n  enroll(input: $input) {\n    serialNumber\n    panelName\n    enrolled\n    error\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res
