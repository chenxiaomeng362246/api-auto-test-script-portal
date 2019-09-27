# coding=utf-8

import json


class GraphQLClient1:

    def __init__(self):
        pass

    # 处理Graph -->'dict/list'

    def execute(self, query, variables=None):

        data = {'query': query,
                'variables': variables}

        params = json.dumps(data)
        # params = json.dumps(data).encode('utf-8')
        return params