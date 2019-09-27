# coding=utf-8


from __future__ import print_function

__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
import config.gbl as g
from api_call.base.txt_opera import TxtOpera
from api_call.usermanage.client_params import GraphQLClient1


class LessonPlan01(BaseHttp):
    def __init__(self, env='test'):
        super(LessonPlan01, self).__init__(env=env)
        if self.env == 'test':
            self.ssl = False
        else:
            self.ssl = True
        self.token = ''

        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()

        self.gql = GraphQLClient1()
        # self.header = {
        #    "Accept": "application/json",
        #    "Content-Type": "application/json",
        #    "Qa-Tag":"0",
        #     "Authorization": "DEBUG userid=2132756444,realm=oh"
        #
        # }

        if self.env == 'test':
            self.header = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Qa-Tag": "0",
                "Authorization": "DEBUG userid=2133200833,realm=oh",
                "sdp-app-id": "9857bf72-7aa5-4e20-829b-86001e144654"

            }
        elif self.env == 'pre':
            self.header = {
                # "Accept": "application/json",
                "Content-Type": "application/json",
                # "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
                # "Qa-Tag": "0",
                # "Authorization": "DEBUG userid=2133151049,realm=oh"
                # "Authorization": "Bearer " + self.token
            #     "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
            #     "Authorization": "Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjMjZkNGQxZC1hNGI2LTQzMzQtYjVkNS1mNGM1YjgzY2M0YzYiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiJjMjZkNGQxZC1hNGI2LTQzMzQtYjVkNS1mNGM1YjgzY2M0YzYiLCJnaXZlbl9uYW1lIjoiV2FuZyIsImF1ZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZXZlbnRfaWQiOiI5N2YwZTBkMi02MjRiLTQ3NjUtYTNlNi1iNGU0ZTdhNWFiODQiLCJ0b2tlbl91c2UiOiJpZCIsInByb2ZpbGVfaWQiOiI4Y2I5MzM4NC01OWY1LTQ4YTAtOGVjOS0xMzM0NDRhYmI5MmIiLCJhdXRoX3RpbWUiOjE1NjE2MjE5OTAsImV4cCI6MTU2MTYyNTU5MCwiaWF0IjoxNTYxNjIxOTkwLCJmYW1pbHlfbmFtZSI6IlZhbmVzc2EiLCJlbWFpbCI6InZhbmVzc2ExMTAzODZAbmQuY29tLmNuIn0.HWg0o_KO7pKBExQcqUtTbtG3MuDjEVo4tJQahK4EEBi-0aB49YepKwMO_pneqQAA6qtiDAIwIUhEs7M4hm_GQVcglTKkvnl095LIBGqafWwgkUISNFTABkOsclDTed21QKyJY2AvCsggtqCJyGMWVSBZUkNR1qTYxskX2f6I65bM_1n3bHhnuBEPzlNMq9ik7Um7CuEK-Ao0qS06kwDbbW93XAppWK3Je1GZyJXsKOt7krbdxn0zZoIH-Qa6JekE8CT9iImOH-4VAym7OEaCGcrk09Cg77KTM7pB34QpydqiFlYnGbiJp6O549AtLbnXowFNYXVv7czDF_9j-O_NLg"
            #     "x-api-key": "hibkxo48a90bxkeaw22du9w01xnoy64y2itsmgv9",
            #     "Authorization": "Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJnaXZlbl9uYW1lIjoidG9kZCIsImF1ZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZXZlbnRfaWQiOiJmZTNjY2ViNy05OGNjLTQ3NDUtYWM1Yy01OTJhYTYyNjIyYTEiLCJ0b2tlbl91c2UiOiJpZCIsInByb2ZpbGVfaWQiOiI3MDIwMzc0ZS0yNGU5LTRhZWEtODAyNS1lYjkwNTQ1Y2E1NTAiLCJhdXRoX3RpbWUiOjE1NjIwNjQwNjcsImV4cCI6MTU2MjA2NzY2NywiaWF0IjoxNTYyMDY0MDY3LCJmYW1pbHlfbmFtZSI6ImNoZW4iLCJlbWFpbCI6Im5sNTg4MjExMkAxMjYuY29tIn0.SDOLIwcd5ubUUjvKCZfagMzY_iSE5sEvd2ZhfK_PxgDEClbzSlcYyQ6fIQUG7XSDvPjMLBldywTruIPixmYWKUKgWQ1xxmQXKcSD3m8rIbyQdV85AQsGpK_niaI5buNyHzOtZo4AOMwjNvxWPWR0A2aPUGZEtD60j6cPyimkNo73pBr1Bkfq2gwLe_0W5B1vvvl_Zcca0UINc1Z93tZMhTC0HrIq2Oyox61T96j9qMMSs9nv_BfmibIBrFlHWEfImd4kg4JvGdg7awz3vy1FqCL_sUpSs9AvtrGBJKi8k7fjfNfBX09J8WW1yxydxB5641wu4GtQlE37s7IMr5fCOg"
                 "x-api-key": "b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg",
                "Authorization": "Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJnaXZlbl9uYW1lIjoidG9kZCIsImF1ZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZXZlbnRfaWQiOiJmZTNjY2ViNy05OGNjLTQ3NDUtYWM1Yy01OTJhYTYyNjIyYTEiLCJ0b2tlbl91c2UiOiJpZCIsInByb2ZpbGVfaWQiOiI3MDIwMzc0ZS0yNGU5LTRhZWEtODAyNS1lYjkwNTQ1Y2E1NTAiLCJhdXRoX3RpbWUiOjE1NjIwNjQwNjcsImV4cCI6MTU2MjA2NzY2NywiaWF0IjoxNTYyMDY0MDY3LCJmYW1pbHlfbmFtZSI6ImNoZW4iLCJlbWFpbCI6Im5sNTg4MjExMkAxMjYuY29tIn0.SDOLIwcd5ubUUjvKCZfagMzY_iSE5sEvd2ZhfK_PxgDEClbzSlcYyQ6fIQUG7XSDvPjMLBldywTruIPixmYWKUKgWQ1xxmQXKcSD3m8rIbyQdV85AQsGpK_niaI5buNyHzOtZo4AOMwjNvxWPWR0A2aPUGZEtD60j6cPyimkNo73pBr1Bkfq2gwLe_0W5B1vvvl_Zcca0UINc1Z93tZMhTC0HrIq2Oyox61T96j9qMMSs9nv_BfmibIBrFlHWEfImd4kg4JvGdg7awz3vy1FqCL_sUpSs9AvtrGBJKi8k7fjfNfBX09J8WW1yxydxB5641wu4GtQlE37s7IMr5fCOg"
            }

        else:
            self.header = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Qa-Tag": "0",
                "Authorization": "DEBUG userid=2132756444,realm=oh"

            }
        self.http_obj = CoHttpM.Http(self.get_host_usermanage(), self.get_port(), ssl=self.ssl)

    # ============================================公共部分========================================

    def api_post(self):

        url = '/user-management/graphql'
        # variables = {"serialNumber": "65W25KCI18CX135000017P"}
        # query = '''
        #           {
        #             Panel(serialNumber:"65W25KCI18CX135000017P"){
        #               bezelFirmware
        #               ipAddress
        #               macAddress
        #               summary {
        #                 name
        #                 serialNumber
        #                 updateAvailable
        #                 mainboardFirmware
        #                 model
        #               }
        #             }
        #           }
        #           '''

        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = self.gql.execute(query)
        params = self.gql.execute(payload)
        response = self.http_obj.post(url,params)
        print('<p>{}</p>'.format(response))
        return response
