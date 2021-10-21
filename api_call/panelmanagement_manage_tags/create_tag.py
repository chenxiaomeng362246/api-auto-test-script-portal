# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/19
from util.manage_panel_http import BaseHttp


class CreateTag(BaseHttp):
    def __init__(self, env='env'):
        super(CreateTag, self).__init__(env=env)

    def get_taggroup(self):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "getTagGroups",
            "variables": {},
            "query": "query getTagGroups {\n  Tags {\n    group\n    groupId\n    values {\n      value\n      id\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        res = self.post(url, body)
        return res


    def create_tag(self, group, value):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "createTag",
            "variables": {
                "group": group,
                "value": value
            },
            "query": "mutation createTag($group: String!, $value: String!) {\n  createTag(group: $group, value: $value) {\n    id\n    value\n    group\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res
