from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "modify_notify_using": "/workflow/$VERSION$/ntfcfg",  # 修改节点通知
    "add_notify_user": "/workflow/$VERSION$/ntfcfg/notify/user",  # 添加通知用户
    "del_notify_user": "/workflow/$VERSION$/ntfcfg/notify/user",  # 删除通知用户
    "del_notify_using": "/workflow/$VERSION$/ntfcfg/%s",  # 节点删除通知
    "add_notify_using": "/workflow/$VERSION$/ntfcfg/%s/%s",  # 添加节点通知
    "update_notify_using": "/workflow/$VERSION$/ntfcfg/%s/%s/%s",  # 修改节点通知
    "query_page_using": "/workflow/$VERSION$/userquit/queryPage",  # 查询离职用户
    "update_using_p": "/workflow/$VERSION$/userquit/%s",  # 状态修改
})


def modify_notify_using(self, act_id, def_id, list_, checker=None):
    """
    接口名称：修改节点通知;    接口地址：/workflow/$VERSION$/ntfcfg;
    """
    r = RequestService.call_put(apis.get("modify_notify_using", None), json=list_
                                , params={
            "actDefId": act_id,  # actDefId - required: True
            "procDefId": def_id,  # procDefId - required: True
        }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_notify_user(self, list_, checker=None):
    """
    接口名称：添加通知用户;    接口地址：/workflow/$VERSION$/ntfcfg/notify/user；	
    """
    r = RequestService.call_put(apis.get("add_notify_user", None), json=list_)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def del_notify_user(self, checker=None):
    """
    接口名称：删除通知用户;    接口地址：/workflow/$VERSION$/ntfcfg/notify/user；	
    """
    r = RequestService.call_delete(apis.get("del_notify_user", None), params={
        "etUserNotifyRelList": ""  # etUserNotifyRelList - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def del_notify_using(self, ids, checker=None):
    """
    接口名称：节点删除通知;    接口地址：/workflow/$VERSION$/ntfcfg/{ids}；	
    """
    r = RequestService.call_delete(apis.get("del_notify_using", ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_notify_using(self, act_id, def_id, list_, checker=None):
    """
    接口名称：添加节点通知;    接口地址：/workflow/$VERSION$/ntfcfg/{procDefId}/{actDefId}；	
    """
    r = RequestService.call_put(apis.get("add_notify_using", def_id, act_id), json=list_)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_notify_using(self, dto, def_id, act_id, mode_ids, checker=None):
    """
    接口名称：修改节点通知;    接口地址：/workflow/$VERSION$/ntfcfg/{procDefId}/{actDefId}/{notifyId}；	
    """
    r = RequestService.call_put(apis.get("update_notify_using", def_id, act_id, mode_ids), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using(self, checker=None):
    """
    接口名称：查询离职用户;    接口地址：/workflow/$VERSION$/userquit/queryPage；	
    """
    r = RequestService.call_get(apis.get("query_page_using", None), params={
        "createBy": "",  # None - required: False
        "createTime": "",  # None - required: False
        "id": "",  # 对象Id - required: False
        "pageIndex": "",  # 页码 - required: False
        "pageSize": "",  # 每页条数 - required: False
        "status": "",  # None - required: False
        "tenantId": "",  # None - required: False
        "updateBy": "",  # None - required: False
        "updateTime": "",  # None - required: False
        "userId": "",  # None - required: False
        "userName": "",  # None - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_using_p(self, checker=None):
    """
    接口名称：状态修改;    接口地址：/workflow/$VERSION$/userquit/{id}；	
    """
    r = RequestService.call_put(apis.get("update_using_p", None), json={
        "userQuit": ""  # 接口调用记录 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
