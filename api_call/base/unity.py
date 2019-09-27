# coding=utf-8

__author__ = 'Administrator'

import sys
import json
import time
import os
from hamcrest import *
from cof.rand import CoRand
import api_call.account.v01.server as Server
import api_call.account.base.http as BaseM

path = os.path.dirname(__file__)
sys.path.insert(0, path + os.sep + '..')


# v0.1中的身份验证方法
class Unity(BaseM.BaseHttp):
    def getMACContent(self, access_token, url, method, mac_key):
        """
        :name 获取Authorization - os方法

        :param
        #.  id token
        #.  time 2014-12-24T12:23:12Z 时间
        #.  host 访问的域名（这里要加上端口号）
        #.  method  获取方法
        """
        # key参数
        rand_o = CoRand()

        id = access_token

        host = self.get_host() + ":" + str(self.get_port())

        servertime = self.get_server_time()
        servertime = servertime.encode('UTF-8')

        p = os.path.abspath(__file__)
        p = os.path.dirname(p)
        print os.path.exists(p + os.sep + 'token.jar')
        tok_jar = p + os.sep + 'token.jar'

        # 调用jar[命令跟dos下一样]
        url = url.replace('$', '*')
        print url
        command = 'java -jar ' + tok_jar + ' %s %s %s %s "%s" %s>token.txt' % (id, servertime, host, method, url, mac_key)
        print command
        os.system(command)

        # 读文件，取token
        file = open('token.txt', 'r')
        authorization = file.read()
        file.close()

        authorization = authorization.strip()

        return authorization

    def getMACContentForLms(self, access_token, time, url, method, mac_key):
        """
        :name 获取Authorization - os方法

        :param
        #.  id token
        #.  time 2014-12-24T12:23:12Z 时间
        #.  host 访问的域名（这里要加上端口号）
        #.  method  获取方法
        """
        # key参数
        rand_o = CoRand()

        id = access_token

        host = self.get_host()
        servertime = time.encode('UTF-8')

        p = os.path.abspath(__file__)
        p = os.path.dirname(p)
        print os.path.exists(p + os.sep + 'token.jar')
        tok_jar = p + os.sep + 'token.jar'

        # 调用jar[命令跟dos下一样]
        url = url.replace('$', '*')
        print url
        command = 'java -jar ' + tok_jar + ' %s %s %s %s "%s" %s>token.txt' % (id, servertime, host, method, url, mac_key)
        print command
        os.system(command)

        # 读文件，取token
        file = open('token.txt', 'r')
        authorization = file.read()
        file.close()

        authorization = authorization.strip()

        return authorization
    def get_server_time(self):

        server_o = Server.ServerV03()

        response = server_o.get_time()

        #code = response['code']
        data = response['data']

        data_dec = json.loads(data)
        assert_that(data_dec, has_key('server_time'))
        time = data_dec['server_time']

        return time

    def get_server_time_stamp(self):
        """
        把获取到的时间转换成时间戳
        """
        server_time = self.get_server_time()
        print server_time
        #server_time = "2014-12-26T16:53:38.613+0800"

        time_1 = server_time[:-9].replace('T', ' ')
        time_2 = server_time[20:23]

        stamp = time.mktime(time.strptime(time_1,'%Y-%m-%d %H:%M:%S'))
        stamp = str(stamp)[:-2] + time_2

        return str(stamp)

if __name__ == "__main__":
    unity_obj = Unity()

    url = "/v0.3/organizations/1233/orgnodes/213/actions/search?name=asdsd&$offset=0&$limit=10"
    res = unity_obj.getMACContent("a064534c-57a6-4dc2-87db-c0c7576cc81b", url, "POST", "qFkgnEyPlw")

    print res



