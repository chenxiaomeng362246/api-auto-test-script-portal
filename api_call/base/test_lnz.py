#coding=utf-8
import random
import uuid

# name = 'test_name'
# # # namespace = 'test_namespace'
# # namespace = uuid.NAMESPACE_URL
# #
# # print uuid.uuid1()
# # print uuid.uuid3(namespace,name)
# # print uuid.uuid4()
# # print uuid.uuid5(namespace,name)

if __name__ == "__main__":
        my_list = list(range(4))
        print(my_list)
        print(random.shuffle(my_list))
        print(my_list)