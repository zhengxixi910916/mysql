from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "hist_comments_using": "/workflow/$VERSION$/hist/comments",  # 查询审批历史记录
    "hist_comments_business": "/workflow/$VERSION$/hist/comments/businessdata",  # 查询审批历史记录相关联的业务表单数据
    "claim_using_g": "/workflow/$VERSION$/hist/%s/completetask",  # 已经审批过的流程节点
})


def hist_comments_using(self, records_id, checker=None):
    """
    接口名称：查询审批历史记录;    接口地址：/workflow/$VERSION$/hist/comments；
    """
    r = RequestService.call_get(apis.get("hist_comments_using", None), params={
        "processInstanceId": records_id  # 流程实例ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def hist_comments_business(self, process_instance_id, checker=None):
    """
    接口名称：查询审批历史记录相关联的业务表单数据;    接口地址：/workflow/$VERSION$/hist/comments/businessdata；
    """
    r = RequestService.call_get(apis.get("hist_comments_business", None), params={
        "processInstanceId": process_instance_id  # 流程实例ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def claim_using_g(self, process_instance_id, checker=None):
    """
    接口名称：已经审批过的流程节点;    接口地址：/workflow/$VERSION$/hist/{processInstanceId}/completetask；
    """
    r = RequestService.call_get(apis.get("claim_using_g", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
