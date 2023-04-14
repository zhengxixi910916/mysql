from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "download_file_using": "/workflow/$VERSION$/procinst/attachment/download/%s",  # 下载附件
    "upload_file_using": "/workflow/$VERSION$/procinst/attachment/upload",  # 上传附件
    "delete_attachment_using": "/workflow/$VERSION$/procinst/attachment/%s/%s",  # 删除附件
    "submit_bacth_process": "/workflow/$VERSION$/procinst/batchStart",  # 批量启动流程
    "check_user_in": "/workflow/$VERSION$/procinst/checkUserInProcess/%s",  # 判断人员是否在流程中
    "replace_all_process": "/workflow/$VERSION$/procinst/modifyuser/%s",  # 修改流程已处理节点/未来节点的处理人
    "query_process_instance1": "/workflow/$VERSION$/procinst/query/config/list/%s/%s",
    # 查询流程实例所有节点的配置和接口调用日志
    "query_process_instance2": "/workflow/$VERSION$/procinst/query/list/%s/%s",
    # 查询相同流程定义，且处于同一节点的流程实例
    "query_process_instance3": "/workflow/$VERSION$/procinst/query/variable/%s",  # 判断人员是否在流程中
    "query_process_instance": "/workflow/$VERSION$/procinst/query/%s",  # 根据流程实例ID查询流程实例信息
    "running_using_g": "/workflow/$VERSION$/procinst/running",  # 查询正在运行的流程
    "running_by_user": "/workflow/$VERSION$/procinst/running/%s",  # 查询正在运行的流程
    "query_submitted_process": "/workflow/$VERSION$/procinst/submitted",  # 查询当前用户启动的流程
    "update_process_instance": "/workflow/$VERSION$/procinst/update/attachment",  # 更新流程附件
    "business_key_start": "/workflow/$VERSION$/procinst/%s/businessKeyStartProcess",  # 根据业务对象ID查询是否有正在运行的流程
    "get_diagram_by": "/workflow/$VERSION$/procinst/%s/nodes",  # 查询当前流程实例所有元素
    "getlast_version_nodes1": "/workflow/$VERSION$/procinst/%s/nodes/lastversion",
    # 查询最新版本的流程定义的所有元素
    "getlast_version_nodes": "/workflow/$VERSION$/procinst/%s/nodes/lastversion/%s",
    # 根据业务类型定义及业务状态查询最新版本的流程定义的所有元素
    "submit_process_and": "/workflow/$VERSION$/procinst/%s/%s/%s/start",
    # 根据业务对象类型PPM_PLAN_***和业务状态启动流程
    "submit_process_using": "/workflow/$VERSION$/procinst/%s/%s/start",  # 根据Key启动流程
    "activate_process_instance": "/workflow/$VERSION$/procinst/%s/activate",  # 激活流程实例
    "get_assign_list": "/workflow/$VERSION$/procinst/%s/assign",  # 根据流程实例id查询处理人
    "get_highlighted_using": "/workflow/$VERSION$/procinst/%s/highlights",  # 当前活动节点
    "set_process_users": "/workflow/$VERSION$/procinst/%s/setProcessUsers",  # 设置节点处理人
    "suspend_process_instance": "/workflow/$VERSION$/procinst/%s/suspend",  # 挂起流程实例
    "update_process_name": "/workflow/$VERSION$/procinst/%s/updateProcessName",  # 修改流程实例的标题
})



