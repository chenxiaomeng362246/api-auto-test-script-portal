# coding=utf-8


__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
import config.gbl as g
from api_call.base.txt_opera import TxtOpera


class LessonPlan(BaseHttp):
    def __init__(self, env='dev'):
        super(LessonPlan, self).__init__(env=env)
        if self.env == 'dev' or self.env == 'sandbox':
            # self.ssl = False
            self.ssl = True
        else:
            self.ssl = False
        self.token = ''
        self.token_access = ''

        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()
        self.token_access = my_txt.read_txt_access()

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
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                "Authorization": self.XSRF_TOKEN,
                "Cookie": "XSRF-TOKEN=" + self.XSRF_TOKEN + ";prom:sess=" + self.cookies_p

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
        elif self.env == 'pro':
            self.header = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Qa-Tag": "0",
                "Authorization": "DEBUG userid=2132756444,realm=oh"

            }
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=self.ssl)

    # ============================================公共部分========================================

    def post_list_query(self):
        """
      4.1.2 [POST] /Filters and sort
        """
        url = "/profile/graphql"
        payload = "{\"query\":\"mutation updateUserProfile($userProfileInput: UserProfileInput!) {\\n        updateUserProfile(userProfileInput: $userProfileInput) {\\n            \\nid\\ndisplayName\\npublicName\\nfavoriteColor\\nmarketingOptIn\\nEULA\\ncountryCode\\nlanguageCode\\njson\\navatar {\\n    preSignedUrl\\n    preSignedUrlTtl\\n}\\n        }\\n    }\",\"variables\":{\"userProfileInput\":{\"countryCode\":\"CN\",\"marketingOptIn\":true,\"languageCode\":\"zh-TW\"}}}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        print(res)
        return res

    def post_list_query_01(self):
        """
      4.1.2 [POST] /Filters and sort
        """
        url = "/profile/graphql"
        payload = "{\"query\":\"mutation updateUserProfile($userProfileInput: UserProfileInput!) {\\n        updateUserProfile(userProfileInput: $userProfileInput) {\\n            \\nid\\ndisplayName\\npublicName\\nfavoriteColor\\nmarketingOptIn\\nEULA\\ncountryCode\\nlanguageCode\\njson\\navatar {\\n    preSignedUrl\\n    preSignedUrlTtl\\n}\\n        }\\n    }\",\"variables\":{\"userProfileInput\":{\"countryCode\":\"CN\",\"marketingOptIn\":true,\"languageCode\":\"en\"}}}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_list_query_010(self):
        """
      4.1.2 [POST] /Filters and sort
        """
        url = "/profile/graphql"
        payload = "{\"query\":\"mutation updateUserProfile($userProfileInput: UserProfileInput!) {\\n        updateUserProfile(userProfileInput: $userProfileInput) {\\n            \\nid\\ndisplayName\\npublicName\\nfavoriteColor\\nmarketingOptIn\\nEULA\\ncountryCode\\nlanguageCode\\njson\\navatar {\\n    preSignedUrl\\n    preSignedUrlTtl\\n}\\n        }\\n    }\",\"variables\":{\"userProfileInput\":{\"countryCode\":\"CN\",\"marketingOptIn\":true,\"languageCode\":\"en\"}}}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_edit_password(self, password_pre, password_new):
        """
      4. 密码变更
        """
        url = "/identity/password/change"
        params = {
            "previousPassword": password_pre,
            "proposedPassword": password_new
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_edit_password_01(self, password_pre_01, password_new_01):
        """
      4. 密码变更
        """
        url = "/identity/password/change"
        params = {
            "previousPassword": password_pre_01,
            "proposedPassword": password_new_01
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res
