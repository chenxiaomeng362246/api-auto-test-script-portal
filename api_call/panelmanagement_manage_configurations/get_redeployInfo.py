# coding = utf-8
# __author:chenxiaomeng
# date:2021/10/19
from util.manage_panel_http import BaseHttp
class Redeployinfo(BaseHttp):
    def __init__(self, env='env'):
        super(Redeployinfo, self).__init__(env=env)

    def redeployinfo(self):
        url = '/mdm-portal/graphql'
        body = {
            "operationName": "reDeployTemplateConfigs",
            "variables": {
                "reDeployTemplateRequest": {
                    "source": "gms",
                    "enableTarget": {
                        "hierarchy": "organization",
                        "targets": [
                            "60b63190-0832-88c0-d843-a6cda5c4eda9"
                        ]
                    },
                    "options": {
                        "sourceDetail": {
                            "enable": True
                        }
                    },
                    "extend": "{\"ownerName\":\"Google\",\"sites\":[],\"isEnableChanged\":true,\"isPanelSelectionChanged\":true}"
                }
            },
            "query": "mutation reDeployTemplateConfigs($reDeployTemplateRequest: IReDeployTemplateRequest!) {\n  reDeployTemplateConfigs(reDeployTemplateRequest: $reDeployTemplateRequest)\n}\n"
        }
        res = self.post(url, body)
        return res
