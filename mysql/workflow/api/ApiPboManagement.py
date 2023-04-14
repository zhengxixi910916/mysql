from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "get_pbo_list": "/workflow/pbo/list",  # 查询Pbo列表
    "get_pbo_status": "/workflow/pbo/state/list",  # Pbo状态列表
})


def get_pbo_list(self, checker=None):
    """
    接口名称：查询Pbo列表;    接口地址：/workflow/pbo/list；	
    """
    r = RequestService.call_get(apis.get("get_pbo_list", None), params={
        "StartUserId": "",  # 流程启动人 - required: False
        "current": "",  # 页码 - required: False
        "name": "",  # 名称 - required: False
        "number": "",  # 编码 - required: False
        "pboType": "",  # pbo类型 - required: False
        "processId": "",  # 流程id - required: False
        "processName": "",  # 模板名称 - required: False
        "proposerId": "",  # 申请人id - required: False
        "size": "",  # 页大小 - required: False
        "startUserId": "",  # None - required: False
        "流程状态": "",  # None - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_pbo_status(self, app_id, checker=None):
    """
    接口名称：Pbo状态列表;    接口地址：/workflow/pbo/state/list；	
    """
    r = RequestService.call_get(apis.get("get_pbo_status", None), params={
        "appId": app_id  # appId - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