def download_file_using(self, checker=None):
    """
    接口名称：下载附件;    接口地址：/workflow/$VERSION$/procinst/attachment/download/{dirId}；
    """
    r = RequestService.call_get(apis.get("download_file_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def upload_file_using(self, checker=None):
    """
    接口名称：上传附件;    接口地址：/workflow/$VERSION$/procinst/attachment/upload；
    """
    r = RequestService.call_post(apis.get("upload_file_using", None), data={
        "file": ""  # file - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_attachment_using(self, checker=None):
    """
    接口名称：删除附件;    接口地址：/workflow/$VERSION$/procinst/attachment/{processInstanceId}/{fileId}；
    """
    r = RequestService.call_delete(apis.get("delete_attachment_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def submit_bacth_process(self, checker=None):
    """
    接口名称：批量启动流程;    接口地址：/workflow/$VERSION$/procinst/batchStart；
    """
    r = RequestService.call_post(apis.get("submit_bacth_process", None), json={
        "startProcessList": ""  # startProcessList - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def check_user_in(self, user_id, process_instance_id, checker=None):
    """
    接口名称：判断人员是否在流程中;    接口地址：/workflow/$VERSION$/procinst/checkUserInProcess/{processInstanceId}；
    """
    r = RequestService.call_get(apis.get("check_user_in", process_instance_id), params={
        "userId": user_id  # 用户ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def replace_all_process(self, checker=None):
    """
    接口名称：修改流程已处理节点/未来节点的处理人;    接口地址：/workflow/$VERSION$/procinst/modifyuser/{userId}；
    """
    r = RequestService.call_post(apis.get("replace_all_process", None), json={
        "processInstanceDtos": ""  # 替换ID与用户集合 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_instance1(self, process_instance_id, process_definition_id, checker=None):
    """
    接口名称：查询流程实例所有节点的配置和接口调用日志;    接口地址：/workflow/$VERSION$/procinst/query/config/list/{processInstanceId}/{processDefinitionId}；
    """
    r = RequestService.call_get(apis.get("query_process_instance1", process_instance_id, process_definition_id, ), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_instance2(self, process_instance_id, activity_id, checker=None):
    """
    接口名称：查询相同流程定义，且处于同一节点的流程实例;    接口地址：/workflow/$VERSION$/procinst/query/list/{processDefinitionId}/{activityId}；
    """
    r = RequestService.call_get(apis.get("query_process_instance2", process_instance_id, activity_id), params={
        "pageIndex": 1,  # None - required: True
        "pageSize": 20,  # None - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_instance3(self, variable_name, process_instance_id, checker=None):
    """
    接口名称：判断人员是否在流程中;    接口地址：/workflow/$VERSION$/procinst/query/variable/{processInstanceId}；
    """
    r = RequestService.call_get(apis.get("query_process_instance3", process_instance_id), params={
        "variableName": variable_name  # 变量名称 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_instance(self, process_instance_id, checker=None):
    """
    接口名称：根据流程实例ID查询流程实例信息;    接口地址：/workflow/$VERSION$/procinst/query/{processInstanceId}；
    """
    r = RequestService.call_get(apis.get("query_process_instance", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def running_using_g(self, dto, checker=None):
    """
    接口名称：查询正在运行的流程;    接口地址：/workflow/$VERSION$/procinst/running；
    """
    r = RequestService.call_get(apis.get("running_using_g", None), params={
        "tenantId": dto.get("tenantId", "department"),
        "category": dto.get("category", ""),
        "title": dto.get("title", ""),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
        "contextType": dto.get("contextType", "0"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def running_by_user(self, user_id, checker=None):
    """
    接口名称：查询正在运行的流程;    接口地址：/workflow/$VERSION$/procinst/running/{userId}；
    """
    r = RequestService.call_get(apis.get("running_by_user", user_id), params={
        "pageIndex": 1,  # 页码 - required: False
        "pageSize": 20,  # 页大小 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

def query_submitted_process(self, dto, checker=None):
    """
    接口名称：查询当前用户启动的流程;    接口地址：/workflow/$VERSION$/procinst/submitted；
    """
    r = RequestService.call_get(apis.get("query_submitted_process", None), params={
        "tenantId": dto.get("tenantId", "type1"),
        "processDefinitionKey": dto.get("processDefinitionKey"),
        "title": dto.get("title"),
        "category": dto.get("category", "others"),
        "activityAssigneeList": dto.get("activityAssigneeList"),
        "taskStartTimeStart": dto.get("taskStartTimeStart"),
        "taskStartTimeEnd": dto.get("taskStartTimeEnd"),
        "processInstanceEndTimeStart": dto.get("processInstanceEndTimeStart"),
        "processInstanceEndTimeEnd": dto.get("processInstanceEndTimeEnd"),
        "pager_name": dto.get("pager_name", 20),
        "sort_by": dto.get("sort_by"),
        "order_by": dto.get("order_by", 20),
        "pageIndex": dto.get("pageIndex", 1),
        "contextType": dto.get("contextType", 0),
        "taskStartTimeFrom": dto.get("taskStartTimeFrom"),
        "taskStartTimeTo": dto.get("taskStartTimeTo"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_process_instance(self, checker=None):
    """
    接口名称：更新流程附件;    接口地址：/workflow/$VERSION$/procinst/update/attachment；
    """
    r = RequestService.call_put(apis.get("update_process_instance", None), json={
        "attachmentId": "",  # 旧附件ID - required: True
        "newFilePath": "",  # 新附件ID - required: True
        "processInstanceId": "",  # 流程实例ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def business_key_start(self, business_key, checker=None):
    """
    接口名称：根据业务对象ID查询是否有正在运行的流程;    接口地址：/workflow/$VERSION$/procinst/{businessKey}/businessKeyStartProcess；
    """
    r = RequestService.call_get(apis.get("business_key_start", business_key), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_diagram_by(self, process_definition_key, process_instance_id, checker=None):
    """
    接口名称：查询当前流程实例所有元素;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionId}/nodes；
    """
    r = RequestService.call_get(apis.get("get_diagram_by", process_definition_key), params={
        "processInstanceId": process_instance_id  # 流程实例ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def getlast_version_nodes1(self, process_definition_key, process_instance_id, checker=None):
    """
    接口名称：查询最新版本的流程定义的所有元素;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionKey}/nodes/lastversion；
    """
    r = RequestService.call_get(apis.get("getlast_version_nodes1", process_definition_key), params={
        "processInstanceId": process_instance_id  # 流程实例ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def getlast_version_nodes(self, process_definition_key, business_state, process_instance_id, checker=None):
    """
    接口名称：根据业务类型定义及业务状态查询最新版本的流程定义的所有元素;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionKey}/nodes/lastversion/{businessState}；
    """
    r = RequestService.call_get(apis.get("getlast_version_nodes", process_definition_key, business_state, ), params={
        "processInstanceId": process_instance_id  # 流程实例ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def submit_process_and(self, checker=None):
    """
    接口名称：根据业务对象类型PPM_PLAN_***和业务状态启动流程;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionKey}/{businessState}/{category}/start；
    """
    r = RequestService.call_post(apis.get("submit_process_and", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def submit_process_using(self, checker=None):
    """
    接口名称：根据Key启动流程;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionKey}/{category}/start；
    """
    r = RequestService.call_post(apis.get("submit_process_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def activate_process_instance(self, process_instance_id, checker=None):
    """
    接口名称：激活流程实例;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/activate；
    """
    r = RequestService.call_get(apis.get("activate_process_instance", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_assign_list(self, process_instance_id, checker=None):
    """
    接口名称：根据流程实例id查询处理人;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/assign；
    """
    r = RequestService.call_get(apis.get("get_assign_list", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_highlighted_using(self, process_instance_id, checker=None):
    """
    接口名称：当前活动节点;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/highlights；
    """
    r = RequestService.call_get(apis.get("get_highlighted_using", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def set_process_users(self, list_, process_instance_id, checker=None):
    """
    接口名称：设置节点处理人;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/setProcessUsers；
    """
    r = RequestService.call_post(apis.post("set_process_users", process_instance_id), params={
        "activityIdUsersJson": str(list_)})
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def suspend_process_instance(self, process_instance_id, checker=None):
    """
    接口名称：挂起流程实例;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/suspend；
    """
    r = RequestService.call_get(apis.get("suspend_process_instance", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_process_name(self, title, process_instance_id, checker=None):
    """
    接口名称：修改流程实例的标题;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/updateProcessName；
    """
    r = RequestService.call_post(apis.get("update_process_name", process_instance_id), params={
        "title": title  # 流程实例的标题 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
