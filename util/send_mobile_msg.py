# coding=utf-8

__author__ = 'yxy'

import urllib
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from util.http import BaseHttp


class SmsClient(BaseHttp):
    def __init__(self, env='test'):
        super(SmsClient, self).__init__(env=env)
        self.ssl = False
        self.host = 'cloud.101.com'
        self.header = {
           "Accept": "application/sdp+json",
           "Authorization": "User user_id=59110000",
           "User-Agent": 'yxy'
        }
        self.http_obj = CoHttpM.Http(self.host, self.get_port(), ssl=self.ssl)

    def send_sms(self, mobile, content):
        """

        :return:
        """
        url_params = {
            "mobile": mobile,
            "content": content
        }
        url = '/v1/task/job/createsms'
        url += '?' + urllib.urlencode(url_params, doseq=1)
        print url
        self.http_obj.set_header(self.header)
        body = {}
        params = json_encode(body)

        res = self.http_obj.post(url, params)
        return res

class FalconClient(BaseHttp):
    def __init__(self, env='test'):
        super(FalconClient, self).__init__(env=env)
        self.ssl = False
        self.host = 'alarm.falcon.sdp'
        self.port = '6063'
        self.header = {
           "Accept": "application/json",
           "Content-Type": "application/json",
           "Api-Token": "c119a423a2c05da9703a76ab57fa4570f0fa655951da2",
           "User-Agent": 'yxy'
        }
        self.http_obj = CoHttpM.Http(self.host, self.get_port(), ssl=self.ssl)

    def call_mobile(self, mobile_list, content='生产登录告警，请查看'):
        """

        :return:
        """
        url = '/v1/api/alarms'

        self.http_obj.set_header(self.header)
        body = {
            "type": "phone",
            "content": content,
            "recievers": mobile_list
        }
        params = json_encode(body)

        res = self.http_obj.post(url, params)
        return res

