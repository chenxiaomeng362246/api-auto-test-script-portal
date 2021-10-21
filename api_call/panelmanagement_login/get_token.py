# coding=utf-8
from util.get_token_http import *


class Tokenget(BaseHttp):
    def __init__(self):
        super(Tokenget, self).__init__()

# 正向用例：输入正确的用户名和密码，可以正常登录成功且获取到对应的token值
    def get_right_token(self):
        url = '/identity/login'
        method = 'POST'
        body_data = {
            "email": self.user,
            "password": self.password
        }
        res = self.post(url, body_data)
        return res

# 逆向用例：输入空值，无法正常登录获取 也无法正常获取到对应的token值
    def get_wrong_token(self):
        url = '/identity/login'
        method = 'POST'
        body_data = {
            "email": '',
            "password": ''
        }
        res = self.post(url, body_data)
        return res


