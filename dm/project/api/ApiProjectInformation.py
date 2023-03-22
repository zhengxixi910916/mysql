# -*- coding: utf-8 -*-#
# Author:zhihuimin
# Date:2022/7/7
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
apis = Api({
    "updateApplicationConfigUsingPUT": "/proj/$VERSION$/basic/config/-1/update",  # 修改系统应用配置
})

def update_application_config(self, checker=None):
    """
    接口名称：修改系统应用配置
    接口地址：/proj/$VERSION$/basic/config/-1/update
    """
    r = RequestService.call_put(apis.get("updateApplicationConfigUsingPUT", None),json={
                    "config": "[{\"processDefinitionKey\":\"PROJECT_PUBLISH\",\"baselineType\":\"task,project,require\",\"name\":\"项目计划发布配置\"},{\"processDefinitionKey\":\"MILESTONE_UPDATE\",\"baselineType\":\"task\",\"name\":\"计划里程碑变更\"}]",
                    "contextId": "all",
                    "delFlag": "0",
                    "description": "系统自动基线配置",
                    "id": "38a60511ef71409bad12bec7bef2b091",
                    "name": "系统自动基线配置",
                    "type": "baseline"# 基础配置 - required: False
                })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r