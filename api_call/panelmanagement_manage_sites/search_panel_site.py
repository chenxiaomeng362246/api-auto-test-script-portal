# coding=utf-8
# __author:chenxiaomeng
# date:2021/10/14
from util.manage_panel_http import BaseHttp


class SearchPanelSite(BaseHttp):
    def __init__(self, env='env'):
        super(SearchPanelSite, self).__init__(env=env)

    def search_panel_site(self, pageSize, pageNumber,sortField,searchString):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "searchSites",
            "variables": {
                "searchRequest": {
                    "pageSize": pageSize,
                    "pageNumber":pageNumber,
                    "sortField": sortField,
                    "sortDirection": "ASC",
                    "searchString": searchString,
                    "parentOrgPrn": "prn:Organization::PrometheanTest"
                }
            },
            "query": "query searchSites($searchRequest: SearchSitesInput!) {\n  searchSites(searchRequest: $searchRequest) {\n    sites {\n      id\n      prn\n      name\n      description\n      panelCount\n      notes\n      siteManagers {\n        firstName\n        lastName\n        email\n        __typename\n      }\n      __typename\n    }\n    totalElements\n    __typename\n  }\n}\n"
        }

        res = self.post(url, body)
        return res
