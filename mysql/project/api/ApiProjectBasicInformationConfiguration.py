from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目基础信息配置
'''
apis = Api({
    "showNoticeConfigUsingPOST": "/proj/$VERSION$/notice/get",  # 显示基础配置信息
    "addNoticeConfigUsingPUT": "/proj/$VERSION$/notice/%s/add",  # 配置基础信息
})


def showNoticeConfigUsingPOST(self, project_id, checker=None):
    """
    接口名称：显示基础配置信息
    接口地址：/proj/$VERSION$/notice/get
    """
    r = RequestService.call_post(apis.get("showNoticeConfigUsingPOST", None), json={
        "projectId": [project_id],
        "type" : ""# 通知配置对象 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r['res']["data"]
    else:
        apis.check_success(self, r)
        return r['res']["data"]


def addNoticeConfigUsingPUT(self, project_id, task_patternid,requirement_patternid,issue_patternid,risk_patternid,project_patternid,checker=None):
    """
    接口名称：配置基础信息
    接口地址：/proj/$VERSION$/notice/{project_id}/add
    """
    r = RequestService.call_put(apis.get("addNoticeConfigUsingPUT", project_id), json=[{
        "patternId":task_patternid,
        "notiType":"ELTask",
        "available":"Y",
        "ruleList":
            [{
                "id":"430af59b7f8bb9bf4d31aada738a67af",
                "ruleDesc":"light-yellow",
                "ruleNum":"3"
            },{
                "id":"f40f4fc4b61b54506cc733136adf6e38",
                "ruleDesc":"light-red",
                "ruleNum":"0"
            }]},{
        "patternId":requirement_patternid,
        "notiType":"ELRequirement",
        "available":"Y",
        "ruleList":
            [{
                "id":"e5a3f8ffdadd2a28db2fdf6b02e07e3d",
                "ruleDesc":"light-yellow",
                "ruleNum":"3"
            },{
                "id":"3c7cb6ced6d948b21ae560ceb2af59b0",
                "ruleDesc":"light-red",
                "ruleNum":"5"
            }]},{
        "patternId":issue_patternid,
        "notiType":"ELIssue",
        "available":"Y",
        "ruleList":
            [{
                "id":"1da4601e73f6adbee84828167259352d",
                "ruleDesc":"light-yellow",
                "ruleNum":"3"
            },{
                "id":"79119ee7ae0a978cdded55af04f22e7e",
                "ruleDesc":"light-red",
                "ruleNum":"0"
            }]},{
        "patternId":risk_patternid,
        "notiType":"ELRisk",
        "available":"Y",
        "ruleList":
            [{
                "id":"d72b0d9442f2aac3cb520606695208a5",
                "ruleDesc":"light-yellow","ruleNum":"3"
            },{
                "id":"802fe99768bd819b2d503dc180e7637a",
                "ruleDesc":"light-red",
                "ruleNum":"0"
            }]},{
        "patternId":project_patternid,
        "notiType":"ELProject",
        "available":"Y",
        "ruleList":
            [{
                "id":"9bbc81dde489784b0037ae45d863973c",
                "ruleDesc":"light-yellow",
                "ruleNum":"1"
            },{
                "id":"698e13060967ea58daa17786b7a0ca56",
                "ruleDesc":"light-red",
                "ruleNum":"10"
            }],
        "pattern":"progressCompare"
    }], )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r
