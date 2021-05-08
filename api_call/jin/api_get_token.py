# coding=utf-8
import json
import nd.rest.http_mot as CoHttpM
from api_call.base.http import BaseHttp


class LessonPlan(BaseHttp):
    def __init__(self, env='env'):
        super(LessonPlan, self).__init__(env=env)
        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "x-api-key": "b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg"
            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "x-api-key": "l4mfs8uak1wglsxsyr4ada8h0d0179fwwlrgrzxg"
            }
        elif self.env == 'staging':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "x-api-key": "3ca4wndiwle7aenp6bsqr5w6c6fo8ark8mspgloc"
            }
        elif self.env == 'prod':
            self.header = {
                "Content-Type": "application/json;charset=utf-8",
                "x-api-key": "0rx9owt77ggnq47odona8bvu35k71a7sjpp4m5p9"
            }

        # 初始化http，设置header
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=True)
        self.http_obj.set_header(self.header)

    def jin_gettoken(self):
        url = '/identity/login'
        if self.env == 'prod':
            body = {
                "email": "chenrj@nd.com.cn",
                "password": "Jin_owen930926"
            }
        elif self.env != 'prod':
            body = {
                "email": "chenrj@nd.com.cn",
                "password": "Jin_111111"
            }
        body = json.dumps(body)
        res = self.http_obj.post(url, body)
        return res
