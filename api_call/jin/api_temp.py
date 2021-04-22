# coding=utf-8
import json
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp


class Jin(BaseHttp):
    def __init__(self, env='dev'):
        super(Jin, self).__init__(env=env)
        tokenid = "Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0OGUzOThlYy0wNjUyLTRiYjEtOWRmZS02MWU3MjQ5OTA3ZWYiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiI0OGUzOThlYy0wNjUyLTRiYjEtOWRmZS02MWU3MjQ5OTA3ZWYiLCJnaXZlbl9uYW1lIjoibmQxMTMiLCJhdWQiOiI2cTloZ29kOTJuMnUwZTk4cDA1cDBub2lwNSIsImV2ZW50X2lkIjoiYTBiMzFmNGEtMmExMy00NTU5LTk5OTEtNTk3MWY4N2YyM2NmIiwidG9rZW5fdXNlIjoiaWQiLCJwcm9maWxlX2lkIjoiMTA3YmJhNzQtZWY4Mi00ZGY4LWFhY2MtZDUwNTQ4ZWFhMGI5IiwiYXV0aF90aW1lIjoxNjE5MDgxMzI0LCJleHAiOjE2MTkwODQ5MjQsImlhdCI6MTYxOTA4MTMyNSwiZmFtaWx5X25hbWUiOiJjaGVucmoiLCJlbWFpbCI6ImNoZW5yakBuZC5jb20uY24ifQ.eq8aHFBo0sEoW0kU4S7AYhCMraDtzw3MHHzVut6OCrg03FAaW1WnWwu1WN2k_qhTq3j5Ojlt3dzKIfq4xA_Hh_s76DgcwPWXXjZ_1sWA4C-j5E6K5wt4hGHVQtwGvXENNEgvYPRfjnK_xCcskPAPl-ukUzgLHfMqej_NZAzZzsRJIs4r6Cj46rTHuq-Avg3RXLoU7werkWos2cbCXM98H2kN0ArxAnbm6uvkcG14C31S7P5-j9S7SnUYqigBJZ9oPk5wA3KDD1HMM_dNky4RO9onwkAZy1C8CNLNUSk_mLCJzLQTJFKGBxUzCwAlFspS0UUjllUoqTGTsH3DvzDAZQ"
        self.header = {
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": tokenid,
            "x-api-key": "bombp7rgz71fovyquy0yic24cy3tv7v48z6gj1kp"
        }
        # 初始化http，设置header
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)
        self.http_obj.set_header(self.header)

    def jin2_api_get_org_details(self, org_name):
        url = '/org-support/graphql'
        body = {
            "operationName": "getOrgDetails",
            "variables": {
                "prn": org_name
            },
            "query": "query getOrgDetails($prn: String!) {\n  getOrgDetails(prn: $prn) {\n    prn\n    name\n    description\n    address\n    address2\n    city\n    region\n    postalCode\n    country\n    domains {\n      name\n      userCount\n      __typename\n    }\n    admins {\n      firstName\n      lastName\n      email\n      disabled\n      __typename\n    }\n    userCount\n    adminCount\n    status\n    createdOn\n    lastUpdatedOn\n    __typename\n  }\n  countriesList {\n    countryCode\n    name\n    __typename\n  }\n}\n"
        }
        body = json.dumps(body)
        res = self.http_obj.post(url, body)
        return res
