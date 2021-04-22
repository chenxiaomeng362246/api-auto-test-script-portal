# coding=utf-8
import json
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp


class JinToken(BaseHttp):
    def __init__(self, env='dev'):
        super(JinToken, self).__init__(env=env)
        self.header = {
            "Content-Type": "application/json;charset=utf-8",
            "x-api-key": "b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg"
        }
        # 初始化http，设置header
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)
        self.http_obj.set_header(self.header)

    def jin_gettoken(self):
        url = '/identity/login'
        body = {
            "email": "chenrj@nd.com.cn",
            "password": "Jin_111111"
        }
        body = json.dumps(body)
        res = self.http_obj.post(url, body)
        return res
