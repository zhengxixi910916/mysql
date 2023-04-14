from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "del_read_informed_using_delete": "/workflow/$VERSION$/process/record/del/read/%s",  # 删除已读的知会
    "del_read_using_delete": "/workflow/$VERSION$/process/record/del/%s",  # 删除流程记录
    "informed_task_using_post": "/workflow/$VERSION$/process/record/informed",  # 任务知会
    "mark_read_using_post": "/workflow/$VERSION$/process/record/informed/mark/read",  # 标记未读为已读
    "query_informed_using_get": "/workflow/$VERSION$/process/record/informed/page",  # 分页查询流程知会我的
    "query_page_using_get_6": "/workflow/$VERSION$/process/record/page",  # 分页查询流程记录
    "query_inst_page_using_get": "/workflow/$VERSION$/process/record/queryInstPage",  # 分页查询流程实例记录
})


def del_read_informed_using_delete(self, informed_ids, checker=None):
    """
    接口名称：删除已读的知会
    接口地址：/workflow/$VERSION$/process/record/del/read/{informedIds}
    """
    r = RequestService.call_delete(apis.get("del_read_informed_using_delete", informed_ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def del_read_using_delete(self, records_id_1, checker=None):
    """
    接口名称：删除流程记录
    接口地址：/workflow/$VERSION$/process/record/del/{ids}
    """
    r = RequestService.call_delete(apis.get("del_read_using_delete", records_id_1), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def informed_task_using_post(self, comment, informed_user_id, task_id, checker=None):
    """
    接口名称：任务知会
    接口地址：/workflow/$VERSION$/process/record/informed
    """
    r = RequestService.call_post(apis.get("informed_task_using_post", None), params={
        "comment": comment,  # 备注 - required: False
        "informedUserId": informed_user_id,  # 被知会人ID - required: True
        "taskId": task_id,  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def mark_read_using_post(self, informed_ids="", checker=None):
    """
    接口名称：标记未读为已读
    接口地址：/workflow/$VERSION$/process/record/informed/mark/read
    """
    r = RequestService.call_post(apis.get("mark_read_using_post", None), params={
        "informedIds": informed_ids  # informedIds，多个逗号隔开 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_informed_using_get(self, page_index=1, page_size=100, checker=None):
    """
    接口名称：分页查询流程知会我的
    接口地址：/workflow/$VERSION$/process/record/informed/page
    """
    r = RequestService.call_get(apis.get("query_informed_using_get", None), params={
        "appId": "",  # 应用ID - required: False
        "pageIndex": page_index,  # 页码 - required: False
        "pageSize": page_size,  # 页大小 - required: False
        "procInstId": "",  # 流程实例Id - required: False
        "processName": "",  # 流程名称 - required: False
        "remark": "",  # 备注 - required: False
        "sign": "",  # 标记是否流程管理查询 - required: False
        "state": "",  # 状态：1 已读，0未读 - required: False
        "taskId": "",  # 任务Id - required: False
        "taskName": "",  # 任务名称 - required: False
        "type": "",  # 类型 - required: False
        "userIds": "",  # userIds，多个逗号隔开 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_page_using_get_6(self, dto, checker=None):
    """
    接口名称：分页查询流程记录
    接口地址：/workflow/$VERSION$/process/record/page
    """
    r = RequestService.call_get(apis.get("query_page_using_get_6", None), params={
        "appId": dto.get("appId", "erdp"),
        "type": dto.get("type", ""),
        "difference": dto.get("difference", "-1"),
        "category": dto.get("category", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "processInstId": dto.get("processInstId", ""),
        "processInstName": dto.get("processInstName", ""),
        "pager_name": dto.get("pager_name", "20"),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_inst_page_using_get(self, dto, checker=None):
    """
    接口名称：分页查询流程实例记录
    接口地址：/workflow/$VERSION$/process/record/queryInstPage
    """
    r = RequestService.call_get(apis.get("query_inst_page_using_get", None), params={
        "appId": dto.get("appId", "erdp"),
        "type": dto.get("type", ""),
        "difference": dto.get("difference", "-1"),
        "category": dto.get("category", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "processInstId": dto.get("processInstId", ""),
        "processInstName": dto.get("processInstName", ""),
        "pager_name": dto.get("pager_name", "20"),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r
