# coding=utf-8
import json
import nd.rest.http_mot as CoHttpM

__author__ = 'Administrator'

# import rsa
from nd.rest.conf.conf import MyCfg


# v0.1-v0.3使用
class BaseHttp(object):
    def __init__(self, env='dev'):
        self.env = env
        # 读取配置
        my_cfg = MyCfg('cfg.ini')
        my_cfg.set_path(__file__)
        my_cfg.set_section(self.env)
        self.port = my_cfg.get('port')
        self.version = '0.1'
        # self.project_id = my_cfg.get('pro_id')
        self.gis_host = my_cfg.get('gis_host')
        self.ybm_host = my_cfg.get('ybm_host')

        # 网页url  //https://devresourcelibrary.prometheanproduct.com
        self.web_url = my_cfg.get('web_url')

    def get_gis_host(self):
        return self.gis_host

    def get_ybm_host(self):
        return self.ybm_host

    def get_port(self):
        return self.port

    def get_url(self, url):
        return "/v" + str(self.version) + "/" + url

    def get_web_url(self):
        return "https://" + self.web_url
