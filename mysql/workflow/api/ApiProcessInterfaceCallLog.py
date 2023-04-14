from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "get_invoke_log_history_using_get": "/workflow/$VERSION$/interfaceinvoklog/getHistory/{invokeLogId}",  # 查看调用记录历史
    "get_interface_invoke_inst_log_using_get": "/workflow/$VERSION$/interfaceinvoklog/query/inst/page",  # 查询流程实例调用记录
    "get_interface_invoke_log_using_get": "/workflow/$VERSION$/interfaceinvoklog/query/log/list",  # 查询流程实例调用记录
    "get_interface_record_using_get": "/workflow/$VERSION$/interfaceinvoklog/queryPage",  # 查看调用记录
    "retry_using_post": "/workflow/$VERSION$/interfaceinvoklog/retry",  # 接口调用重试
})


def get_invoke_log_history_using_get(self, checker=None):
    """
    接口名称：查看调用记录历史
    接口地址：/workflow/$VERSION$/interfaceinvoklog/getHistory/{invokeLogId}
    """
    r = RequestService.call_get(apis.get("get_invoke_log_history_using_get", ), params={
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_interface_invoke_inst_log_using_get(self, dto, checker=None):
    """
    接口名称：查询流程实例调用记录
    接口地址：/workflow/$VERSION$/interfaceinvoklog/query/inst/page
    """
    r = RequestService.call_get(apis.get("get_interface_invoke_inst_log_using_get", None), params={
        "tenantId": dto.get("tenantId", "erdp"),
        "procInstName": dto.get("procInstName", ""),
        "procInstId": dto.get("procInstId", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "interfaceName": dto.get("interfaceName", ""),
        "interfaceType": dto.get("interfaceType", ""),
        "taskKey": dto.get("taskKey", ""),
        "operatorUser": dto.get("operatorUser", ""),
        "result": dto.get("result", ""),
        "syncFlag": dto.get("syncFlag", ""),
        "order": dto.get("order", ""),
        "orderByField": dto.get("orderByField", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_interface_invoke_log_using_get(self, dto, checker=None):
    """
    接口名称：查询流程实例调用记录
    接口地址：/workflow/$VERSION$/interfaceinvoklog/query/log/list
    """
    r = RequestService.call_get(apis.get("get_interface_invoke_log_using_get", None), params={
        "tenantId": dto.get("tenantId", "erdp"),
        "procInstName": dto.get("procInstName", ""),
        "procInstId": dto.get("procInstId", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "interfaceName": dto.get("interfaceName", ""),
        "interfaceType": dto.get("interfaceType", ""),
        "taskKey": dto.get("taskKey", ""),
        "operatorUser": dto.get("operatorUser", ""),
        "result": dto.get("result", ""),
        "syncFlag": dto.get("syncFlag", ""),
        "order": dto.get("order", ""),
        "orderByField": dto.get("orderByField", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_interface_record_using_get(self, dto, checker=None):
    """
    接口名称：查看调用记录
    接口地址：/workflow/$VERSION$/interfaceinvoklog/queryPage
    """
    r = RequestService.call_get(apis.get("get_interface_record_using_get", None), params={
        "tenantId": dto.get("tenantId", "erdp"),
        "procInstName": dto.get("procInstName", ""),
        "procInstId": dto.get("procInstId", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "interfaceName": dto.get("interfaceName", ""),
        "interfaceType": dto.get("interfaceType", ""),
        "taskKey": dto.get("taskKey", ""),
        "operatorUser": dto.get("operatorUser", ""),
        "result": dto.get("result", ""),
        "syncFlag": dto.get("syncFlag", ""),
        "order": dto.get("order", ""),
        "orderByField": dto.get("orderByField", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def retry_using_post(self, dto, checker=None):
    """
    接口名称：接口调用重试
    接口地址：/workflow/$VERSION$/interfaceinvoklog/retry
    """
    r = RequestService.call_post(apis.get("retry_using_post", None), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r