# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/14
from util.manage_panel_http import BaseHttp


class DeleteTag(BaseHttp):
    def __init__(self, env='env'):
        super(DeleteTag, self).__init__(env=env)

    def delete_tag(self, id):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "deleteBatchTags",
            "variables": {
                "id":id
            },
            # "id": id,
            # "query": "mutation deleteBatchTags {\n  deleteTag1: deleteTag(id: \"7f2f7457-5ba4-47e1-8521-b90ef9ff37cb\") {\n    id\n    value\n    group\n    __typename\n  }\n}\n"
            "query": "mutation deleteBatchTags($id: String!) {\n  deleteTag1: deleteTag(id:$id) {\n    id\n    value\n    group\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res
