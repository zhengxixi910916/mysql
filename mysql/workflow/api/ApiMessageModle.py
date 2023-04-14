from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_using_p": "/workflow/$VERSION$/msgmode",  # 创建消息模板
    "modify_using_p": "/workflow/$VERSION$/msgmode",  # 修改消息模板
    "query_page_using": "/workflow/$VERSION$/msgmode/page",  # 分页查询消息模板
    "query_by_variables": "/workflow/$VERSION$/msgmode/variables",  # 获取模板变量列表
    "del_using_d": "/workflow/$VERSION$/msgmode/%s",  # 删除消息模板
    "query_by_id": "/workflow/$VERSION$/msgmode/%s",  # 根据ID查询消息模板
})


def add_using_p(self, dto, checker=None):
    """
    接口名称：创建消息模板;    接口地址：/workflow/$VERSION$/msgmode；
    """
    r = RequestService.call_post(apis.get("add_using_p", None), params={
        "modeName": dto.get("modeName", "转办test"),
        "notifyType": dto.get("notifyType", "transfer"),
        "templateCode": dto.get("templateCode", "test001"),
        "dateNode": dto.get("dateNode", "0"),
        "sendTime": dto.get("sendTime", "00:00"),
        "available": dto.get("available", "Y"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def modify_using_p(self, message_mode, checker=None):
    """
    接口名称：修改消息模板;    接口地址：/workflow/$VERSION$/msgmode；
    """
    r = RequestService.call_put(apis.get("modify_using_p", None), json=message_mode)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using(self, dto, checker=None):
    """
    接口名称：分页查询消息模板;    接口地址：/workflow/$VERSION$/msgmode/page；
    """
    r = RequestService.call_get(apis.get("query_page_using", None), params={
        "tenantId": dto.get("tenantId", "department"),
        "modeName": dto.get("modeName", ""),
        "pager_name": dto.get("pager_name", "20"),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
        "contextTyp": dto.get("contextTyp", "0"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_by_variables(self, checker=None):
    """
    接口名称：获取模板变量列表;    接口地址：/workflow/$VERSION$/msgmode/variables；
    """
    r = RequestService.call_get(apis.get("query_by_variables", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def del_using_d(self, mode_ids, checker=None):
    """
    接口名称：删除消息模板;    接口地址：/workflow/$VERSION$/msgmode/{modeIds}；
    """
    r = RequestService.call_delete(apis.get("del_using_d", mode_ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_by_id(self, mode_ids, checker=None):
    """
    接口名称：根据ID查询消息模板;    接口地址：/workflow/$VERSION$/msgmode/{modeId}；
    """
    r = RequestService.call_get(apis.get("query_by_id", mode_ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
