# coding=utf-8


__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
from api_call.base.txt_opera import TxtOpera
import testcases.account.xq_glb as glb
import random


class LessonPlan(BaseHttp):
    def __init__(self, env='dev'):
        super(LessonPlan, self).__init__(env=env)
        self.ssl = True
        self.token = ''

        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()

        self.cookies = ''
        self.XSRF_TOKEN = ''
        self.cookies_x = ''
        self.cookies_p = ''
        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()
        self.cookies = my_txt.read_txt_cookies()
        self.XSRF_TOKEN = my_txt.read_txt_cookies_x()
        self.cookies_x = my_txt.read_txt_cookies_x()
        self.cookies_p = my_txt.read_txt_cookies_p()
        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json",
                # my pumi
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                # Panel Management
                # "x-api-key": "bv6d45mobai6lk31l9sw6s9argxn42x0x35j7jlt"
                # user Management
                # "x-api-key": "hibkxo48a90bxkeaw22du9w01xnoy64y2itsmgv9"
                "Authorization": self.XSRF_TOKEN,
                # "XSRF-TOKEN" : self.XSRF_TOKEN,
                # "credentials": "include"
                "Cookie": "XSRF-TOKEN=" + self.XSRF_TOKEN + ";prom:sess=" + self.cookies_p
                # "Cookie":self.cookies
                # "Cookie": my_txt.read_txt_cookies()

            }
        elif self.env == 'sandbox':
            self.header = {
                "Content-Type": "application/json",
                "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
                "Authorization": self.XSRF_TOKEN,
                # "XSRF-TOKEN" : self.XSRF_TOKEN,
                # "credentials": "include"
                "Cookie": "XSRF-TOKEN=" + self.XSRF_TOKEN + ";prom:sess=" + self.cookies_p
                # "Cookie":self.cookies
                # "Cookie": my_txt.read_txt_cookies()
            }
        else:
            self.header = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Qa-Tag": "0",
                "Authorization": "DEBUG userid=2132756444,realm=oh"

            }
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=self.ssl)
        self.userId = self.get_user_info()

    # ============================================公共部分========================================

    def get_user_info(self):
        """
            user_info  //获取userId
        """
        url = '/profile/graphql'
        self.http_obj.set_header(self.header)
        params = {
            "query": "query getUserProfile { \n        getUserProfile {\n             id\n            email\n            firstName\n            lastName\n            displayName \n            publicName \n            favoriteColor \n            marketingOptIn \n            EULA \n            countryCode\n            languageCode \n            panelPreference { \n                wallpaperUrl\n                favoriteApps \n                json\n            } \n            json\n            avatar {\n                preSignedUrl\n                preSignedUrlTtl\n            }\n        } \n    }"
        }
        params = json.dumps(params)
        res = self.http_obj.post(url, params)
        get_user_profile = json.loads(res.get('data')).get('data')
        user_id = get_user_profile.get('getUserProfile').get('id')
        print('<p>{}</p>'.format(user_id))
        return user_id

    def post_login_AddCollection(self, userId, collection):
        """
      4.1.2 [POST] /Filters and sort
        """

        # url = "/learning-store/gls/collections"
        url = "/learning-store/gls/collections"
        params = {

            "userId": userId,
            "collection": collection

        }
        params = json_encode(params)

        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    # 资源搜索与排序
    def post_resourceList(self, offset, limit, language, order, keyword=None):
        """
        1.[POST] /资源搜索与排序[post]
        """

        # url = "/learning-store/ndr/resource/list"
        url = "/learning-store/gls/resources/action/search"
        params = {

            "offset": offset,
            "limit": limit,
            # "language": language,  # "en-US"
            "order": order,  # "Rating desc"
            "types": [],
            "grades": [],
            "subjects": []
        }

        # 按照关键字搜索
        if keyword:
            params['keyword'] = keyword

        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    # 资源搜索与排序 按平均分排列  大于一颗星，意思每个人评分都大于一颗星
    def post_resourceList_rating(self, offset, limit, language, order, rating):
        """
      1.[POST] /资源搜索与排序[post]
        """

        # url = "/learning-store/ndr/resource/list"
        url = "/learning-store/gls/resources/action/search"
        params = {

            "offset": offset,
            "limit": limit,
            "language": language,  # "en-US"
            "order": order,  # "Rating desc",
            "rating": rating
            # "types": [],
            # "grades": [],
            # "subjects": []
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    # 资源审核
    def post_resourceList_flag(self, user_id, resource_id, resource_title, comment, type):
        """
        # 1.[POST] /资源搜索与排序[post]
        1.[POST]  资源审核  //V0.2.4
        """
        url = "/learning-store/gls/users/" + user_id + "/resources/" + resource_id + "/flag"
        # params = {
        #     "comment": comment,
        #     "type": type}

        # V0.2.4
        type_description = {1: "Inappropriate content",
                            2: "Copyright infringement",
                            3: "Resource unavailable or unable to access resource",
                            4: "Other (please explain with additional information)"}
        # 处理type获取type_description
        if isinstance(type, str):
            type_list = type.split(',')
            description = list()
            for i in range(len(type_list)):
                description.append(type_description[int(type_list[i])])
            description = ';'.join(description)
        else:
            description = type_description[type]

        params = {
            "comment": comment,
            "type": type,
            "resourceTitle": resource_title,
            "resourceUrl": self.get_web_url() + '/detail/' + resource_id,
            "typeDescription" : description
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    # 资源详情
    def get_resourceList_information(self, resource_id, user_id):
        """
      1.[POST] Resource Information
        """
        url = "/learning-store/gls/resources/" + resource_id + "?&user_id=" + user_id
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_resourceList_information_none(self, resource_id, user_id):
        """
      1.[get] Resource Information
        """
        url = "/learning-store/gls/resources/" + resource_id + "?user_id=" + user_id
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res
        # 资源搜索与排序

    def post_resourceList_1(self, offset, limit, language, order, keyword):
        """
      1.[POST] /资源搜索与排序[post]
        """

        # url = "/learning-store/ndr/resource/list"
        url = "/learning-store/gls/resources/action/search"
        params = {

            "offset": offset,
            "limit": limit,
            "language": language,  # "en-US"
            "order": order,  # "Rating desc",
            "keyword": keyword
            # "types": [],
            # "grades": [],
            # "subjects": []
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resourceAdd(self, userId, collectionIds, resourceId):
        """
        4.4 将资源添加到colletction[post]
        """

        # url = "/learning-store/gls/resource/add/library"
        url = "/learning-store/gls/collections/resources"
        params = {
            "userId": userId,  # // 必填
            # "collectionId":"", #// 必填
            "collectionIds": collectionIds,  # // 前端迁移到这个参数后，将移除对collectionId的支持
            "resourceId": resourceId  # 资源id
            # "thumbnail":"", #// 选填
            # "type":"", #资源类型，用于排序
            # "grades":[""],# grade用于排序必填
            # "rating":, # rating用于排序选填，不填默认为0
            # "note":""
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_thumbnailAdd(self, ids):
        """
        4.7. 获取collection的缩略图信息[POST]
        """

        # url = "/learning-store/gls/resource/thumbnail/library"
        url = "/learning-store/gls/collections/thumbnails/action/search"
        params = {
            "ids": ids  # // 必填
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def put_login_UpdateCollection(self, id, userId, collection):
        """
        4.2 [PUT]/gls/collections/{collection_id}
        """

        # url = "/learning-store/gls/resource/update/library"

        url = "/learning-store/gls/collections/" + id
        params = {
            # "id": id,
            "userId": userId,
            "collection": collection,
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.put(url, params)
        return res

    def patch_mylibrary_id_deleted(self, id, delete):
        """
        4.1.5 [PATCH] //learning-store/gls/resource/delete/library/{id}/ 收藏夹删除或恢复
        """

        url = "/learning-store/gls/resource/delete/library/" + id
        self.http_obj.set_header(self.header)
        res = self.http_obj.patch(url, "")
        return res

    def delete_mylibrary_id(self, id):
        """
    4.3 [DELETE] //learning-store/gls/resource/delete/library/{id}/ 收藏夹删除 /gls/collections/{collection_id} 删除的是collection
        """

        # url = "/learning-store/gls/resource/delete/library/" + id
        url = "/learning-store/gls/collections/" + id
        self.http_obj.set_header(self.header)
        res = self.http_obj.delete(url)
        return res

    def get_resourceid(self):
        """
      4.1.1 [GET] /得到resourceid
        """

        url = "/learning-store/apps"

        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    # /learning-store/gls/resource/group/library/379563000@qq.com?offset=0&limit=12

    def delete_collection_id(self, collection_id):
        """
        4.1.5 [PATCH] /gls/collections/{collection_id}
        """

        url = "/learning-store/gls/collections/" + collection_id

        self.http_obj.set_header(self.header)
        res = self.http_obj.patch(url, "")
        return res

    def del_resource_delete_collection(self, collection_id, resource_id):
        """
    4.5 [delete] /gls/collections/{collection_id}/resources/{resource_id}
        """

        url = "/learning-store/gls/collections/" + collection_id + "/resources/" + resource_id
        self.http_obj.set_header(self.header)
        res = self.http_obj.delete(url)
        return res

    def get_collectionGroup(self, user_id, offset=0):
        """
      4.6 [GET] collectionGroup

        """

        # url = "/learning-store/gls/resource/group/library/"+user_id+"?offset=0&limit=12"
        url = "/learning-store/gls/users/" + user_id + "/collections/resources/number?" + str(offset) + "&limit=12"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    # /learning-store/gls/resource/group/library/379563000@qq.com?offset=0&limit=12

    def get_resourceid_group(self, userid):
        """
      4.6. collection分组[GET]
        """

        url = "/learning-store/gls/resource/group/library/" + userid + "?offset=0&limit=12"

        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def post_collection(self, offset, limit, collectionId, sort):
        """
      4.8. 获取collection中的资源列表[POST]
        """

        # url = "/learning-store/ls/resource/list/library"
        url = "/learning-store/gls/collections/resources/action/search"
        params = {

            "offset": offset,
            "limit": limit,
            "collectionId": collectionId,
            "sort": sort
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def get_list_collection_library(self, userId):
        """
      4.9. 获取某个用户下的所有collection列表[GET]
      Get total number of resource in all collections for a user
        """
        url = "/learning-store/gls/users/" + userId + "/collections/resources/number"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_resourceid_count(self, userId):
        """
      4.10. 统计某个用户my library中资源个数 GET
        """
        url = "/learning-store/gls/users/" + userId + "/resources/count"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_collectionid_count(self, user_id):
        """
      4.11 [get] /gls/users/{user_id}/resources/count
        """
        url = "/learning-store/gls/users/" + user_id + "/collections"

        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_resource_link(self, resource_id):
        """
      4.12 [get] /gls/users/{user_id}/resources/count
        """
        url = "/learning-store/gls/resources/" + resource_id + "/source_link"

        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    # 等级和评论的接口

    def post_resource_reviews(self, resource_id, userId, userName):
        """
        默认type=single
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews"
        params = {
            "userId": userId,
            "userName": userName
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_01(self, resource_id, userId, userName, rating):
        """
      4.14 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + resource_id + "/reviews"
        params = {
            "userId": userId,
            "userName": userName,
            "rating": rating
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def put_user_review_of_a_resource(self, id, resource_id, rating, userId):
        """
        4.15 [put] /gls/resources/reviews/{id} 修改评论
        """
        content = "修改评论评价语"
        url = "/learning-store/gls/resources/reviews/" + id + '?resource_id=' + resource_id
        params = {"content": content,
                  "rating": rating,
                  "userId": userId,
                  "userName": "lianuser"
                  }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.put(url, params)
        return res

    def put_user_review_of_a_resource_se(self, id, content, rating):
        """
        4.15 [put] /gls/resources/reviews/{id}
        """
        url = "/learning-store/gls/resources/reviews/" + id
        params = {
            "rating": rating,
            "content": content
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.put(url, params)
        return res

    def get_user_review(self, user_id, resource_id):
        """
     4.16 [GET] /gls/users/{user_id}/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/users/" + user_id + "/resources/" + resource_id + "/reviews"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_resource_review_list(self, user_id, resource_id):
        """
     4.16_01 [GET] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + resource_id + "/reviews"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_user_review_of_specific_resource(self, resource_id, offset, limit):
        """
        4.17 [get] /gls/resources/{resource_id}/reviews?offset={offset}&limit={limit}
        """
        url = "/learning-store/gls/resources/" + resource_id + "/reviews?offset=" + offset + "&limit=" + limit
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_number_of_rating(self, resource_id):
        """
        4.18 [get] /gls/resources/{resource_id}/ratings/number
        """
        url = "/learning-store/gls/resources/" + resource_id + "/ratings/number"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_get_tags_for(self, tag_path, language):
        """
      4.19 [get] /gls/users/{user_id}/resources/count
        """
        url = "/learning-store/gls/tag_cascades/" + tag_path + "?language=" + language

        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def post_whether_resource_collected(self, user_id, ids):
        """
        4.20 [post] /gls/users/{user_id}/collections/action/exist
        """
        url = "/learning-store/gls/users/" + user_id + "/collections/action/exist"
        params = {
            "ids": ids  # // 必填
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_logout_Ls(self, email, password):
        """
      4.1.2 [POST] / usermanagement 登录接口
        """
        url = "/identity/logout"
        params = {}
        params = json_encode(params)

        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_v1(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": userId,
            "userName": userName,
            "avgItems": [],
            "content": "tab \t",
            "sumItems": []
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_un(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": "66c6e254-f01c-44f8-8729-6f72f49be167",
            "userName": userName,
            "avgItems": [],
            "content": "tab \t",
            "sumItems": []
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_v1_01(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": userId,
            "userName": userName,
            "avgItems":
                [{
                    "code": "thinkingSkills",
                    "rating": 3
                }],
            "content": "tab \n" + str(time.strftime("%Y%m%d%H%M%S", time.localtime())),
            "sumItems":
                [{
                    "code": "s1",
                    "rating": 1
                }]
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_v1_02(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": userId,
            "userName": userName,
            "avgItems":
                [{
                    "code": "easyToUseAndUnderstand",
                    "rating": 3
                },
                    {
                        "code": "appropriate",
                        "rating": 4
                    },
                    {
                        "code": "studentResponsivenes",
                        "rating": 4
                    },
                    {
                        "code": "multipleIntelligences",
                        "rating": 5
                    },
                    {
                        "code": "thinkingSkills",
                        "rating": 3
                    }
                ],
            "content": "tab \n" + str(time.strftime("%Y%m%d%H%M%S", time.localtime())),
            "sumItems":
                [{
                    "code": "recommend",
                    "rating": 1
                }]
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_v1_03(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": userId,
            "userName": userName,
            "avgItems":
                [{
                    "code": "overall",
                    "rating": 1
                },
                    {
                        "code": "easyToUseAndUnderstand",
                        "rating": 2
                    },
                    {
                        "code": "appropriate",
                        "rating": 3
                    },
                    {
                        "code": "studentResponsivenes",
                        "rating": 4
                    },
                    {
                        "code": "multipleIntelligences",
                        "rating": 5
                    }],
            "content": "tab \n" + str(time.strftime("%Y%m%d%H%M%S", time.localtime())),
            "sumItems":
                [{
                    "code": "recommend",
                    "rating": 1
                }]
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_v1_04(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": userId,
            "userName": userName,
            "avgItems":
                [{
                    "code": "overall1",
                    "rating": 1
                },
                    {
                        "code": "easyToUseAndUnderstand1",
                        "rating": 2
                    },
                    {
                        "code": "appropriate1",
                        "rating": 3
                    },
                    {
                        "code": "studentResponsivenes1",
                        "rating": 4
                    },
                    {
                        "code": "multipleIntelligences1",
                        "rating": 5
                    }],
            "content": "tab \n" + str(time.strftime("%Y%m%d%H%M%S", time.localtime())),
            "sumItems":
                [{
                    "code": "recommend1",
                    "rating": 1
                }]
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def post_resource_reviews_v1_05(self, resource_id, userId, userName):
        """
        改造接口 type=multiple
      4.13 [post] /gls/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/resources/" + str(resource_id) + "/reviews?type=multiple"
        params = {
            "userId": userId,
            "userName": userName,
            "avgItems":
                [{
                    "code": "overall1",
                    "rating": 1
                },
                    {
                        "code": "easyToUseAndUnderstand1",
                        "rating": 2
                    },
                    {
                        "code": "appropriate1",
                        "rating": 3
                    },
                    {
                        "code": "studentResponsivenes1",
                        "rating": 4
                    },
                    {
                        "code": "multipleIntelligences1",
                        "rating": 5
                    }],
            "content": "",
            "sumItems":
                [{
                    "code": "recommend1",
                    "rating": 1
                }]
        }
        params = json.dumps(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, params)
        return res

    def put_user_review_of_a_resource_v1(self, id, resource_id, rating, userId):
        """
        改造接口 type=multiple
        4.15 [put] /gls/resources/reviews/{id} 修改评论
        """
        content = "修改评论评价语"
        url = "/learning-store/gls/resources/reviews/" + id + '?type=multiple&resource_id=' + resource_id
        params = {
            "content": "this is very good resource ,I like it ，thank you for suporting" + str(
                time.strftime("%Y%m%d%H%M%S", time.localtime())),
            "avgItems": [{
                "code": "easyToUseAndUnderstand",
                "rating": rating
            }, {
                "code": "appropriate",
                "rating": 4
            }, {
                "code": "studentResponsivenes",
                "rating": 2
            }, {
                "code": "thinkingSkills",
                "rating": 2
            }, {
                "code": "multipleIntelligences",
                "rating": 2
            }],
            "sumItems": [{
                "code": "recommend",
                "rating": 1
            }],
            "rating": 2
        }
        params = json_encode(params)
        self.http_obj.set_header(self.header)
        res = self.http_obj.put(url, params)
        return res

    def get_user_review_v1(self, user_id, resource_id):
        """
        改造接口 type=multiple
     4.16 [GET] /gls/users/{user_id}/resources/{resource_id}/reviews
        """
        url = "/learning-store/gls/users/" + user_id + "/resources/" + resource_id + "/reviews?type=multiple"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_user_review_of_specific_resource_v1(self, resource_id, offset, limit):
        """
        改造接口 type=multiple
        4.17 [get] /gls/resources/{resource_id}/reviews?offset={offset}&limit={limit}
        """
        url = "/learning-store/gls/resources/" + resource_id + "/reviews?offset=" + offset + "&limit=" + limit
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_number_of_rating_v1(self, resource_id):
        """
            改造接口 type=multiple
            4.18 [get] /gls/resources/{resource_id}/ratings/number
        """
        url = "/learning-store/gls/resources/" + resource_id + "/ratings/number?type=multiple"
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def get_collections_count(self, user_id):
        """
            获取收藏夹个数  //[get] /learning-store/gls/users/{user_id}/collections/count
        """
        url = '/learning-store/gls/users/' + user_id + '/collections/count'
        res = self.http_obj.get(url)
        return res