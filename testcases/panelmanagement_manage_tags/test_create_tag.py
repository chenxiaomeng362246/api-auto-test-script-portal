# coding=utf-8
#__author:chenxiaomeng
#date:2021/10/19

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_manage_tags.create_tag as api_pm
from util.txt_opera import TxtOpera
import data_struct.ramdon as randomdata
import string

class test_create_tag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_pm.CreateTag(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass

    #先查看当前的tag group都有什么
    # def test_get_taggroup(self):
    #     response = self.panel_object.get_taggroup()
    #     err_message="获取taggroup失败"
    #     data = self.rest_o.parse_response(response, glb.CODE200, err_message)
    #
    #     grouptaglist = data['data']['Tags'][0]
    #     length =len(grouptaglist)
    #
    #     print length
    #     print grouptaglist
    #     print type(grouptaglist)


    #由于接口文档中并无参数长度校验、必填项校验、无有效性校验、无参数组合校验、故只针对场景进行分类
    #正向用例一：建新的group，新的tag组成可以使用的新tag
    def test_create_tag_case1_ok(self):
        """
            [POST]panel manage tag
        """
        group=randomdata.Random().getramdondata()
        value=randomdata.Random().getramdondata()

        response = self.panel_object.create_tag(group,value)
        # name = ["a", "b", "c"]
        # for n in name:
        err_message = "添加tag失败"
        data = self.rest_o.parse_response(response, glb.CODE200, err_message)

        tagvalue = data['data']['createTag']['value']
        tagid = data['data']['createTag']['id']
        taggroup = data['data']['createTag']['group']
        # 断言 增加的site和返回增加的site的name一致 说明有正确添加成功
        self.assertItemsEqual(value, tagvalue)

        TxtOpera().write_tag_id(tagid)
        TxtOpera().write_tag_group(taggroup)


    #  #正向用例二：从已经存在的group中新建tag
    # def test_create_tag_case1_ok(self):
    #     """
    #         [POST]panel manage tag
    #     """
    #     group = randomdata.Random().getramdondata()
    #     value = randomdata.Random().getramdondata()
    #
    #     response = self.panel_object.create_tag(group, value)
    #     # name = ["a", "b", "c"]
    #     # for n in name:
    #     err_message = "添加tag失败"
    #     data = self.rest_o.parse_response(response, glb.CODE200, err_message)
    #
    #     tagvalue = data['data']['createTag']['value']
    #
    #     # 断言 增加的site和返回增加的site的name一致 说明有正确添加成功
    #     self.assertItemsEqual(value, tagvalue)

    # 逆向用例
    # 传递参数为空
    def test_create_tag_withoutparam(self):
        """
            [POST]panel manage tag
        """
        group=None
        value=None

        response = self.panel_object.create_tag(group,value)
        # name = ["a", "b", "c"]
        # for n in name:
        err_message = "添加tag失败"
        data = self.rest_o.parse_response(response, glb.CODE400, err_message)






