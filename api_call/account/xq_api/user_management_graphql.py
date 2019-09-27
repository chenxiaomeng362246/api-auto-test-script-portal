# coding=utf-8


__author__ = 'Administrator'
# import json
# import time
# import nd.rest.http_mot as CoHttpM
# from tornado.escape import json_encode
# from api_call.base.http import BaseHttp
# import config.gbl as g
# from api_call.base.txt_opera import TxtOpera
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
#                 "sdp-app-id":"9857bf72-7aa5-4e20-829b-86001e144654"
#
#             }
#         elif self.env == 'pre':
#             self.header = {
#                 # "Accept": "application/json",
#                 "Content-Type": "application/json",
#                 "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
#                 # "Qa-Tag": "0",
#                 # "Authorization": "DEBUG userid=2133151049,realm=oh"
#                 "Authorization":"Bearer "+self.token
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
#

    # ============================================公共部分========================================
import httplib,json,graphene
graphene.String

# class Query(graphene.ObjectType):
#     def __init__(self,value):
#         super(graphene.ObjectType,self).__init__()
#         self.a= graphene.String(name=graphene.String(default_value=value))
#
#     def kk(self,name):
#         return name
#
# s=graphene.Schema(query=Query)
# r = s.execute('{query}')
# print r.get('query')


def post_list_query():
    # s=graphene.Schema(query=Query)
    # r = s.execute('query')
    """
  4.1.2 [POST] /Filters and sort
    """

    # url = "/learning-store/gls/collections"
    host = 'devapi.prometheanproduct.com'
    port = 443
    url = "/user-management/graphql"
    header = {
                # "Accept": "application/json",
                "Content-Type": "application/json",
                "x-api-key": "b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg",
                # "Qa-Tag": "0",
                # "Authorization": "DEBUG userid=2133151049,realm=oh"
                "Authorization":"Bearer eyJraWQiOiJQeUw0cTdoRlhZYXZrZkhwVE1DZW9aRUZIaU55WENKcWwzZElTUU41TWRBPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiVXNqTS0yUVBxUXYxNlhjM2RRN2ZyQSIsInN1YiI6ImIxNTQ5NWY1LTIxYWItNDUzMS05NWQ5LTkxZTU5OWMyMTU1NSIsImNsaWVudElkIjoiNnE5aGdvZDkybjJ1MGU5OHAwNXAwbm9pcDUiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfenJUamdnd3hXX09mZmljZTM2NSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV96clRqZ2d3eFciLCJjb2duaXRvOnVzZXJuYW1lIjoiT2ZmaWNlMzY1X3hzUS0xZmoyNGY0eG9pTGhCZHYtclNiRDJqcnAxSFVndVA3N0R5QVhGSkkiLCJnaXZlbl9uYW1lIjoieGlhb2xpYW4iLCJhdWQiOiI2cTloZ29kOTJuMnUwZTk4cDA1cDBub2lwNSIsImlkZW50aXRpZXMiOlt7InVzZXJJZCI6InhzUS0xZmoyNGY0eG9pTGhCZHYtclNiRDJqcnAxSFVndVA3N0R5QVhGSkkiLCJwcm92aWRlck5hbWUiOiJPZmZpY2UzNjUiLCJwcm92aWRlclR5cGUiOiJPSURDIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTU2MTM1OTQ5MzI3OSJ9XSwidG9rZW5fdXNlIjoiaWQiLCJwcm9maWxlX2lkIjoiODVmN2YxYjUtOWU4NS00NDdiLTg5MjQtMjJjMmJlZDQ0YjMxIiwiYXV0aF90aW1lIjoxNTYxMzU5NTAwLCJleHAiOjE1NjEzNjM0NjUsImlhdCI6MTU2MTM1OTg2NSwiZmFtaWx5X25hbWUiOiJsaWFuIiwiZW1haWwiOiJxYXRlc3RAbmRsbnoub25taWNyb3NvZnQuY29tIn0.HggLA6XrWWfm9I_du6kOnKQo23xJksy-R6Z5ZdRRlwRJncUAtUjQLVF6r2G0K77wyswh-JmslpCLp_X8MAkIseT9KwDDRmFRNJyuArBtIQnjlVgyDuTrbmWT7gCYBKFxyYZJNNpqLenpwjFyAYXZjkSjPsHNBoiC1TCczGlJ2Adk_1VbxvNFAFMsUPeVGwNeDxblxri41RTfD0BZfGZdENiybyn1KQZhmufAL10pwlvV_ITPvoaLxjQrX9dRirM8Viu2PGMIL64XOCdJVg7pwBdJ9D45o_FN6pKq0f-KkpUrG4GMzcYEyXj4BREyK9TNuLP4q3ULLKbC3P2ki--caA"}
    params ={"operationName":None,"variables":{},"query":"{"
                                                         "listAccountStatuses {\n    accountStatuses {\n      prn\n      name\n    }\n  }\n}\n"}
    # params = json_encode(params)
    params = json.dumps(params)

    res = httplib.HTTPSConnection(host,port)
    res.request(method='post',url=url,body=params,headers=header)
    response = res.getresponse()
    return response.read()

if __name__ == '__main__':
   print post_list_query()
