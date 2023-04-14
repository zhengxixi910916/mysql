from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "query_process_instances": "/workflow/$VERSION$/business/process/history/%s",  # 根据流程业务关联表查询流程实例相关信息
    "query_by_business": "/workflow/$VERSION$/business/process/ids/%s",  # 根据业务ID获取流程定义ID、流程实例ID、当前活动任务ID
})


def query_process_instances(self, business_id, checker=None):
    """
    接口名称：根据流程业务关联表查询流程实例相关信息;    接口地址：/workflow/$VERSION$/business/process/history/{businessId}；
    """
    r = RequestService.call_get(apis.get("query_process_instances", business_id), params={
        "activityId": "",  # 当前执行的活动的ID - required: False
        "processDefinitionKey": "",  # 流程定义的key - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_by_business(self, business_ids, checker=None):
    """
    接口名称：根据业务ID获取流程定义ID、流程实例ID、当前活动任务ID;    接口地址：/workflow/$VERSION$/business/process/ids/{businessIds}；
    """
    r = RequestService.call_get(apis.get("query_by_business", business_ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
