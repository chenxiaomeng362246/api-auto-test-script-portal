# coding=utf-8

from data_struct.util import *


class RequestData(BaseData):
    """
    所有request结构均可以调用改方法
    """

    def __init__(self, **kwargs):
        """简化请求参数"""
        BaseData.__init__(self)
        self.params = new_copy_dict(kwargs)


class BodyData(BaseData):
    """
    所有request结构均可以调用改方法
    """

    def __init__(self, **kwargs):
        """简化请求参数"""
        BaseData.__init__(self)
        self.params = new_copy_dict(kwargs)
