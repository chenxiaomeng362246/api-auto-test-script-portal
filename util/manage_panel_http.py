# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/13
from nd.rest.co_token.uc import *
import json
import nd.rest.http_mot as CoHttpM
from nd.rest.conf.conf import MyCfg
from util.txt_opera import TxtOpera
from config.gbl import ENVIRONMENT


class BaseHttp(object):
    def __init__(self, env = ENVIRONMENT, cfg='panelmanagement_setting.ini', language=None, ssl=True):
        """
        """
        self.env = env
        self.language = language

        # 1.读配置文件，获取host等配置
        my_cfg = MyCfg(cfg)
        my_cfg.set_path(__file__)
        my_cfg.set_section(self.env)
        try:
            self.version = '1'
            self.host = my_cfg.get("host")
            self.web_url = my_cfg.get("web_url")
            self.port = my_cfg.get("port")
            self.user = my_cfg.get("username")
            self.password = my_cfg.get("password")

        except Exception as e:
            print e

        # 2.设置默认的header
        self.header = dict()
        self.header['Content-Type'] = 'application/json;charset=utf-8'
        self.header['Accept'] = 'application/json'
        self.header['x-api-key'] = my_cfg.get("x-api-key")
        self.header['x-auth-organization-id'] = my_cfg.get("x-auth-organization-id")

        self.tokenId = ''
        my_txt = TxtOpera()
        self.tokenId = my_txt.read_txt_authorizationToken()

        self.header['Authorization'] = self.tokenId



        # self.header['Accept-Language'] = 'zh-CN,zh;q=0.8'  # 中文
        # self.header['Accept-Language'] = 'th'                   # 泰文
        # self.header['Accept-Language'] = 'en-us'                # 英文

        # 3.选择token对象、设置环境头信息(common内部登录生成token )
        # if self.env == 'dev':
        #     self.header['x-api-key'] = my_cfg.get("x-api-key")
        # elif self.env == 'sandbox':
        #     self.header['x-api-key'] = my_cfg.get("x-api-key")
        # elif self.env == 'staging':
        #     self.header['x-api-key'] = my_cfg.get("x-api-key")
        # elif self.env == 'pro':
        #     self.header['x-api-key'] = my_cfg.get("x-api-key")



        self.http_o = CoHttpM.Http(self.host, self.port, ssl=ssl)
        self.http_o.set_header(self.header)


    # 4、调用接口测试中使用的http方法提交数据 获取返回值
    def get(self, url):
        url = self.get_url(url)
        res = self.http_o.get(url)
        return res

    def post(self, url, param=''):
        url = self.get_url(url)
        param = json.dumps(param)
        res = self.http_o.post(url, param)
        return res

    def put(self, url, params=''):
        url = self.get_url(url)
        param = json.dumps(params)
        res = self.http_o.put(url, param)
        return res

    def delete(self, url, param=""):
        url = self.get_url(url)
        if param == "":
            res = self.http_o.delete(url)
        else:
            params = json.dumps(param)
            res = self.http_o.delete(url, params)
        return res

    # 5、其他通用get方法
    # def get_url(self, url):
    #     return "/v" + str(self.version) + url
    def get_url(self, url):
        return url

    def get_port(self):
        return self.port

    def get_web_url(self):
        return "https://" + self.web_url

    def set_auth(self, token_type=2, user_name=None, password=None, org='', url='', method=''):
        """
        设置身份信息
        无指定的身份信息时，直接使用默认的身份
        token_type:
            0: header中，不使用Authorization
            1：token 错误
            其他：header中带Authorization
        user_name、password： 切换登录者时传入，不传，默认使用设置的账号
        """
        if user_name is None or user_name == '':
            user_name = self.user

        if password is None or password == '':
            password = self.password

        if token_type == 0:
            self.remove_cookie()
        elif token_type == 1:  # 使用无效的token
            access = "d604c53601aa747f00524d"
            self.header['Authorization'] = access
        elif token_type == 2 or token_type == 3:
            if self.port:
                access_token = self.uc_token_o.get_token(user_name, password, org, self.get_url(url), method,
                                                         self.host + ':' + self.port)
            else:
                access_token = self.uc_token_o.get_token(user_name, password, org, self.get_url(url), method, self.host)
            self.header['Authorization'] = access_token
            self.http_o.set_header(self.header)

    def remove_cookie(self):
        """
        清除header中的Cookie
        """
        if 'Authorization' in self.header.keys():
            self.header.pop('Authorization')
        # if 'Accept' in self.header:
        #     self.header.pop('Accept')
        self.http_o.set_header(self.header)
