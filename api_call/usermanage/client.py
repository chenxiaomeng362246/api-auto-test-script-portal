from six.moves import urllib
import json
__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
import config.gbl as g
from api_call.base.txt_opera import TxtOpera

#
# class LessonPlan(BaseHttp):
#     def __init__(self, env='test'):
#         super(LessonPlan, self).__init__(env=env)
#         if self.env == 'test':
#             self.ssl = False
#         else:
#             self.ssl = True
#         self.token = ''
#
#         # token
#         my_txt = TxtOpera()
#         self.token = my_txt.read_txt()
#         # self.header = {
#         #    "Accept": "application/json",
#         #    "Content-Type": "application/json",
#         #    "Qa-Tag":"0",
#         #     "Authorization": "DEBUG userid=2132756444,realm=oh"
#         #
#         # }
#
#         if self.env == 'test':
#             self.header = {
#                 "Accept": "application/json",
#                 "Content-Type": "application/json",
#                 "Qa-Tag": "0",
#                 "Authorization": "DEBUG userid=2133200833,realm=oh",
#                 "sdp-app-id": "9857bf72-7aa5-4e20-829b-86001e144654"
#
#             }
#         elif self.env == 'pre':
#             self.header = {
#                 # "Accept": "application/json",
#                 "Content-Type": "application/json",
#                 "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
#                 # "Qa-Tag": "0",
#                 # "Authorization": "DEBUG userid=2133151049,realm=oh"
#                 "Authorization": "Bearer " + self.token
#             }
#         else:
#             self.header = {
#                 "Accept": "application/json",
#                 "Content-Type": "application/json",
#                 "Qa-Tag": "0",
#                 "Authorization": "DEBUG userid=2132756444,realm=oh"
#
#             }
#         self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=self.ssl)

class GraphQLClient:

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headername = None
        # self.http_obj = CoHttpM.Http()

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token, headername='Authorization'):
        self.token = token
        self.headername = headername

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   # "x-api-key":"lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",panel management
                   # "x-api-key": "hibkxo48a90bxkeaw22du9w01xnoy64y2itsmgv9",
                   # "Authorization":"Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJnaXZlbl9uYW1lIjoidG9kZCIsImF1ZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZXZlbnRfaWQiOiJmZTNjY2ViNy05OGNjLTQ3NDUtYWM1Yy01OTJhYTYyNjIyYTEiLCJ0b2tlbl91c2UiOiJpZCIsInByb2ZpbGVfaWQiOiI3MDIwMzc0ZS0yNGU5LTRhZWEtODAyNS1lYjkwNTQ1Y2E1NTAiLCJhdXRoX3RpbWUiOjE1NjIwNjQwNjcsImV4cCI6MTU2MjA2NzY2NywiaWF0IjoxNTYyMDY0MDY3LCJmYW1pbHlfbmFtZSI6ImNoZW4iLCJlbWFpbCI6Im5sNTg4MjExMkAxMjYuY29tIn0.SDOLIwcd5ubUUjvKCZfagMzY_iSE5sEvd2ZhfK_PxgDEClbzSlcYyQ6fIQUG7XSDvPjMLBldywTruIPixmYWKUKgWQ1xxmQXKcSD3m8rIbyQdV85AQsGpK_niaI5buNyHzOtZo4AOMwjNvxWPWR0A2aPUGZEtD60j6cPyimkNo73pBr1Bkfq2gwLe_0W5B1vvvl_Zcca0UINc1Z93tZMhTC0HrIq2Oyox61T96j9qMMSs9nv_BfmibIBrFlHWEfImd4kg4JvGdg7awz3vy1FqCL_sUpSs9AvtrGBJKi8k7fjfNfBX09J8WW1yxydxB5641wu4GtQlE37s7IMr5fCOg"
                    'x-api-key': 'b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg',
                    'Authorization': 'Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJjbGllbnRJZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX3pyVGpnZ3d4VyIsImNvZ25pdG86dXNlcm5hbWUiOiIwZTcwYTFkNi1iOGQ5LTQ4M2QtYjJmZS1lZGE2ZmNkMzJkMTEiLCJnaXZlbl9uYW1lIjoidG9kZCIsImF1ZCI6IjZxOWhnb2Q5Mm4ydTBlOThwMDVwMG5vaXA1IiwiZXZlbnRfaWQiOiJmZTNjY2ViNy05OGNjLTQ3NDUtYWM1Yy01OTJhYTYyNjIyYTEiLCJ0b2tlbl91c2UiOiJpZCIsInByb2ZpbGVfaWQiOiI3MDIwMzc0ZS0yNGU5LTRhZWEtODAyNS1lYjkwNTQ1Y2E1NTAiLCJhdXRoX3RpbWUiOjE1NjIwNjQwNjcsImV4cCI6MTU2MjA2NzY2NywiaWF0IjoxNTYyMDY0MDY3LCJmYW1pbHlfbmFtZSI6ImNoZW4iLCJlbWFpbCI6Im5sNTg4MjExMkAxMjYuY29tIn0.SDOLIwcd5ubUUjvKCZfagMzY_iSE5sEvd2ZhfK_PxgDEClbzSlcYyQ6fIQUG7XSDvPjMLBldywTruIPixmYWKUKgWQ1xxmQXKcSD3m8rIbyQdV85AQsGpK_niaI5buNyHzOtZo4AOMwjNvxWPWR0A2aPUGZEtD60j6cPyimkNo73pBr1Bkfq2gwLe_0W5B1vvvl_Zcca0UINc1Z93tZMhTC0HrIq2Oyox61T96j9qMMSs9nv_BfmibIBrFlHWEfImd4kg4JvGdg7awz3vy1FqCL_sUpSs9AvtrGBJKi8k7fjfNfBX09J8WW1yxydxB5641wu4GtQlE37s7IMr5fCOg'
                   }

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        # params = json.dumps(data)

        # self.http_obj.set_header(self.header)
        # req = self.http_obj.post(headers, params)
        # return req
        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)

        response = urllib.request.urlopen(req)
        return response

        # try:
        #     response = urllib.request.urlopen(req)
        #     return response.read().decode('utf-8')
        #
        # except urllib.error.HTTPError as e:
        #     print((e.read()))
        #     print('')
        #     # raise e
        #     return e.read()
