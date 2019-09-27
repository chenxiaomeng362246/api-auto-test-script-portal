# coding=utf-8

import os
import json
import time
import types
from hamcrest import *
import datetime
from nd.rest.restful import Restful

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# #################### http状态码 宏定义 ################## #
OK = 200  # 请求成功
CREATED = 201  # 资源创建成功
ACCEPTED = 202  # pOST，DELETE或者PATCH请求提交成功，稍后将异步的进行处理
NO_CONTENT = 204  # Response中包含一些Header和一个状态行， 但不包括实体的主题内容（没有response body）
NOT_MIDIFIED = 304  # 资源最新，使用客户端缓存
BAD_REQUEST = 400  # 无效请求(默认)
REQUIRE_ARGUMENT = 400  # 缺少参数
INVALID_ARGUMENT = 400  # 无效参数(格式不对,长度过长或过短等)
UNAUTHORIZED = 401  # 未授权(默认)
AUTH_TOKEN_EXPIRED = 401  # 授权已过期
AUTH_INVALID_TOKEN = 401  # 无效的授权(如token不存在、需要mac签名、mac签名无效、nonce无效、重复提交等)
AUTH_INVALID_TIMESTAMP = 401  # 无效的时间戳，当时间戳与系统的差异大于5分钟后，产生该错误，客户端需要进行校时操作。
REQUEST_DENIED = 403  # 请求受限(默认)
AUTH_DENIED = 403  # 授权受限（无权限或IP地址受限等）
NOT_FOUND = 404  # 请求的路径不存在(默认)
METHOD_NOT_ALLOWED = 405  # 请求的方法不支持
NOT_ACCEPTABLE = 406  # 服务器无法提供请求时指定的数据响应格式
GONE = 410  # 被请求的资源在服务器上已经不再可用，而且没有任何已知的转发地址
UNSUPPORTED_MEDIA_TYPE = 415  # 服务器不支持请求所提交的数据格式
REQUEST_RATE_LIMITED = 429  # 请求过于频繁
INTERNAL_SERVER_ERROR = 500  # 服务器内部错误(默认)
BAD_GATEWAY = 502  # 无效网关
SERVICE_UNAVAILABLE = 503  # 服务不可用

# #################### 数据 宏定义 ################## #

INVALID_AUTH_TIMESTAMP = '无效的时间戳，当时间戳与系统的差异大于5分钟'
ACCESS_IS_DENIED = 'Access is denied'
DECODE_DENIED = '解密失败'


# #################### 数据类公共方法 ################## #
def assert_keys(data, *key_list):
    """
    数据结构验证
    验证接口返回数据的数据结构是否正确
    """
    for key in key_list:
        assert_that(data, has_key(key))


def copy_dict(ori_dict):
    """
    复制字典，但是过滤为None的字段
    参数：ori_dict 原字典数据
    return：param_dict 过滤了为None的字段、以及self
    """
    param_dict = dict()
    for key in ori_dict:
        if key != 'self' and ori_dict[key] is not None:
            if key in ['offset', 'limit', 'orderby', 'filter', 'order', 'result', 'select']:
                param_dict['$' + key] = ori_dict[key]
            else:
                param_dict[key] = ori_dict[key]

    return param_dict


def new_copy_dict(ori_dict):
    """
    复制字典，但是过滤为None的字段。与旧的区别：所有查询串参数前不加“$”
    参数：ori_dict 原字典数据
    return：param_dict 过滤了为None的字段、以及self
    """
    param_dict = dict()
    for key in ori_dict:
        if key != 'self' and ori_dict[key] is not None:
            param_dict[key] = ori_dict[key]

    return param_dict


def convert_list(ori_dict):
    """
    将param转换成list
    参数：ori_dict 原字典数据
    return：param_list 将dict转换成key-value的list存放
    """
    param_list = []

    for key in ori_dict.keys():
        param = {}
        value = ori_dict[key]
        param['key'] = key
        param['value'] = value
        param_list.append(param)

    return param_list


def get_dict(data):
    """
    复制内容：
    若data为dict，直接复制；
    否则先转换成dict，再复制
    """
    if isinstance(data, types.StringType):
        param_dict = json.loads(data)
    else:
        assert_that(type(data), types.DictType)
        param_dict = data

    return param_dict


class BaseData(object):
    """
    数据的基础类
    """

    def __init__(self):
        """
        将初始化传入的参数赋值给成员变量
        """
        self.params = dict()

    def get(self):
        """
        返回初始的数据
        """
        return self.params

def compare_info(info_1, info_2, skip_keys=['create_time', 'update_time']):
    """
    对比两个数据的信息
    :param info_1:
    :param info_2:
    :param skip_keys: 跳过不对比的key的列表
    :return: 无
    """
    # print "-------------------info_1------------------"
    # print info_1
    # print "-------------------info_2------------------"
    # print info_2

    for key in info_1:
        if key in skip_keys:
            continue
        # print "key: " + str(key)
        message = '与原先的值不一致 key:%s' % key
        assert_that(info_1[key], equal_to(info_2[key]), message)


class PagerResult(object):
    """
    """
    def __init__(self, data):
        assert_keys(data, 'total', 'items')
