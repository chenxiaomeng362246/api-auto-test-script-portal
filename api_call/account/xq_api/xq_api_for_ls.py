# coding=utf-8


__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
from api_call.base.txt_opera import TxtOpera
import testcases.account.xq_glb as glb
import random


class NotePlan(BaseHttp):
    def __init__(self, env='dev'):
        super(NotePlan, self).__init__(env=env)
        self.ssl = True
        self.token = ''

        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()

        self.cookies = ''
        self.XSRF_TOKEN = ''
        self.cookies_x = ''
        self.cookies_p = ''
        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()
        self.cookies = my_txt.read_txt_cookies()
        self.XSRF_TOKEN = my_txt.read_txt_cookies_x()
        self.cookies_x = my_txt.read_txt_cookies_x()
        self.cookies_p = my_txt.read_txt_cookies_p()
        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json",
                # my pumi
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                # Panel Management
                # "x-api-key": "bv6d45mobai6lk31l9sw6s9argxn42x0x35j7jlt"
                # user Management
                # "x-api-key": "hibkxo48a90bxkeaw22du9w01xnoy64y2itsmgv9"
                "Authorization": self.XSRF_TOKEN,
                # "XSRF-TOKEN" : self.XSRF_TOKEN,
                # "credentials": "include"
                "Cookie": "XSRF-TOKEN=" + self.XSRF_TOKEN + ";prom:sess=" + self.cookies_p
                # "Cookie":self.cookies
                # "Cookie": my_txt.read_txt_cookies()

            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json",
                "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
                "Authorization": self.XSRF_TOKEN,
                # "XSRF-TOKEN" : self.XSRF_TOKEN,
                # "credentials": "include"
                "Cookie": "XSRF-TOKEN=" + self.XSRF_TOKEN + ";prom:sess=" + self.cookies_p
                # "Cookie":self.cookies
                # "Cookie": my_txt.read_txt_cookies()
            }
        else:
            self.header = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Qa-Tag": "0",
                "Authorization": "DEBUG userid=2132756444,realm=oh"

            }
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=self.ssl)
        self.userId = self.get_user_info()
    # ============================================公共部分========================================

    def get_user_info(self):
        """
            user_info  //获取userId
        """
        url = '/profile/graphql'
        self.http_obj.set_header(self.header)
        params = {
            "query": "query getUserProfile { \n        getUserProfile {\n             id\n            email\n            firstName\n            lastName\n            displayName \n            publicName \n            favoriteColor \n            marketingOptIn \n            EULA \n            countryCode\n            languageCode \n            panelPreference { \n                wallpaperUrl\n                favoriteApps \n                json\n            } \n            json\n            avatar {\n                preSignedUrl\n                preSignedUrlTtl\n            }\n        } \n    }"
        }
        params = json.dumps(params)
        res = self.http_obj.post(url, params)
        get_user_profile = json.loads(res.get('data')).get('data')
        user_id = get_user_profile.get('getUserProfile').get('id')
        print('<p>{}</p>'.format(res))
        return user_id

    # 资源搜索与排序
    def post_resourceList(self, offset, limit, language, order):
        """
        1.[POST] /资源搜索与排序[post]
        """

        # url = "/learning-store/ndr/resource/list"
        url = "/learning-store/gls/resources/action/search"
        params = {

            "offset": offset,
            "limit": limit,
            # "language": language,  # "en-US"
            "order": order,  # "Rating desc"
            "types": [],
            "grades": [],
            "subjects": []
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    # 获取用户资源
    def get_user_resource_note(self, user_id, resource_id):

        url = '/learning-store/gls/users/' + user_id + '/resources/' + resource_id + '/note'
        res = self.http_obj.get(url)
        print(res)
        return res

    def get_list_collection_library(self, userId):
        """
          4.9. 获取某个用户下的所有collection列表[GET]
          Get total number of resource in all collections for a user
        """
        url = "/learning-store/gls/users/" + userId + "/collections/resources/number"
        res = self.http_obj.get(url)
        return res





