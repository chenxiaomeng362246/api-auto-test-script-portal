# coding=utf-8
#import config.xq_glb as glb
#__author:chenxiaomeng
#date:2021/10/14

from config.gbl import *
import config.information_glb as glb
import unittest
import api_call.panelmanagement_manage_sites.search_panel_site as api_pm
import json


class test_search_panel_site(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest_o = Restful()
        cls.panel_object = api_pm.SearchPanelSite(ENVIRONMENT)



    @classmethod
    def tearDownClass(cls):
        # 析构方法 退出登录
        pass


    def test_search_panel_site(self):
        """
            [POST]panel manage site
        """
        pageSize = 25
        pageNumber = 0
        sortField = "name"
        searchString = "Smoke"

        err_message = '没有找到对应内容'
        response = self.panel_object.search_panel_site(pageSize, pageNumber, sortField, searchString)
        #parse_response返回的data_dec，data_dec是loads(data)就是转换为dict输出
        data=self.rest_o.parse_response(response, glb.CODE200, err_message)

        #验证找到的内容中是否有搜索的内容
        # response=json.loads(response)
        # print isinstance(data,dict)
        print isinstance(data, dict)
       # sitename = data['searchSites']['sites']['name']


        sitename = data['data']['searchSites']['sites'][0]['name']
        #print isinstance(sitename, list)
        print type(sitename)
        print sitename
        #self.assertRegexpMatches(searchString, sitename)

        # 断言 前面有包含后面的关键字
        self.assertRegexpMatches(sitename, searchString),'当前搜索的关键字是' + searchString + '匹配的额名字是' + sitename
        #self.assertEquals("当前数据搜索与实际想要搜索的数据不同",searchString,sitename)








