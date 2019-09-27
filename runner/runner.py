# coding=utf-8
import sys
import os
sys.path.insert(0, '..')
from nd.rest.sla.sla import SendSLA
from nd.rest.co_test.runner import run

__author__ = 'linzh'

reload(sys)

sys.setdefaultencoding('utf-8')
#
#
# proid = sys.argv[2]
res = run(os.path.realpath(__file__))
# sender_sla = SendSLA()
# if proid is not None:
#    print "接口监控报告推送："
#    print "proid：", proid
#    # 发送CS报告
#    sender_sla.send(res['url'], proid)
#    # 发送本地报告
#    sender_sla.send_local_report_url(res['report_local_url'], proid)