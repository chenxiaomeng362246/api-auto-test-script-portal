# coding=utf-8


__author__ = 'Administrator'

import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
from api_call.usermanage.client_params import GraphQLClient1


class LessonPlan(BaseHttp):
    def __init__(self,env='dev'):
        super(LessonPlan, self).__init__(env=env)
        if self.env == 'dev':
            self.ssl = True
        else:
            self.ssl = True
        # self.header = {
        #    "Accept": "application/json",
        #    "Content-Type": "application/json;charset=utf-8",
        #    "Qa-Tag":"0",
        # # "Authorization": "DEBUG userid=310522,realm=oh",
        # # "x-api-key":"s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp"
        #
        #     "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw"
        # }
        if self.env == 'dev':
            self.header = {
                # "Accept": "application/json",
                "Content-Type": "application/json",
                # "Qa-Tag": "0",
                #MyPromethean
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw"
                #Panel Management
                # "x-api-key": "bv6d45mobai6lk31l9sw6s9argxn42x0x35j7jlt"
                # user ManagementA
                # "x-api-key": "hibkxo48a90bxkeaw22du9w01xnoy64y2itsmgv9"
            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json",
                # MyPromethean
                "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp"
                # Panel Management
                # "x-api-key": "ffk2es1wc2q36r91uq79o4ow65qfkaqn8xhl5ml3"
                # user Management
                # "x-api-key": "9df3s1p1asihvujg0rigw3v5rdmpg3olrcwlv2wg"
            }
        elif self.env == 'staging':
            self.header = {
                "Content-Type": "application/json",
                # MyPromethean
                "x-api-key": "200vfopedjj7adxw9ei3n94liu880s9o1tvkssg6"
                # Panel Management
                # "x-api-key": "ffk2es1wc2q36r91uq79o4ow65qfkaqn8xhl5ml3"
                # user Management
                # "x-api-key": "9df3s1p1asihvujg0rigw3v5rdmpg3olrcwlv2wg"
            }
        else:
            self.header = {
                "Accept": "application/json",
                "Content-Type": "application/json;charset=utf-8",
                "Qa-Tag": "0",
                # MyPromethean ?
                "x-api-key": "8pnnytjzrw7z1l0g2i8f8luvwmyhkjo7wajaiza0"
                # Panel Management?
                # user Management?
            }

        self.http_obj = CoHttpM.Http(self.get_gis_host(), self.get_port(), ssl=self.ssl)

    # ============================================公共部分========================================

    def post_login_Ls(self, email, password):
        """
      4.1.2 [POST] / usermanagement 登录接口
        """
        url = "/identity/login"
        params = {

            "email": email,
            "password": password
        }
        params = json_encode(params)

        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res



    def post_loginrefresh_ls(self,RefreshToken,IdToken):
        """
             4.1.2
       """

        url = "/identity/login/refresh "
        params = {

            "refreshToken": RefreshToken

        }
        params = json_encode(params)
        # 认证是idtocken
        self.header={"Authorization": "Bearer "+IdToken,
                     "Accept": "application/json",
                     "Content-Type": "application/json;charset=utf-8",
                     "Qa-Tag": "0",
                     # "Authorization": "DEBUG userid=310522,realm=oh",
                     "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp"
                     }
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res