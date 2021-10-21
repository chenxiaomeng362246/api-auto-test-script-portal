# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/19
from util.manage_panel_http import BaseHttp


class UpdateTag(BaseHttp):
    def __init__(self, env='env'):
        super(UpdateTag, self).__init__(env=env)

    def update_tag(self,id,group,value):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "updateTag",
            "variables": {
                "id": id,
                "group": group,
                "value": value
            },
            "query": "mutation updateTag($id: String!, $group: String!, $value: String!) {\n  updateTag(id: $id, group: $group, value: $value) {\n    id\n    value\n    group\n    __typename\n  }\n}\n"
        }
        res = self.post(url, body)
        return res
