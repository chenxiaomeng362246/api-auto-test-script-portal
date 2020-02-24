# coding=utf-8
import random
import sys
import api_call.account.xq_api.xq_api_for_ybm as ybm_api
import testcases.account.xq_glb as glb
# import testcases.account.fep_glb as glb
import nd.rest.http_mot as CoHttpM
import json
from config.gbl import *
import uuid
from unittest import SkipTest
import unittest
import ddt
from data_struct.request_data import RequestData

__author__ = 'Administrator'
sys.path.insert(0, '..')
reload(sys)
sys.setdefaultencoding('utf-8')


def item(response):
    #  data ->type dict
    data = json.loads(response['data'])
    return data

@ddt.ddt
class UserTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     assert_that(ENVIRONMENT in [TEST, PRE], equal_to(True), '暂不支持该环境')

    # def setUp(self):
    #     self.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)
    #
    # def tearDown(self):
    #     # 析构方法 退出登录
    #     '''
    #     '''
    @classmethod
    def setUpClass(cls):
        cls.lesson_object = ybm_api.LessonPlan(ENVIRONMENT)

    @classmethod
    def tearDownClass(cls):
        pass

    # 获取资源总页数
    def get_offset_count(self):
        offset = 0
        limit = 12
        language = []
        order = "Rating desc"
        response = self.lesson_object.post_resourceList(offset, limit, language, order)
        data = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        count = data.get('count')

        # 处理资源总页数
        if count % 12 == 0 and count !=0:
            page = count // 12
        elif count == 0:
            page = 1
        else:
            page = count // 12 + 1
        return page

    def test_new_collection(self):
        '''
       4.1 [POST] /新增collection已经更新第二版本
        level:1,2,4,5
        '''

        response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.new_collection)  #
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_new_collection_more(self):
        '''
       4.1 [POST] /新增collection已经更新第二版本
        level:1,2,4,5
        '''
        cnt_collection = 1
        # new_collection_test = str(uuid.uuid4())
        while cnt_collection < 10:
            new_collection_test = str(uuid.uuid4())
            response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, new_collection_test)  #
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            # data_body = item(response)
            # if response.get("code") == 400:
            #    print ("<p>%s</p>".format(data_body["code"]))
            # elif response.get("code") == 200:
            #     pass
            time.sleep(1.0)
            cnt_collection = cnt_collection + 1
        time.sleep(1.0)

    # def test_new_collection_reverse(self):
    #     '''
    #    4.1.1 [POST] /新增collection已经更新第二版本 反向案例 表情符号 -->属于正向用例,暂时注释
    #     level:1,2,4,5
    #     '''
    #     response = self.lesson_object.post_login_AddCollection(glb.userId, glb.NEW_COLLECTION_03)
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_new_collection_special_character(self):
        '''
       4.1.2 [POST] /新增collection已经更新第二版本 反向案例 用户id 超过100个字符的时候
        level:1,2,4,5
        '''
        response = self.lesson_object.post_login_AddCollection(glb.userId_02, glb.NEW_COLLECTION_03)
        time.sleep(3)
        data_dec = glb.rest_o.parse_response(response, glb.CODE403, glb.message)

    def test_new_collection_existing_name(self):
        '''
       4.1.3 [POST] /新增collection已经更新第二版本 反向案例  收藏夹数据库已存在的名称
        level:1,2,4,5
        '''
        response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.new_collection_02)
        data_dec = glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_update_collection(self):
        '''
       4.2 [PUT] / 4.2. 更新collection[PUT]
        level:1,2,4,5
        '''
        response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.collection)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        id = data_dec["id"]
        response = self.lesson_object.put_login_UpdateCollection(id, self.lesson_object.userId, glb.update_collection)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_update_collection_reserve(self):
        '''
       4.2.0[PUT] / 4.2. 更新collection[PUT] 反向案例 一个用户同时更新同一个收藏夹。
        level:1,2,4,5
        '''
        response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.collection)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        id = data_dec["id"]
        response = self.lesson_object.put_login_UpdateCollection(id, self.lesson_object.userId, glb.update_collection)
        data_dec = glb.rest_o.parse_response(response, glb.CODE400, glb.message)

    def test_delete_collection(self):
        """
            4.3[DELETE] 4.3. 删除collection[DELETE]
            level:1,2,4,5
        """

        # 获取所有收藏夹id
        collection_ids = list()
        offset = 0
        while True:
            response = self.lesson_object.get_collectionGroup(self.lesson_object.userId, offset)
            data = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            for item in data.get('items'):
                collection_ids.append(item.get('collectionId'))
            if len(data.get('items')) < 12:
                break
            else:
                offset = offset + 12
                time.sleep(1.0)  # 强制等待1秒

        # 处理收藏夹
        count = len(collection_ids) # 收藏夹个数
        if count == 0:
            # 新增一个，再删除
            response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.collection)
            data = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            collection_id = data["id"]

            response = self.lesson_object.delete_mylibrary_id(collection_id)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        elif count > 5:

            # 保留5条，其它收藏夹随机删除
            for i in xrange(5, count):
                collection_id = random.choice(collection_ids)
                response = self.lesson_object.delete_mylibrary_id(collection_id)
                glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                time.sleep(1.5)  # 强制等待1.5秒
                collection_ids.remove(collection_id)  # 剔除已删除收藏夹
        else:
            # 1-5条，随机删除1条
            collection_id = random.choice(collection_ids)
            response = self.lesson_object.delete_mylibrary_id(collection_id)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)


    def test_delete_collection_reserve(self):
        '''
       4.3.0[DELETE] 4.3. 删除collection[DELETE] 如果有缓存，重复删除同一个收藏夹
        level:1,2,4,5
        '''
        response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.collection)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        id = data_dec["id"]
        # response = self.lesson_object.delete_mylibrary_id(id)
        response = self.lesson_object.delete_mylibrary_id(id)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_keyword(self):
        '''
       4.4.00 [POST]search 资源 关键字keyword 为特殊字符比如“#” 、”&”、” ?”、”=”、”/”
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit, glb.language, glb.order, glb.keyword)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_kw_tab(self):
        '''
       4.4.01[POST]search 资源 关键字keyword 为字符串中间有空格
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit, glb.language, glb.order, glb.keyword_1)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_kw_html(self):
        '''
       4.4.02[POST]search 资源 关键字keyword 为html格式<p>
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit, glb.language, glb.order, glb.keyword_2)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_kw_English(self):
        '''
       4.4.021[POST]search 资源 关键字keyword 为英文字母
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit, glb.language, glb.order, glb.keyword_4)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_kw_sensitive(self):
        '''
       4.4.03[POST]search 资源 关键字keyword 为敏感词台独
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit, glb.language, glb.order, glb.keyword_3)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_kw_parameter(self):
        '''
       4.4.04[POST]search 资源 parameter输错  Learning StoreLS-399  For integer property(limit, offset),fastjson converts null to 0.The problem is almost no risk.
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit_4, glb.language, glb.order,
                                                          glb.keyword_3)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_kw_parameter_0(self):
        '''
       4.4.040[POST]search 资源 parameter输错  Learning StoreLS-399  For integer property(limit, offset),fastjson converts null to 0.The problem is almost no risk.
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset_4, glb.limit_4, glb.language, glb.order,
                                                          glb.keyword_3)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_order_1(self):
        '''
       4.4.05[POST]search 资源排序Type desc
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit_4, glb.language, glb.order_1,
                                                          glb.keyword_3)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_order_2(self):
        '''
       4.4.06[POST]search 资源 排序Grade Level desc
        '''
        response = self.lesson_object.post_resourceList_1(glb.offset, glb.limit_4, glb.language, glb.order_2,
                                                          glb.keyword_3)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection(self):
        '''
       4.4.0 [POST]search 资源
        '''
        # 首先获取资源id
        response = self.lesson_object.post_collection(glb.offset, glb.limit, self.lesson_object.userId, glb.sort)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_search_collection_rating(self):
        '''
       4.4.00 [POST]search 资源 平均分 排序
        '''
        # 首先获取资源id
        response = self.lesson_object.post_resourceList_rating(glb.offset, glb.limit, glb.language, glb.order,
                                                               glb.rating)
        print("<p>%s</p> " % response)
        # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # rating=json.loads(response['data'])
        rating = item(response)
        # 不是列表不能用for  键值对用
        for s in rating["items"]:
            if s.get("custom_properties").get("avg_rating") >= 1 and glb.rating == 1:
                pass
            elif s.get("custom_properties").get("avg_rating") >= 2 and glb.rating == 2:
                pass
            elif s.get("custom_properties").get("avg_rating") >= 3 and glb.rating == 3:
                pass
            elif s.get("custom_properties").get("avg_rating") >= 4 and glb.rating == 4:
                pass
            elif s.get("custom_properties").get("avg_rating") >= 5 and glb.rating == 5:
                pass
            else:
                raise TypeError('avg_rating错误值{}'.format(s.get("custom_properties").get("avg_rating")))
        #         报错  自己定义的错误
        #         失败 ：程序报错
        print "<p>test</p>"
        print ("<p>{}</p>".format(rating))
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    # def test_resource_search_collection_rating_01(self):
    #     '''
    #    4.4.00 [POST]search 资源 平均分 排序
    #     '''
    #     # 首先获取资源id
    #     response = self.lesson_object.post_resourceList_rating(glb.offset,glb.limit,glb.language, glb.order,glb.rating)
    #     # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
    #     rating=response["items"]
    #     for s in rating:
    #         if s.get("custom_properties").get("avg_rating")>3:
    #             pass
    #         else:
    #             raise TypeError('avg_rating错误值{}'.format(s.get("custom_properties").get("avg_rating")))
    #     #         报错  自己定义的错误
    #     #         失败 ：程序报错
    #     print "<p>test</p>"
    #     print ("<p>{}</p>".format(rating))
    #     data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_add_collection(self):
        '''
       4.4.1.0 [POST]将资源添加到collection[POST] 一个资源对应多个收藏夹
        '''
        print "<p>4.4.1 首先获取资源id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 判断资源列表
        try:
            resource_id = data_dec["items"][1]["id"]
        except IndexError as e:
            print('<p>资源的列表获取资源少于2个 reslut:{}</p>\n{}'.format(data_dec, e))
        else:
            print "<p>4.4.2 再次获取收藏夹id</p>"
            response = self.lesson_object.get_collectionid_count(self.lesson_object.userId)
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

            collection_ids = []
            for value in data_dec.get('items'):
                glb.cnt += 1
                if glb.cnt < 51:
                    res = value.get('id')
                    collection_ids.append(res)
                else:
                    break
            response = self.lesson_object.post_resourceAdd(self.lesson_object.userId, collection_ids, resource_id)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_add_collection_more(self):
        '''
       4.4.2.0 [POST]将资源添加到collection[POST] 随机一个资源对应多个收藏夹
        '''
        print "<p>首先获取资源id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 判断资源列表
        items = data_dec["items"]
        if items < 1:
            chosen = 0
        else:
            chosen = random.randint(0, len(items) - 1)

        try:
            resource_id = items[chosen]["id"]
        except IndexError as e:
            print('<p>资源的列表获取资源为空 reslut:{}</p>\n{}'.format(items, e))

        else:
            print "<p>再次获取收藏夹id</p>"
            response = self.lesson_object.get_collectionid_count(self.lesson_object.userId)
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            collection_ids = []
            for value in data_dec.get('items'):
                glb.cnt1 += 1
                if glb.cnt1 < 50:
                    res = value.get('id')
                    collection_ids.append(res)
                else:
                    break
            response = self.lesson_object.post_resourceAdd(self.lesson_object.userId, collection_ids, resource_id)
            print "<p>400意思是Resources have been collected</p>"
            if response.get("code") == 400:
                glb.rest_o.parse_response(response, glb.CODE400, glb.message)
            else:
                glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_add_collection_random(self):
        '''
       4.4.3.0 [POST]将资源添加到collection[POST] 随机页数其中一个资源对应多个收藏夹
        '''
        print "<p>4.4.1 首先获取资源id</p>"
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_resource_add_collection_random()
            else:
                chosen = random.randint(0, len(items) - 1)
                resourceid = items[chosen]["id"]

                print "<p>4.4.2 再次获取收藏夹id</p>"
                response = self.lesson_object.get_collectionid_count(self.lesson_object.userId)
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                collectionIDS = []
                for value in data_dec.get('items'):
                    glb.cnt2 += 1
                    if glb.cnt2 < 50:
                        res = value.get('id')
                        collectionIDS.append(res)
                    else:
                        break
                # collectionIds =[data_dec["items"][0]["id"]]
                # for i in range(len(data_dec))
                #     for value in data_dec.get('items'):
                #       res = value.get('id')
                #       collectionIds.append(res)
                # collectionarr=collectionid.split(',')
                #
                # collectionIds= [data_dec["items"][0]["id"]]
                response = self.lesson_object.post_resourceAdd(self.lesson_object.userId, collectionIDS, resourceid)
                # 资源是否被收藏的情况
                message = "Resources have been collected"
                data = item(response)
                if response.get('code') == 400 and data.get('message') == message:  # 简单判断被收藏,未进行判断每个资源真的被收藏过
                    glb.rest_o.parse_response(response, glb.CODE400, glb.message)
                    print('<p>{}</p>'.format('存在资源已被收集'))

                glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_resource_add_collection_reverse(self):
        '''
       4.4.4.0 [POST]将资源添加到collection[POST] 随机页数其中一个资源对应多个收藏夹
        '''
        print "<p>4.4.1 首先获取资源id</p>"
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_resource_add_collection_reverse()
            else:
                chosen = random.randint(0, len(items) - 1)
                resourceid = items[chosen]["id"]

                print "<p>4.4.2 再次获取收藏夹id</p>"
                response = self.lesson_object.get_collectionid_count(self.lesson_object.userId)
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                collectionIDS = []
                for value in data_dec.get('items'):
                    print '<p>{}</p>'.format(value)
                    glb.cnt3 = glb.cnt3 + 1
                    if glb.cnt3 < 51:
                        res = value.get('id')
                        collectionIDS.append(res)
                print '<p>{}</p>'.format(collectionIDS)
                response = self.lesson_object.post_resourceAdd(self.lesson_object.userId, collectionIDS, resourceid)
                if response.get("code") == 400:
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_resource_delete_collection(self):
        '''
        4.5. [DELETE]  将资源移除collection [DELETE]
        '''

        print "<p> 1.通过查询整个资源的列表获取资源id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit_search, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        print "<p> 2.取整个列表资源id其中一个</p>"
        # 取整个列表资源id其中一个
        try:
            resource_id = data_dec["items"][1]["id"]
        except IndexError as e:
            print('<p>资源的列表获取资源少于2个 reslut:{} {}</p>'.format(data_dec, e))

        else:
            print "<p> 3.通过查询整个collection的列表获取资源id</p>"
            # 4.5.1通过查询整个collection的列表获取资源id
            response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.new_collection_01)
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            collection_id = data_dec["id"]
            collectionarr = collection_id.split(',')
            response = self.lesson_object.post_resourceAdd(self.lesson_object.userId, collectionarr, resource_id)
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

            response = self.lesson_object.del_resource_delete_collection(collection_id, resource_id)
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            # id = data_dec["id"]

    def test_resource_delete_collection_reverse(self):
        '''
        4.5.0 [DELETE]  将资源移除collection [DELETE] 反向案例为了不影响其他案例自己新建一个收藏夹，先把资源添加到收藏夹，再从收藏夹删除。
        '''
        # 4.5.1通过查询整个资源的列表获取资源id
        print "<p>第一步骤通过查询整个资源的列表获取资源id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit_search, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        print "<p>第二步骤取整个列表资源id其中一个</p>"
        # 取整个列表资源id其中一个
        # 判断资源列表
        try:
            resource_id = data_dec["items"][1]["id"]
        except IndexError as e:
            print('<p>资源的列表获取资源少于2个 reslut:{}</p>\n{}'.format(data_dec, e))

        else:
            print "<p>第三步骤通过查询整个collection的列表获取资源id</p>"
            response = self.lesson_object.post_login_AddCollection(self.lesson_object.userId, glb.new_collection_01)
            print ("<p>{}</p>".format(response.get("code")))
            if response.get("code") == 400:
                pass
            else:
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                collectionid = data_dec["id"]
                collectionarr = collectionid.split(',')
                response = self.lesson_object.post_resourceAdd(self.lesson_object.userId, collectionarr, resource_id)
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

                response = self.lesson_object.del_resource_delete_collection(collectionid, resource_id)
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                # id = data_dec["id"]

    def test_resource_group_collection(self):
        '''
        4.6. [GET] collection分组[GET]
        '''
        response = self.lesson_object.get_collectionGroup(self.lesson_object.userId)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # id = data_dec["id"]

    def test_resource_thumbnail_collection(self):
        '''
       4.7. [POST] 获取collection的缩略图信息
        '''
        response = self.lesson_object.get_collectionGroup(self.lesson_object.userId)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        collectionIds = []
        for value in data_dec.get('items'):
            res = value.get('collectionId')
            collectionIds.append(res)
        # collectionarr = collectionId.split(',')
        response = self.lesson_object.post_thumbnailAdd(collectionIds)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # id = data_dec["id"]

    def test_resource_list_collection(self):
        '''
       4.8.[POST] 获取collection中的资源列表
        '''
        response = self.lesson_object.post_collection(glb.offset, glb.limit, self.lesson_object.userId, glb.sort)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # id = data_dec["id"]

    def test_resource_list_collection_user_id(self):
        '''
       4.9. 获取某个用户下的所有collection列表[GET]
        '''
        response = self.lesson_object.get_list_collection_library(self.lesson_object.userId)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # id = data_dec["id"]

    def test_resource_count_my_library(self):
        '''
       4.10. 统计某个用户my library中资源个数 GET
        '''
        response = self.lesson_object.get_resourceid_count(self.lesson_object.userId)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # id = data_dec["id"]

    def test_resourceCollections_count_my_library(self):
        '''
       4.11. 统计某个用户my library中collection个数 GET
        '''
        response = self.lesson_object.get_collectionid_count(self.lesson_object.userId)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # id = data_dec["id"]

    def test_resource_exist_collection(self):
        '''
       4.12_0. 判断某个资源是否已被收藏到collection中 POST
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_resource_exist_collection()
            else:
                resourceIds = []
                for value in data_dec.get('items'):
                    res = value.get('id')
                    resourceIds.append(res)
                response = self.lesson_object.post_whether_resource_collected(self.lesson_object.userId, resourceIds)
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                # id = data_dec["id"]
        except ValueError:
            print('<p>资源列表无资源</p>')

    # @unittest.skip("前端还没有开发，直接访问url访问不了，因为有类似api网关的问题")
    @ddt.data(*[{"comment": glb.comment, "type": glb.type},
                {"comment": glb.comment_v2, "type": glb.type_v4},
                {"comment": glb.comment_v2, "type": glb.type_v33}])
    def test_flagAsInappropriate_search_null(self, value):
        """
              4.12. 针对一个资源进行审核
              2019/10/28  资源审核 //v0.2.4
        """

        page = self.get_offset_count()
        # 处理分页过多时，请求分页固定分页值30  //offset 超过10000就会报500  es
        if page >= 30:
            offset_ran = random.randint(0, 30) * 12  # 随机页数 //12 * (0/1/2...)
        else:
            offset_ran = random.randint(0, page) * 12

        print "<p>第一步，获取列表资源的id</p>"
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 获取资源id和资源name
        items = data_dec["items"]
        chosen = random.randint(0, len(items) - 1)
        resource_id = items[chosen]["id"]
        resource_title = items[chosen]['global_title'].values()[0]

        print "<p>第二步，对获取到列表资源的id，进行资源标注暴力，非法，广告，安全泄密</p>"
        response = self.lesson_object.post_resourceList_flag(
            self.lesson_object.userId,
            resource_id,
            resource_title,
            value["comment"],
            value["type"]
        )
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        # data = item(response)

        # v0.2.4 //被标注报500？ 注释这段，等接口修改好，需要重启用修改此逻辑
        # message = 'Fail to get resource link'
        # if response.get('code') == 500 and data.get('message') == message:  # 此资源被标注
        #     glb.rest_o.parse_response(response, glb.CODE500, glb.message)
        # else:
        #     glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        print "<p>第三步，资源已标注，判断资源是否被确认删除</p>"

        # 按照name搜索资源
        response = self.lesson_object.post_resourceList(0, 12, glb.language, glb.order, keyword=resource_title)
        data = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        count = data.get('count')
        if count == 0:
            # 已被删除
            response = self.lesson_object.get_resourceList_information(resource_id, self.lesson_object.userId)
            glb.rest_o.parse_response(response, glb.CODE404, glb.message)
        else:
            # 未被删除
            response = self.lesson_object.get_resourceList_information(resource_id, self.lesson_object.userId)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    # @unittest.skip("前端还没有开发，直接访问url访问不了，因为有类似api网关的问题")
    def test_getLinkOfResource_for_download(self):
        '''
        4.13 资源链接下载
        '''
        print "<p>第一步，获取列表资源的id</p>"
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_getLinkOfResource_for_download()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.get_resource_link(resource_id)
                glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    # @unittest.skip("前端还没有开发，直接访问url访问不了，因为有类似api网关的问题")
    def test_post_resource_reviews(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.post_resource_reviews(resource_id, self.lesson_object.userId,
                                                                    glb.userName)
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    # @unittest.skip("前端还没有开发，直接访问url访问不了，因为有类似api网关的问题")
    def test_post_resource_reviews_01(self):
        '''
        4.15 获得某个用户的评分以及评论 可选请求体案例
        '''
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        # 列表有十个资源取下标是从0开始
        resourceid = data_dec["items"][chosen]["id"]
        response = self.lesson_object.post_resource_reviews_01(resourceid, self.lesson_object.userId, glb.userName,
                                                               glb.rating)
        print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
        if response.get("code") == 400:
            pass
        else:
            data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_user_review_of_a_resource(self):
        """
            4.16修改评论
            1. 拿用户（id）对资源（id）的评论
            2. 返回200 - （前端认为已经有评论了，就修改评论）
            3. 取到对应的评论id，发editReviewRequest接口
        """
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        # 列表有十个资源取下标是从0开始
        resourceid = data_dec["items"][chosen]["id"]
        # 某个用户某个资源的详情 取返回来的rating
        response = self.lesson_object.get_user_review(self.lesson_object.userId, resourceid)
        if response.get("code") == 400:
            pass
        elif response.get("code") == 200:
            # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            # id = data_dec["id"]
            # rating=data_dec["rating"]
            # str_value = str(id)
            # print  ("<p>{}</p>".format(str_value))
            # response = self.lesson_object.put_user_review_of_a_resource(str_value,rating)
            # #在这个用户底下id出现400 提示"code":"LS/REVIEW_UPDATE_ERROR", "message":"review param is missing"
            # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            data = item(response)
            if data:  # 此用户有进行评价
                id = str(data['id'])
                rating = random.randint(1, 5)
                response = self.lesson_object.put_user_review_of_a_resource(id, resourceid, rating,
                                                                            self.lesson_object.userId)
            else:
                rating = random.randint(1, 5)
                response = self.lesson_object.post_resource_reviews_01(resourceid, self.lesson_object.userId,
                                                                       glb.USER_NAME, rating)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        else:
            print('<p>response code unequal 200 and 400</p>')

    def test_user_review_of_a_resource_01(self):
        '''
        4.1601
        修改评论
        1. 拿用户（id）对资源（id）的评论
        2. 返回200 - （前端认为已经有评论了，就修改评论）
        3. 取到对应的评论id，发editReviewRequest接口。
        '''
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        # 列表有十个资源取下标是从0开始
        resourceid = data_dec["items"][chosen]["id"]
        # 某个用户某个资源的详情 取返回来的rating
        response = self.lesson_object.get_user_review(self.lesson_object.userId, resourceid)
        if response.get("code") == 400:
            pass
        elif response.get("code") == 200:
            data = item(response)
            if data:  # 此用户有进行评价
                id = str(data['id'])
                rating = random.randint(1, 5)
                response = self.lesson_object.put_user_review_of_a_resource(id, resourceid, rating,
                                                                            self.lesson_object.userId)  # 修改评价
            else:
                rating = random.randint(1, 5)
                response = self.lesson_object.post_resource_reviews_01(resourceid, self.lesson_object.userId,
                                                                       glb.USER_NAME, rating)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        else:
            print('<p>response code unequal 200 and 400</p>')

    def test_user_review(self):
        """
            4.17 提交评论内容
            新增评论
            1. 拿用户（id）对资源（id）的评论
            2. 返回404 - （前端认为已经有评论了，就新增评论）（如果是其他的code，前端认为1没有获取成功，就把服务端的报错显示一下）
            3. 如果返回404，发postReviewRequest接口
        """
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = item(response)
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_user_review()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.get_user_review(self.lesson_object.userId, resource_id)
                data = item(response)

                if response.get("code") == 400:
                    pass
                elif response.get("code") == 200:
                    if data:  # 此用户有进行评价
                        id = data['id']
                        rating = random.randint(1, 5)
                        response = self.lesson_object.put_user_review_of_a_resource(id, resource_id, rating,
                                                                                    self.lesson_object.userId)
                    else:
                        rating = random.randint(1, 5)
                        response = self.lesson_object.post_resource_reviews_01(resource_id, self.lesson_object.userId,
                                                                               glb.USER_NAME, rating)

                    glb.rest_o.parse_response(response, glb.CODE200, glb.message)
                else:
                    print('<p>response code unequal 200 and 400</p>')
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_user_review_of_specific_resource(self):
        '''
        4.18
        '''
        print "<p>第一步，获取列表资源的id</p>"
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(glb.offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_user_review_of_specific_resource()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.get_user_review_of_specific_resource(resource_id, glb.offset_01,
                                                                                   glb.limit_01)
                data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_user_review_of_specific_resource(self):
        '''
        4.19
        '''
        print "<p>第一步，获取列表资源的id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        response = self.lesson_object.get_user_review_of_specific_resource(resourceid, glb.offset_01, glb.limit_01)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_get_number_of_rating(self):
        '''
        4.20 获取对应评分的人数
        '''
        print "<p>第一步，获取列表资源的id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        response = self.lesson_object.get_number_of_rating(resourceid)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_user_review(self):
        '''
        4.21 获取资源评分列表
        '''
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        response = self.lesson_object.get_resource_review_list(self.lesson_object.userId, resourceid)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_resource_sum_people(self):
        '''
       4.22 [POST]资源详情 总人数评论 探测性测试
        '''
        print "<p>先从评论列表获取人员评星级id</p>"
        response1 = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response1, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        # 获取id
        response = self.lesson_object.get_user_review_of_specific_resource(resourceid, glb.offset_01, glb.limit_01)
        print "<p>=====================\n{}\n===============</p>".format(response)
        id_items = item(response)
        # print "<p>。。。。。。。。。。{}。。。。。。。。。。。。。。</p>".format(id_items["items"][0]["rating"])
        print "<p>！！！！！！！！！！！！！！\n{}\n===============</p>".format(id_items)
        # 获取sum_people
        response2 = self.lesson_object.get_resourceList_information_none(resourceid, self.lesson_object.userId)
        print "<p>----------------------------\n{}\n------------------------------------</p>".format(response2)
        # 获取所有评论的总数等于评论列表的id  可以直接获取items的长度
        rating = item(response2)
        print "<p>rating============\n{}\n===============</p>".format(rating.get("custom_properties").get("sum_people"))
        print "<p>length============\n{}\n===============</p>".format(len(id_items.get("items")))
        # 考虑到数据一致性的问题，需要再刷新一次页面，所以再次请求。
        time.sleep(5)
        response3 = self.lesson_object.get_resourceList_information_none(resourceid, self.lesson_object.userId)
        rating_01 = item(response3)
        if rating_01.get("custom_properties").get("sum_people") == len(id_items.get("items")):
            pass
        else:
            pass

    @unittest.skip("1.1版本已经不涉及评分详情总人数的属性sum_people")
    def test_resource_sum_people_01(self):
        '''
       4.2201 [POST]资源详情 总人数评论
        '''
        print "<p>先从评论列表获取人员评星级id</p>"
        response1 = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response1, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        # 获取id
        response = self.lesson_object.get_user_review_of_specific_resource(resourceid, glb.offset_01, glb.limit_01)
        print "<p>=====================\n{}\n===============</p>".format(response)

        id_items = item(response)
        for s in range(0, len(id_items.get("items"))):
            i = 0
            if id_items["items"][s]["rating"] > 0:
                i += 1
        len_i = len([j["rating"] for j in id_items["items"] if j["rating"] > 0])
        response2 = self.lesson_object.get_resourceList_information_none(resourceid, self.lesson_object.userId)
        rating = item(response2)
        print "<p>rating============\n{}\n===============</p>".format(rating.get("custom_properties").get("sum_people"))
        print "<p>length============\n{}\n===============</p>".format(len(id_items.get("items")))
        # 考虑到数据一致性的问题，需要再刷新一次页面，所以再次请求。
        time.sleep(5)
        response3 = self.lesson_object.get_resourceList_information_none(resourceid, self.lesson_object.userId)
        rating_01 = item(response3)
        if rating_01.get("custom_properties").get("sum_people") == len_i:
            pass
        else:
            raise ValueError

    def test_get_tags_grade_level(self):
        '''
       4.23  [get] /gls/tag_cascades/{tag_path}?language={language}
        '''
        print "<p>先从评论列表获取人员评论id</p>"
        response1 = self.lesson_object.get_get_tags_for(glb.tag_path_01, glb.language)
        data_dec = glb.rest_o.parse_response(response1, glb.CODE200, glb.message)

    def test_get_tags_subject(self):
        '''
       4.24  [get] /gls/tag_cascades/{tag_path}?language={language}
        '''
        print "<p>先从评论列表获取人员评论id</p>"
        response1 = self.lesson_object.get_get_tags_for(glb.tag_path_02, glb.language)
        data_dec = glb.rest_o.parse_response(response1, glb.CODE200, glb.message)

    def test_get_tags_format(self):
        '''
       4.25  [get] /gls/tag_cascades/{tag_path}?language={language}
        '''
        print "<p>先从评论列表获取人员评论id</p>"
        response1 = self.lesson_object.get_get_tags_for(glb.tag_path_03, glb.language)
        data_dec = glb.rest_o.parse_response(response1, glb.CODE200, glb.message)

    def test_post_resource_reviews_v1(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_v1()
            else:
                chosen = random.randint(0, len(items) - 1)
                print('<p>资源{}</p>'.format(chosen))
                resource_id = items[chosen]["id"]
                print('<p>资源{}</p>'.format(chosen))
                response = self.lesson_object.post_resource_reviews_v1(resource_id, self.lesson_object.userId,
                                                                       glb.userName)
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_post_resource_reviews_un(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_un()
            else:
                chosen = random.randint(0, len(items) - 1)
                print('<p>资源{}</p>'.format(chosen))
                resource_id = items[chosen]["id"]
                print('<p>资源{}</p>'.format(chosen))
                response = self.lesson_object.post_resource_reviews_un(resource_id, self.lesson_object.userId,
                                                                       glb.userName)
                if response.get("code") == 403:
                    print "<p>报错403，没有权限</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_post_resource_reviews_v1_01(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_v1_01()
            else:
                chosen = random.randint(0, len(items) - 1)
                print('<p>资源{}</p>'.format(chosen))
                resource_id = items[9]["id"]
                print('<p>资源{}</p>'.format(resource_id))
                response = self.lesson_object.post_resource_reviews_v1_01(resource_id, self.lesson_object.userId,
                                                                          glb.userName)
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_post_resource_reviews_v1_02(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_v1_02()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.post_resource_reviews_v1_02(resource_id, self.lesson_object.userId,
                                                                          glb.userName)
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_post_resource_reviews_v1_03(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_v1_03()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.post_resource_reviews_v1_03(resource_id, self.lesson_object.userId,
                                                                          glb.userName)
                print('<p>资源{}</p>'.format(resource_id))
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_post_resource_reviews_v1_04(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_v1_03()
            else:
                chosen = random.randint(0, len(items) - 1)
                resource_id = items[chosen]["id"]
                response = self.lesson_object.post_resource_reviews_v1_04(resource_id, self.lesson_object.userId,
                                                                          glb.userName)
                print('<p>资源{}</p>'.format(resource_id))
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_post_resource_reviews_v1_05(self):
        '''
        4.14 获得某个用户的评分以及评论
        '''
        offset_ran = random.choice(glb.offset_ran)  # 0
        response = self.lesson_object.post_resourceList(offset_ran, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

        # 请求N页列表资源
        try:
            items = data_dec["items"]
            if len(items) < 1:  # 资源为空,重新请求
                glb.offset_ran.remove(offset_ran)  # list删除此元素
                self.test_post_resource_reviews_v1_03()
            else:
                chosen = random.randint(0, len(items) - 1)
                print('<p>资源{}</p>'.format(chosen))
                resource_id = items[chosen]["id"]
                response = self.lesson_object.post_resource_reviews_v1_05(resource_id, self.lesson_object.userId,
                                                                          glb.userName)
                print('<p>资源{}</p>'.format(resource_id))
                if response.get("code") == 400:
                    print "<p>报错400，是因为评分星星是一样的，所以已经存在了，且这个是新增评论的summbit接口，不是edit接口</p>"
                    pass
                else:
                    data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        except ValueError:
            print('<p>资源列表无资源</p>')

    def test_user_review_of_a_resource_v1(self):
        """
            4.16修改评论
            1. 拿用户（id）对资源（id）的评论
            2. 返回200 - （前端认为已经有评论了，就修改评论）
            3. 取到对应的评论id，发editReviewRequest接口
        """
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        # 列表有十个资源取下标是从0开始
        resourceid = data_dec["items"][chosen]["id"]
        # 某个用户某个资源的详情 取返回来的rating
        response = self.lesson_object.get_user_review_v1(self.lesson_object.userId, resourceid)
        if response.get("code") == 400:
            pass
        elif response.get("code") == 200:
            # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            # id = data_dec["id"]
            # rating=data_dec["rating"]
            # str_value = str(id)
            # print  ("<p>{}</p>".format(str_value))
            # response = self.lesson_object.put_user_review_of_a_resource(str_value,rating)
            # #在这个用户底下id出现400 提示"code":"LS/REVIEW_UPDATE_ERROR", "message":"review param is missing"
            # data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
            data = item(response)
            if data:  # 此用户有进行评价
                id = str(data['id'])
                rating = random.randint(1, 5)
                response = self.lesson_object.put_user_review_of_a_resource_v1(id, resourceid, rating,
                                                                               self.lesson_object.userId)
            else:
                rating = random.randint(1, 5)
                response = self.lesson_object.post_resource_reviews_v1(resourceid, self.lesson_object.userId,
                                                                       glb.USER_NAME)
            glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        else:
            print('<p>response code unequal 200 and 400</p>')

    def test_get_number_of_rating_v1(self):
        '''
        4.20获取对应评分的人数
        '''
        print "<p>第一步，获取列表资源的id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        response = self.lesson_object.get_number_of_rating_v1(resourceid)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    def test_user_review_of_specific_resource_v2(self):
        '''
        改造评论列表排序接口
        '''
        print "<p>第一步，获取列表资源的id</p>"
        response = self.lesson_object.post_resourceList(glb.offset, glb.limit, glb.language, glb.order)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)
        chosen = random.randint(0, 9)
        resourceid = data_dec["items"][chosen]["id"]
        response = self.lesson_object.get_user_review_of_specific_resource_v1(resourceid, glb.offset_01, glb.limit_01)
        data_dec = glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    # 获取收藏夹个数
    def test_get_collections_count(self):
        """
            获取收藏夹个数 [get]
        """
        response = self.lesson_object.get_collections_count(self.lesson_object.userId)
        glb.rest_o.parse_response(response, glb.CODE200, glb.message)

    # # 获取收藏夹标注
    # def test_post_collections_note(self):
    #     """
    #         获取收藏夹标注 [get]
    #     """
    #     response = self.lesson_object.post_collections_note()
    #     glb.rest_o.parse_response(response, glb.CODE200, glb.message)


if __name__ == "__main__":
    pass
