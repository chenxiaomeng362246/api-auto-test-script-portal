# coding=utf-8
import json
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp


class Jin(BaseHttp):
    def __init__(self, env='dev'):
        super(Jin, self).__init__(env=env)
        tokenid = "Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0OGUzOThlYy0wNjUyLTRiYjEtOWRmZS02MWU3MjQ5OTA3ZWYiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiI0OGUzOThlYy0wNjUyLTRiYjEtOWRmZS02MWU3MjQ5OTA3ZWYiLCJnaXZlbl9uYW1lIjoibmQxMTMiLCJhdWQiOiI2cTloZ29kOTJuMnUwZTk4cDA1cDBub2lwNSIsImV2ZW50X2lkIjoiZDljNjNiZGYtOTc3Yi00YTliLWFjMzQtNGUzMmRiZjhjNTIxIiwidG9rZW5fdXNlIjoiaWQiLCJwcm9maWxlX2lkIjoiMTA3YmJhNzQtZWY4Mi00ZGY4LWFhY2MtZDUwNTQ4ZWFhMGI5IiwiYXV0aF90aW1lIjoxNjE5MDkzNjE5LCJleHAiOjE2MTkwOTcyMTksImlhdCI6MTYxOTA5MzYxOSwiZmFtaWx5X25hbWUiOiJjaGVucmoiLCJlbWFpbCI6ImNoZW5yakBuZC5jb20uY24ifQ.QQ5BH6RuxlCx0DDx1JNNiR3dAu0pDMyRiSPHLhKSVxpcfCm1ML1J8E48Qz2ncXQwF-tpI4BYhkz_Gbwp2Luyt9c8ecqunRFrQMfeaYGeHaAOe2Oxa2c4VTWIGgz5yWlbp9WsqZtkcWwfHGHA4a0CdEWdqSbf8klgvog-40L5P-ZG32_0hWdvCOnh_3q5RaQ18LQBwnnZShsiAJd1nD3irLAbV3rNfzi6heMr-jh6lVgQiwGL9tcHy9X95-Ezhix9OyBhnuBK3156qMXcDpdheJ3S_BmnG_prnmoK5oNjEeUXoLvAtZkTj98dsfOAAFi9ylhYtwdUzy7x73FU8glO9g"
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
