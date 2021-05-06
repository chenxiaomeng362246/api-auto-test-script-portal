# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import time
import uuid
import pprint
import unittest
from hamcrest import *
from unittest import SkipTest
from nd.rest.rand import CoRand
from nd.rest.restful import Restful


__author__ = "Administrator"  # 开发

#
# 整个工程使用的一套环境代号请保持一致！
#

# 开发
DEV = "dev"

# 测试
TEST = "test"

# 预生产
PRE = "sandbox"
SANDBOX = "sandbox"
STAGING = "staging"

# 生产
PRO = "pro"
PROD = "prod"



# 本地调试代码时使用的环境
# ENVIRONMENT = TEST100
# ENVIRONMENT = TEST
# ENVIRONMENT = DEV
ENVIRONMENT = PRE
# ENVIRONMENT = PRO
# ENVIRONMENT = WJT
# ENVIRONMENT = AWS
# ENVIRONMENT = AWSCA

#
# ---- 用例适用等级 ----
# 版本测试-测试环境 1
# 版本测试-预生产环境 2
# 版本测试-生产环境 3
# 准入测试（开发/测试环境）4
# 每日构建（测试环境） 5
# 生产拨测（监控） 6
# WJT测试 7
# AWS环境测试   8
# AWSCA环境测试 9
