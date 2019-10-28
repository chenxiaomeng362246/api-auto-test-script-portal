#  coding=utf-8
import random
import datetime
import nd.rest.restful as CoRestful
import time, json
import os
import time
from config.gbl import *
import uuid

# lesson_object = Gjj_api.LessonPlan()
rest_o = CoRestful.Restful()

# ======================================
CODE201 = 201
CODE200 = 200
CODE204 = 204
CODE302 = 302
CODE400 = 400
CODE403 = 403
CODE404 = 404
CODE406 = 406
CODE500 = 500
message = "用例执行失败"
# =============================login部分====================================
# userId = "850900451@qq.com"
# userId = "379563000@qq.com"
# user_name = "lnz300005@nd.com.cn"
# password_ds = "1QAZxsw2"
# USER_NAME = "lianuser"

user_name = "17689406280@sina.cn"
password_ds = "Jin-111111"

userId_01 = ""
userId_02 = "asdasdsadsadsadsadsadasdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadsadsads"
userId_03 = "legenecy@163.com"
# new_collection="newcolle{}".format(random.randint(1,100))

new_collection = "newcolle" + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
cnt_collection = 0
# new_collection_01="newcolle_01{}".format(random.randint(1,100))
new_collection_01 = "newcolle_01" + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
new_collection_02 = "newcolle_02   " + str(time.strftime("%Y%m%d%H%M%S",
                                                         time.localtime())) + "asdasdsadsadsadsadsadasdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadsadsads"
NEW_COLLECTION_03 = "-_-|||"
# collection="{}sdfdd".format(random.randint(1,100))
collection = "Favorite" + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
# update_collection="kkfdd{}".format(random.randint(1,100))
update_collection = "kkfdd{}" + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
offset = 0
limit = 12
offset_01 = '0'
limit_01 = '10'
limit_4 = "null"
offset_4 = "null"
offset_ran = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108]
limit_search = 10
language = "en-US"
order = "Rating desc"
order_1 = "Grade Level desc"
order_2 = "Type desc"
sort = "Rating desc"
userName = "lian"
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
email = "850900451@qq.com"
password = "Qazxsw1234"
tag_path_01 = "PROMETHEAN_SUBJECT"
tag_path_02 = "PROMETHEAN_GRADE_LEVEL"
tag_path_03 = "PROMETHEAN_FILE_FORMAT"
# email="379563000@qq.com"
email_0 = ""
email_1 = "aaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA111222288<P>"
email_2 = "learningsrorebetful@qq.com"
# password="Abc123456789"
password_0 = ""
password_1 = "Legenecy04042222"
password_2 = "Le1234"
password_3 = "登陆密码无数字字母>八位"
keyword = "#"
keyword_1 = "1111 #"
keyword_2 = "<p>#"
keyword_3 = "台独"
keyword_4 = "语文"
comment = time.strftime("%Y-%m-%d", time.localtime()) + "测试资源审核" + CoRand.randomword(3)
type = random.randint(1, 4)
rating = random.randint(1, 5)

comment_v2 = time.strftime("%Y-%m-%d", time.localtime()) + "测试资源审核" + CoRand.randomwordmulcode(100)
type_v33 = "1,2,3,4"

# type_v2 = list(range(4)+1)
# print(my_list)
# print(random.shuffle(my_list))
# print(my_list)
# 第一步 生成list
type_v2 = list(range(1, 5))
# 第二步  把list转换成无序
type_v3 = random.shuffle(type_v2)
# 第三步 把数组转为字符串
str3 = ','
seq5 = []
for i in range(len(type_v2)):
    seq5.append(str(type_v2[i]))
type_v4 = str3.join(seq5)

rating_cl = 2.5
content = "sdffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd"

# ============Learning Store修改账号和密码=====================
password_pre = "Jin-111111"

password_new = "Jin-111111"
password_pre_01 = "Jin-111111"
password_new_01 = "Jin-111111"

# email_ds="lnz300005@nd.com.cn"
# password_ds="1QAZxsw2"
# email_ds = "nl5882112@126.com"
# password_ds = "Chen123456"
# =============================地质活动部分====================================
print(comment)
print(type)
