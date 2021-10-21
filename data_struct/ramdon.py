# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/17
import random
import string

class Random(object):
    #seed = "1234567890abcdefghjklmnopqrstuvwxyz!@#$%^&&*()_+=-"
    def getramdondata(self):
        salt = ''.join(random.sample(string.ascii_letters+string.digits,5))
        return salt

