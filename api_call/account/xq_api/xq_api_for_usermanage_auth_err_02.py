# coding=utf-8


__author__ = 'Administrator'
import json
import time
import nd.rest.http_mot as CoHttpM
from tornado.escape import json_encode
from api_call.base.http import BaseHttp
import config.gbl as g
from api_call.base.txt_opera import TxtOpera


class LessonPlan(BaseHttp):
    def __init__(self, env='dev'):
        super(LessonPlan, self).__init__(env=env)
        self.ssl = True
        self.token = ''
        self.cookies = ''
        self.XSRF_TOKEN=''
        self.cookies_x=''
        self.cookies_p = ''
        # token
        my_txt = TxtOpera()
        self.token = my_txt.read_txt()
        self.cookies=my_txt.read_txt_cookies()
        self.XSRF_TOKEN = my_txt.read_txt_cookies_x()
        self.cookies_x=my_txt.read_txt_cookies_x()
        self.cookies_p = my_txt.read_txt_cookies_p()


        if self.env == 'dev':
            self.header = {
                "Content-Type": "application/json",
                # MyPromethean
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                "Authorization":"b830506d-a1a1-4293-a0ba-a7d6787d246a",
               "Cookie":"XSRF-TOKEN=b830506d-a1a1-4293-a0ba-a7d6787d246a;prom:sess=eyJqd3QiOiJleUpyYVdRaU9pSlFlVXcwY1Rkb1JsaFpZWFpyWmtod1ZFMURaVzlhUlVaSWFVNTVXRU5LY1d3elpFbFRVVTQxVFdSQlBTSXNJbUZzWnlJNklsSlRNalUySW4wLmV5SnpkV0lpT2lJNU1XWXdNRGxpWlMxaFpHVmhMVFJrWVdZdFlUTTBOUzAyTm1JeFpUQTBaRFF6TURRaUxDSmpiR2xsYm5SSlpDSTZJalp4T1dobmIyUTVNbTR5ZFRCbE9UaHdNRFZ3TUc1dmFYQTFJaXdpWlcxaGFXeGZkbVZ5YVdacFpXUWlPblJ5ZFdVc0ltbHpjeUk2SW1oMGRIQnpPbHd2WEM5amIyZHVhWFJ2TFdsa2NDNTFjeTFsWVhOMExURXVZVzFoZW05dVlYZHpMbU52YlZ3dmRYTXRaV0Z6ZEMweFgzcHlWR3BuWjNkNFZ5SXNJbU52WjI1cGRHODZkWE5sY201aGJXVWlPaUk1TVdZd01EbGlaUzFoWkdWaExUUmtZV1l0WVRNME5TMDJObUl4WlRBMFpEUXpNRFFpTENKbmFYWmxibDl1WVcxbElqb2liR2xoYmlJc0ltRjFaQ0k2SWpaeE9XaG5iMlE1TW00eWRUQmxPVGh3TURWd01HNXZhWEExSWl3aVpYWmxiblJmYVdRaU9pSXlaR1F4TVRRMU1pMDBOR0l4TFRSaU1HUXRZVE5sTkMxbE1HRXlNakl3WldNNU1USWlMQ0owYjJ0bGJsOTFjMlVpT2lKcFpDSXNJbkJ5YjJacGJHVmZhV1FpT2lJNVlqTTJPR1F6TVMxbE9UQXhMVFEwTmpZdFlqQXlaQzB4TURSbFlUTTRaalExTURFaUxDSmhkWFJvWDNScGJXVWlPakUxTmpVeE5UazFNekFzSW1WNGNDSTZNVFUyTlRFMk16RXpNQ3dpYVdGMElqb3hOVFkxTVRVNU5UTXdMQ0ptWVcxcGJIbGZibUZ0WlNJNkltNTJlbWgxWVc1MWMyVnlhMnc3YXpzaUxDSmxiV0ZwYkNJNklteHVlak13TURBd05VQnVaQzVqYjIwdVkyNGlmUS5YSHBUbTAyREZSOXVFMEl5NXpiT202VWdaS193X3ktSmZYSnhNOHFBWDF0SDFKVW41SC1XTmx0SFNVVXhJejV6MzFBZHh4aU9pdXZRSWpOVGZSTDlrYk5fenpJdWN0anBxWTlnTlJhSHRVQVNaVXhNZGt5R2NmNENTZ1MtMEEwZUk0Y1pERUt2QmI1Q2lVS20xMHk0a1c5Y3QtQ2xhb0MxQU5Od1g2eGRzcjhiZ2lfWHJmNGhtSzNicGxXYjhFY0tqOEQyR1RNS0tVamE1OUkwTk9nR2R1dUhFbmtvLVNvTEJoSFdvbWgwRm95N2txU2VSVzg5bWk4ZS14ODJUZjVaSkxpc3paeEZlZDdTU2JtSlJYcXl6U3BNWWxpYkpnSUE2azFacXRleGhGVjZCUl9uVmlwV25QSmZKSVAzV29LZkpadlRnanBwMEQxQ2otMGIwNFJWTHciLCJhY2Nlc3NUb2tlbiI6ImV5SnJhV1FpT2lJd09FVjNjR2wwY2xWUWJVVkZiR1JNWkZaVFJtTk1jMWxwVW5WRmNGVk1lSEF6T1Uxck5YSXJhblpKUFNJc0ltRnNaeUk2SWxKVE1qVTJJbjAuZXlKemRXSWlPaUk1TVdZd01EbGlaUzFoWkdWaExUUmtZV1l0WVRNME5TMDJObUl4WlRBMFpEUXpNRFFpTENKbGRtVnVkRjlwWkNJNklqSmtaREV4TkRVeUxUUTBZakV0TkdJd1pDMWhNMlUwTFdVd1lUSXlNakJsWXpreE1pSXNJblJ2YTJWdVgzVnpaU0k2SW1GalkyVnpjeUlzSW5OamIzQmxJam9pWVhkekxtTnZaMjVwZEc4dWMybG5ibWx1TG5WelpYSXVZV1J0YVc0aUxDSmhkWFJvWDNScGJXVWlPakUxTmpVeE5UazFNekFzSW1semN5STZJbWgwZEhCek9sd3ZYQzlqYjJkdWFYUnZMV2xrY0M1MWN5MWxZWE4wTFRFdVlXMWhlbTl1WVhkekxtTnZiVnd2ZFhNdFpXRnpkQzB4WDNweVZHcG5aM2Q0VnlJc0ltVjRjQ0k2TVRVMk5URTJNekV6TUN3aWFXRjBJam94TlRZMU1UVTVOVE14TENKcWRHa2lPaUl5TUdFNU9XUTVZeTA1WVdVeUxUUmhPVEV0WWpjMk5pMDVaVGxoTkRVeU1ETXdZaklpTENKamJHbGxiblJmYVdRaU9pSTJjVGxvWjI5a09USnVNblV3WlRrNGNEQTFjREJ1YjJsd05TSXNJblZ6WlhKdVlXMWxJam9pT1RGbU1EQTVZbVV0WVdSbFlTMDBaR0ZtTFdFek5EVXROalppTVdVd05HUTBNekEwSW4wLkRLNEZIMFRfdjFvVUdaVlJBR1E4SWVMeFZZVUduQ0hoaHhrYWRfeXo2enBkdmNfTm5XRnF4YkREOXZNTUZFLTVkZmNQeWR5X3JubmZncnNxWFpjam00RHczZDhiVVJPUzBHNWxrU0pyMGpGeTlWbGE2VEJ0N1ptVUc5ZWV5MDFBZzlrSjhoa2hmOTRDckNlSldydFY5TlB4em14UVFvYllremdoTXhSeGRWWVBOMkNMRmxpd0pTa1ZPLTVYa3ljS0dtQTJhTGllUy1ralZjeEhJWmxtX3BKQ2U4MWYzUG15VHRvM255SlBlTkJoTFMtUjFWYmVWVTl1ZFM3UHJZTXlHS3A2MWVxRTVVSW16b3Y0bVEyQmhJOUU0cUNycmhrTFRnbHNhUDNwbHRtWnF5SnZxQkdIQk84ajhoVjdhRVUyMHF3bkpaZV8zcFhSR1Y2Z1FrY3FoZyIsIl9leHBpcmUiOjE1NjUxNjI1MzEzMDEsIl9tYXhBZ2UiOjMwMDAwMDB9"
            }
        elif self.env == 'sandbox':
            self.header = {
                # "Accept": "application/json",
                "Content-Type": "application/json",
                # MyPromethean
                "x-api-key": "s42d9y1yomrbi87rkewyx6ebqil9zo08gibhttjp",
                "Authorization": "b830506d-a1a1-4293-a0ba-a7d6787d246a",
                "Cookie": "XSRF-TOKEN=b830506d-a1a1-4293-a0ba-a7d6787d246a;prom:sess=eyJqd3QiOiJleUpyYVdRaU9pSlFlVXcwY1Rkb1JsaFpZWFpyWmtod1ZFMURaVzlhUlVaSWFVNTVXRU5LY1d3elpFbFRVVTQxVFdSQlBTSXNJbUZzWnlJNklsSlRNalUySW4wLmV5SnpkV0lpT2lJNU1XWXdNRGxpWlMxaFpHVmhMVFJrWVdZdFlUTTBOUzAyTm1JeFpUQTBaRFF6TURRaUxDSmpiR2xsYm5SSlpDSTZJalp4T1dobmIyUTVNbTR5ZFRCbE9UaHdNRFZ3TUc1dmFYQTFJaXdpWlcxaGFXeGZkbVZ5YVdacFpXUWlPblJ5ZFdVc0ltbHpjeUk2SW1oMGRIQnpPbHd2WEM5amIyZHVhWFJ2TFdsa2NDNTFjeTFsWVhOMExURXVZVzFoZW05dVlYZHpMbU52YlZ3dmRYTXRaV0Z6ZEMweFgzcHlWR3BuWjNkNFZ5SXNJbU52WjI1cGRHODZkWE5sY201aGJXVWlPaUk1TVdZd01EbGlaUzFoWkdWaExUUmtZV1l0WVRNME5TMDJObUl4WlRBMFpEUXpNRFFpTENKbmFYWmxibDl1WVcxbElqb2liR2xoYmlJc0ltRjFaQ0k2SWpaeE9XaG5iMlE1TW00eWRUQmxPVGh3TURWd01HNXZhWEExSWl3aVpYWmxiblJmYVdRaU9pSXlaR1F4TVRRMU1pMDBOR0l4TFRSaU1HUXRZVE5sTkMxbE1HRXlNakl3WldNNU1USWlMQ0owYjJ0bGJsOTFjMlVpT2lKcFpDSXNJbkJ5YjJacGJHVmZhV1FpT2lJNVlqTTJPR1F6TVMxbE9UQXhMVFEwTmpZdFlqQXlaQzB4TURSbFlUTTRaalExTURFaUxDSmhkWFJvWDNScGJXVWlPakUxTmpVeE5UazFNekFzSW1WNGNDSTZNVFUyTlRFMk16RXpNQ3dpYVdGMElqb3hOVFkxTVRVNU5UTXdMQ0ptWVcxcGJIbGZibUZ0WlNJNkltNTJlbWgxWVc1MWMyVnlhMnc3YXpzaUxDSmxiV0ZwYkNJNklteHVlak13TURBd05VQnVaQzVqYjIwdVkyNGlmUS5YSHBUbTAyREZSOXVFMEl5NXpiT202VWdaS193X3ktSmZYSnhNOHFBWDF0SDFKVW41SC1XTmx0SFNVVXhJejV6MzFBZHh4aU9pdXZRSWpOVGZSTDlrYk5fenpJdWN0anBxWTlnTlJhSHRVQVNaVXhNZGt5R2NmNENTZ1MtMEEwZUk0Y1pERUt2QmI1Q2lVS20xMHk0a1c5Y3QtQ2xhb0MxQU5Od1g2eGRzcjhiZ2lfWHJmNGhtSzNicGxXYjhFY0tqOEQyR1RNS0tVamE1OUkwTk9nR2R1dUhFbmtvLVNvTEJoSFdvbWgwRm95N2txU2VSVzg5bWk4ZS14ODJUZjVaSkxpc3paeEZlZDdTU2JtSlJYcXl6U3BNWWxpYkpnSUE2azFacXRleGhGVjZCUl9uVmlwV25QSmZKSVAzV29LZkpadlRnanBwMEQxQ2otMGIwNFJWTHciLCJhY2Nlc3NUb2tlbiI6ImV5SnJhV1FpT2lJd09FVjNjR2wwY2xWUWJVVkZiR1JNWkZaVFJtTk1jMWxwVW5WRmNGVk1lSEF6T1Uxck5YSXJhblpKUFNJc0ltRnNaeUk2SWxKVE1qVTJJbjAuZXlKemRXSWlPaUk1TVdZd01EbGlaUzFoWkdWaExUUmtZV1l0WVRNME5TMDJObUl4WlRBMFpEUXpNRFFpTENKbGRtVnVkRjlwWkNJNklqSmtaREV4TkRVeUxUUTBZakV0TkdJd1pDMWhNMlUwTFdVd1lUSXlNakJsWXpreE1pSXNJblJ2YTJWdVgzVnpaU0k2SW1GalkyVnpjeUlzSW5OamIzQmxJam9pWVhkekxtTnZaMjVwZEc4dWMybG5ibWx1TG5WelpYSXVZV1J0YVc0aUxDSmhkWFJvWDNScGJXVWlPakUxTmpVeE5UazFNekFzSW1semN5STZJbWgwZEhCek9sd3ZYQzlqYjJkdWFYUnZMV2xrY0M1MWN5MWxZWE4wTFRFdVlXMWhlbTl1WVhkekxtTnZiVnd2ZFhNdFpXRnpkQzB4WDNweVZHcG5aM2Q0VnlJc0ltVjRjQ0k2TVRVMk5URTJNekV6TUN3aWFXRjBJam94TlRZMU1UVTVOVE14TENKcWRHa2lPaUl5TUdFNU9XUTVZeTA1WVdVeUxUUmhPVEV0WWpjMk5pMDVaVGxoTkRVeU1ETXdZaklpTENKamJHbGxiblJmYVdRaU9pSTJjVGxvWjI5a09USnVNblV3WlRrNGNEQTFjREJ1YjJsd05TSXNJblZ6WlhKdVlXMWxJam9pT1RGbU1EQTVZbVV0WVdSbFlTMDBaR0ZtTFdFek5EVXROalppTVdVd05HUTBNekEwSW4wLkRLNEZIMFRfdjFvVUdaVlJBR1E4SWVMeFZZVUduQ0hoaHhrYWRfeXo2enBkdmNfTm5XRnF4YkREOXZNTUZFLTVkZmNQeWR5X3JubmZncnNxWFpjam00RHczZDhiVVJPUzBHNWxrU0pyMGpGeTlWbGE2VEJ0N1ptVUc5ZWV5MDFBZzlrSjhoa2hmOTRDckNlSldydFY5TlB4em14UVFvYllremdoTXhSeGRWWVBOMkNMRmxpd0pTa1ZPLTVYa3ljS0dtQTJhTGllUy1ralZjeEhJWmxtX3BKQ2U4MWYzUG15VHRvM255SlBlTkJoTFMtUjFWYmVWVTl1ZFM3UHJZTXlHS3A2MWVxRTVVSW16b3Y0bVEyQmhJOUU0cUNycmhrTFRnbHNhUDNwbHRtWnF5SnZxQkdIQk84ajhoVjdhRVUyMHF3bkpaZV8zcFhSR1Y2Z1FrY3FoZyIsIl9leHBpcmUiOjE1NjUxNjI1MzEzMDEsIl9tYXhBZ2UiOjMwMDAwMDB9"

            }
        else:
            self.header = {
                "Content-Type": "application/json",
                "x-api-key": "lbu4509y4qecawd1sb2dwmur8mom718kn9lxk1cw",
                # Panel Management?
                # user Management?
                "Authorization":self.XSRF_TOKEN,
                # "XSRF-TOKEN" : self.XSRF_TOKEN,
                # "credentials": "include"
                 "Cookie":"XSRF-TOKEN="+self.XSRF_TOKEN+";prom:sess="+self.cookies_p
                # "Cookie":self.cookies
                # "Cookie": my_txt.read_txt_cookies()
            }
        self.http_obj = CoHttpM.Http(self.get_ybm_host(), self.get_port(), ssl=self.ssl)

    # ============================================公共部分========================================


    def post_list_query(self):
        """
      4.1.2 [POST] /Filters and sort
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res



    def post_list_query_all_des(self):
        """
      4. [POST] /Filters and sort 选择全部
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":100,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}],\"accountStatus\":[{\"prn\":\"prn:AccountStatus:System:Active\"},{\"prn\":\"prn:AccountStatus:System:Suspended\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_list_query_all(self):
        """
      4. [POST] /Filters and sort 选择全部
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":100,\"sortDirection\":\"ASC\",\"sortField\":\"lastName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}],\"accountStatus\":[{\"prn\":\"prn:AccountStatus:System:Active\"},{\"prn\":\"prn:AccountStatus:System:Suspended\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def get_user_permissions(self):
        """
       get
        """
        url = "/identity/user/permissions"
        # payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:OrganizationAdministrator\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"},{\"prn\":\"prn:Role:System:PanelAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.get(url)
        return res

    def post_set_roles_for_user(self):
        """
        给一个用户一个角色
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"firstName\",\"filter\":{}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res


    def post_filter_list(self):
        """
         过滤老师和普米管理员账号
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"DESC\",\"sortField\":\"email\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_filter_list_page(self):
        """
         过滤老师和普米管理员账号 加上切换一个页面显示的条数100条
        """

        # url = "/learning-store/gls/collections"
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":100,\"sortDirection\":\"DESC\",\"sortField\":\"email\",\"filter\":{\"roles\":[{\"prn\":\"prn:Role:System:Teacher\"},{\"prn\":\"prn:Role:System:PrometheanAdministrator\"}]}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_search_users(self):
        """
         搜索一个用户名字叫"Dan"
        """

        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"ASC\",\"sortField\":\"firstName\",\"filter\":{\"fullTextSearchString\":\"Dan\"}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_remove_a_role(self):
        """
         选择一个用户去除角色
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"GetUsers\",\"variables\":{\"org\":\"prn:Organization::Promethean\",\"pageNumber\":1,\"pageSize\":25,\"sortDirection\":\"ASC\",\"sortField\":\"firstName\",\"filter\":{\"fullTextSearchString\":\"\"}},\"query\":\"query GetUsers($org: String!, $pageNumber: Int!, $pageSize: Int!, $sortDirection: SortDirection!, $sortField: SortField!, $filter: SearchFilter!) {\\n  searchUsers(searchCriteria: {orgPrn: $org, pageNumber: $pageNumber, pageSize: $pageSize, sortDirection: $sortDirection, sortField: $sortField, searchFilter: $filter}) {\\n    users {\\n      prn\\n      firstName\\n      lastName\\n      email\\n      roles {\\n        prn\\n        name\\n        __typename\\n      }\\n      accountStatus {\\n        prn\\n        name\\n        __typename\\n      }\\n      dateRegistered\\n      lastSignedIn\\n      __typename\\n    }\\n    totalPages\\n    isLastPage\\n    isFirstPage\\n    currentPage\\n    totalElements\\n    __typename\\n  }\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res

    def post_a_role_suspended(self):
        """
         选择lnz300005@nd.com.cn一个用户suspended
        """
        url = "/user-management/graphql"
        payload = "{\"operationName\":\"disableUserInOrg\",\"variables\":{\"disableUserInput\":{\"orgPrn\":\"prn:Organization::Promethean\",\"userPrn\":\"prn:User::lnz300005@nd.com.cn\"}},\"query\":\"mutation disableUserInOrg($disableUserInput: EnableOrDisableUserInOrgInput!) {\\n  disableUserInOrg(disableUserInput: $disableUserInput)\\n}\\n\"}"
        # params = json_encode(payload)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, payload)
        return res