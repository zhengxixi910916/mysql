from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "get_activity_img": "/workflow/$VERSION$/task/activitycoor/%s",  # 当前流程活动节点坐标信息 x,y,height,width
    "delete_file_using": "/workflow/$VERSION$/task/attachment/%s",  # 删除附件
    "get_attachment_list": "/workflow/$VERSION$/task/attachments",  # 获取附件列表
    "claim_using_p": "/workflow/$VERSION$/task/claim",  # 任务签收
    "complete_task_using": "/workflow/$VERSION$/task/complete/%s",  # 任务审批
    "complete_task_using1": "/workflow/$VERSION$/task/completetask/%s/%s",  # 审批处理
    "complete_tasks_using": "/workflow/$VERSION$/task/completetasks",  # 批量审批
    "create_sub_task": "/workflow/$VERSION$/task/create/subtask/%s",  # 创建子任务
    "delegate_task_using": "/workflow/$VERSION$/task/delegate",  # 任务委派
    "delegate_task_cancel": "/workflow/$VERSION$/task/delegate/cancle",  # 任务委派取消
    "query_done_page": "/workflow/$VERSION$/task/donepage",  # 一级实例列表
    "query_done_task": "/workflow/$VERSION$/task/donetask",  # 查询已处理任务列表
    "download_file_using": "/workflow/$VERSION$/task/download/%s",  # 下载附件
    "delete_task_by": "/workflow/$VERSION$/task/drop/%s",  # 删除任务信息
    "get_executor_change": "/workflow/$VERSION$/task/executor",  # 流程转办/委派记录查询
    "query_my_focus": "/workflow/$VERSION$/task/focus",  # 我关注的
    "next_process_gate": "/workflow/$VERSION$/task/formproperties/%s",  # 获取当前节点的路由网关
    "informed_tasks_confirm": "/workflow/$VERSION$/task/informedTasksComfirm/%s",  # 知会任务确认
    "inquiry_task_using": "/workflow/$VERSION$/task/inquiry",  # 任务询问
    "query_business_key": "/workflow/$VERSION$/task/key/businessKeys",  # 根据业务key获取当前发起的所有流程
    "next_process_task": "/workflow/$VERSION$/task/nexttask/%s/%s",  # 获取下一个用户节点信息
    "signature_by_process": "/workflow/$VERSION$/task/process/countersign",  # 加签
    "minus_by_process": "/workflow/$VERSION$/task/process/minussign",  # 减签
    "query_process_chart": "/workflow/$VERSION$/task/processchart/%s",  # 查询流程图
    "query_task_by": "/workflow/$VERSION$/task/query/%s",  # 查询任务信息
    "read_task_using": "/workflow/$VERSION$/task/read",  # 设置已读
    "replace_assignee_using": "/workflow/$VERSION$/task/replace/%s",  # 离职任务替换
    "rollback_assignee_using": "/workflow/$VERSION$/task/rollback",  # 任务处理人撤回
    "rollback_pre_task": "/workflow/$VERSION$/task/rollbackPreTask",  # 任务回退到上一节点
    "query_running_user": "/workflow/$VERSION$/task/runningusertask",  # 根据流程实例id查询当前运行中的节点信息
    "get_running_user": "/workflow/$VERSION$/task/runningusertask/%s",  # 查询当前正在运行的用户节点
    "query_sign_task": "/workflow/$VERSION$/task/signtask",  # 查询签收任务列表
    "simle_complete_using": "/workflow/$VERSION$/task/simple/complete/%s",  # 创建子任务
    "skip_task_using": "/workflow/$VERSION$/task/skiptask/%s/%s",  # 跳跃任务节点
    "stop_task_using": "/workflow/$VERSION$/task/stopTask",  # 流程中止
    "task_view_using": "/workflow/$VERSION$/task/taskview",  # 查询审批详情页面
    "query_todo_task": "/workflow/$VERSION$/task/todo/task",  # queryTodoTaskList
    "query_todo_task1": "/workflow/$VERSION$/task/todotask",  # queryTodoTaskListByUserIdAndSystemId
    "query_todo_task2": "/workflow/$VERSION$/task/todotask/dimissionid",  # 按人员查询所有待办任务
    "transfer_assignee_using": "/workflow/$VERSION$/task/transfer",  # 任务转办
    "transfer_assignee_cancel": "/workflow/$VERSION$/task/transfer/cancle",  # 任务转办取消
    "transfer_delegate_cancel": "/workflow/$VERSION$/task/transferdelegate/cancle",  # 任务转办委派取消
    "unclaim_using_p": "/workflow/$VERSION$/task/unclaim",  # 退回签收
    "upload_file_using": "/workflow/$VERSION$/task/upload/%s/%s",  # 上传附件
    "urge_todo_using": "/workflow/$VERSION$/task/urge",  # 任务催办
    "query_historic_detail": "/workflow/$VERSION$/task/%s/history/formdata",  # 查询流程历史表单数据
})


def get_activity_img(self, process_instance_id, checker=None):
    """
    接口名称：当前流程活动节点坐标信息 x,y,height,width;    接口地址：/workflow/$VERSION$/task/activitycoor/{processInstanceId}；
    """
    r = RequestService.call_get(apis.get("get_activity_img", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_file_using(self, checker=None):
    """
    接口名称：删除附件;    接口地址：/workflow/$VERSION$/task/attachment/{attachmentId}；
    """
    r = RequestService.call_delete(apis.get("delete_file_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_attachment_list(self, process_instance_id, task_id="", checker=None):
    """
    接口名称：获取附件列表;    接口地址：/workflow/$VERSION$/task/attachments；
    """
    r = RequestService.call_get(apis.get("get_attachment_list", None), params={
        "processInstanceId": process_instance_id,  # 流程实例ID - required: False
        "taskId": task_id,  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def claim_using_p(self, process_instance_id, task_id, checker=None):
    """
    接口名称：任务签收;    接口地址：/workflow/$VERSION$/task/claim；
    """
    r = RequestService.call_post(apis.get("claim_using_p", None), params={
        "processInstanceId": process_instance_id,  # 流程id - required: True
        "taskId": task_id,  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def complete_task_using(self, checker=None):
    """
    接口名称：任务审批;    接口地址：/workflow/$VERSION$/task/complete/{taskId}；
    """
    r = RequestService.call_post(apis.get("complete_task_using", None), json={
        "taskComplete": ""  # taskComplete - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def complete_task_using1(self, checker=None):
    """
    接口名称：审批处理;    接口地址：/workflow/$VERSION$/task/completetask/{processInstanceId}/{taskId}；
    """
    r = RequestService.call_post(apis.get("complete_task_using1", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def complete_tasks_using(self, checker=None):
    """
    接口名称：批量审批;    接口地址：/workflow/$VERSION$/task/completetasks；
    """
    r = RequestService.call_post(apis.get("complete_tasks_using", None), json={
        "completeTasksDto": ""  # completeTasksDto - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def create_sub_task(self, checker=None):
    """
    接口名称：创建子任务;    接口地址：/workflow/$VERSION$/task/create/subtask/{taskId}；
    """
    r = RequestService.call_put(apis.get("create_sub_task", None), params={
        "userId": ""  # 处理人 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delegate_task_using(self, checker=None):
    """
    接口名称：任务委派;    接口地址：/workflow/$VERSION$/task/delegate；
    """
    r = RequestService.call_post(apis.get("delegate_task_using", None), params={
        "comment": "",  # 备注 - required: False
        "delegatedUserId": "",  # 被委派人ID - required: True
        "taskId": "",  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delegate_task_cancel(self, checker=None):
    """
    接口名称：任务委派取消;    接口地址：/workflow/$VERSION$/task/delegate/cancle；
    """
    r = RequestService.call_post(apis.get("delegate_task_cancel", None), params={
        "comment": "",  # 备注 - required: False
        "taskId": "",  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_done_page(self, dto, checker=None):
    """
    接口名称：一级实例列表
    接口地址：/workflow/$VERSION$/task/donepage
    """
    r = RequestService.call_get(apis.get("query_done_page", None), params={
        "tenantId": dto.get("tenantId", "ELIssue"),
        "taskName": dto.get("taskName", ""),
        "priority": dto.get("priority", ""),
        "startUserId": dto.get("startUserId", ""),
        "category": dto.get("category", ""),
        "assignee": dto.get("assignee", ""),
        "taskStartTimeStart": dto.get("taskStartTimeStart", ""),
        "taskStartTimeEnd": dto.get("taskStartTimeEnd", ""),
        "taskEndTimeStart": dto.get("taskEndTimeStart", ""),
        "taskEndTimeEnd": dto.get("taskEndTimeEnd", ""),
        "processInstanceEndTimeStart": dto.get("processInstanceEndTimeStart", ""),
        "processInstanceEndTimeEnd": dto.get("processInstanceEndTimeEnd", ""),
        "processDefinitionId": dto.get("processDefinitionId", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "pager_name": dto.get("pager_name", "20"),
        "sort_by": dto.get("sort_by", ""),
        "order_by": dto.get("order_by", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
        "flag": dto.get("flag", "work"),
        "taskEndTimeFrom": dto.get("taskEndTimeFrom", ""),
        "taskEndTimeTo": dto.get("taskEndTimeTo", ""),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_done_task(self, dto, checker=None):
    """
    接口名称：查询已处理任务列表
    接口地址：/workflow/$VERSION$/task/donetask
    """
    r = RequestService.call_get(apis.get("query_done_task", None), params={
        "tenantId": dto.get("tenantId", "ELIssue"),
        "taskName": dto.get("taskName", ""),
        "priority": dto.get("priority", ""),
        "startUserId": dto.get("startUserId", ""),
        "category": dto.get("category", ""),
        "assignee": dto.get("assignee", ""),
        "taskStartTimeStart": dto.get("taskStartTimeStart", ""),
        "taskStartTimeEnd": dto.get("taskStartTimeEnd", ""),
        "taskEndTimeStart": dto.get("taskEndTimeStart", ""),
        "taskEndTimeEnd": dto.get("taskEndTimeEnd", ""),
        "processInstanceEndTimeStart": dto.get("processInstanceEndTimeStart", ""),
        "processInstanceEndTimeEnd": dto.get("processInstanceEndTimeEnd", ""),
        "processDefinitionId": dto.get("processDefinitionId", ""),
        "processDefinitionKey": dto.get("processDefinitionKey", ""),
        "pager_name": dto.get("pager_name", "20"),
        "sort_by": dto.get("sort_by", ""),
        "order_by": dto.get("order_by", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
        "flag": dto.get("flag", "work"),
        "taskEndTimeFrom": dto.get("taskEndTimeFrom", ""),
        "taskEndTimeTo": dto.get("taskEndTimeTo", ""),
        "processInstanceId": dto.get("processInstanceId", "")
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def download_file_using(self, checker=None):
    """
    接口名称：下载附件;    接口地址：/workflow/$VERSION$/task/download/{attachmentId}；
    """
    r = RequestService.call_get(apis.get("download_file_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_task_by(self, checker=None):
    """
    接口名称：删除任务信息;    接口地址：/workflow/$VERSION$/task/drop/{taskId}；
    """
    r = RequestService.call_get(apis.get("delete_task_by", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_executor_change(self, checker=None):
    """
    接口名称：流程转办/委派记录查询;    接口地址：/workflow/$VERSION$/task/executor；
    """
    r = RequestService.call_get(apis.get("get_executor_change", None), params={
        "pageIndex": 1,  # 页码 - required: False
        "pageSize": 20,  # 页大小 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_my_focus(self, dto, checker=None):
    """
    接口名称：我关注的
    接口地址：/workflow/$VERSION$/task/focus
    """
    r = RequestService.call_get(apis.get("query_my_focus", None), params={
        "tenantId": dto.get("tenantId", "department"),
        "category": dto.get("category", ""),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
        "contextType": dto.get("contextType", "0"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def next_process_gate(self, task_id, checker=None):
    """
    接口名称：获取当前节点的路由网关;    接口地址：/workflow/$VERSION$/task/formproperties/{taskId}；
    """
    r = RequestService.call_get(apis.get("next_process_gate", task_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def informed_tasks_confirm(self, checker=None):
    """
    接口名称：知会任务确认;    接口地址：/workflow/$VERSION$/task/informedTasksComfirm/{id}；
    """
    r = RequestService.call_post(apis.get("informed_tasks_confirm", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def inquiry_task_using(self, checker=None):
    """
    接口名称：任务询问;    接口地址：/workflow/$VERSION$/task/inquiry；
    """
    r = RequestService.call_post(apis.get("inquiry_task_using", None), params={
        "comment": "",  # 备注 - required: False
        "inquiryUserId": "",  # 被询问人ID - required: True
        "taskId": "",  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_business_key(self, task_def_key, checker=None):
    """
    接口名称：根据业务key获取当前发起的所有流程;    接口地址：/workflow/$VERSION$/task/key/businessKeys；
    """
    r = RequestService.call_get(apis.get("query_business_key", None), params={
        "businessKeys": task_def_key,  # 业务keys, 多个用逗号隔开 - required: True
        "pageIndex": 1,  # 页码 - required: False
        "pageSize": 20,  # 页大小 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def next_process_task(self, process_instance_id, route_flag, task_def_key="", checker=None):
    """
    接口名称：获取下一个用户节点信息;    接口地址：/workflow/$VERSION$/task/nexttask/{processInstanceId}/{routeFlag}；
    """
    r = RequestService.call_get(apis.get("next_process_task", process_instance_id, route_flag), params={
        "taskKey": task_def_key  # 当前节点TaskKey - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def signature_by_process(self, checker=None):
    """
    接口名称：加签;    接口地址：/workflow/$VERSION$/task/process/countersign；
    """
    r = RequestService.call_post(apis.get("signature_by_process", None), json={
        "etSignalTask": ""  # 加签减签对像 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def minus_by_process(self, checker=None):
    """
    接口名称：减签;    接口地址：/workflow/$VERSION$/task/process/minussign；
    """
    r = RequestService.call_post(apis.get("minus_by_process", None), json={
        "etSignalTask": ""  # 加签减签对像 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_process_chart(self, checker=None):
    """
    接口名称：查询流程图;    接口地址：/workflow/$VERSION$/task/processchart/{processInstanceId}；
    """
    r = RequestService.call_get(apis.get("query_process_chart", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_task_by(self, task_id, checker=None):
    """
    接口名称：查询任务信息;    接口地址：/workflow/$VERSION$/task/query/{taskId}；
    """
    r = RequestService.call_get(apis.get("query_task_by", task_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def read_task_using(self, task_id, checker=None):
    """
    接口名称：设置已读;    接口地址：/workflow/$VERSION$/task/read；
    """
    r = RequestService.call_put(apis.get("read_task_using", None), params={
        "taskId": task_id  # 任务id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def replace_assignee_using(self, checker=None):
    """
    接口名称：离职任务替换;    接口地址：/workflow/$VERSION$/task/replace/{userId}；
    """
    r = RequestService.call_put(apis.get("replace_assignee_using", None), json={
        "replaceList": ""  # 任务id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def rollback_assignee_using(self, checker=None):
    """
    接口名称：任务处理人撤回;    接口地址：/workflow/$VERSION$/task/rollback；
    """
    r = RequestService.call_post(apis.get("rollback_assignee_using", None), params={
        "comment": "",  # 备注 - required: False
        "taskId": "",  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def rollback_pre_task(self, checker=None):
    """
    接口名称：任务回退到上一节点;    接口地址：/workflow/$VERSION$/task/rollbackPreTask；
    """
    r = RequestService.call_post(apis.get("rollback_pre_task", None), params={
        "comment": "",  # 备注 - required: False
        "processInstanceId": "",  # 流程ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_running_user(self, checker=None):
    """
    接口名称：根据流程实例id查询当前运行中的节点信息;    接口地址：/workflow/$VERSION$/task/runningusertask；
    """
    r = RequestService.call_post(apis.get("query_running_user", None), json={
        "processInstanceIds": ""  # 流程实例ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_running_user(self, process_instance_id, checker=None):
    """
    接口名称：查询当前正在运行的用户节点;    接口地址：/workflow/$VERSION$/task/runningusertask/{processInstanceId}；
    """
    r = RequestService.call_get(apis.get("get_running_user", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_sign_task(self, checker=None):
    """
    接口名称：查询签收任务列表;    接口地址：/workflow/$VERSION$/task/signtask；
    """
    r = RequestService.call_get(apis.get("query_sign_task", None), params={

    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def simle_complete_using(self, checker=None):
    """
    接口名称：创建子任务;    接口地址：/workflow/$VERSION$/task/simple/complete/{taskId}；
    """
    r = RequestService.call_put(apis.get("simle_complete_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def skip_task_using(self, checker=None):
    """
    接口名称：跳跃任务节点;    接口地址：/workflow/$VERSION$/task/skiptask/{processInstanceId}/{toStateKey}；
    """
    r = RequestService.call_post(apis.get("skip_task_using", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def stop_task_using(self, checker=None):
    """
    接口名称：流程中止;    接口地址：/workflow/$VERSION$/task/stopTask；
    """
    r = RequestService.call_post(apis.get("stop_task_using", None), params={
        "comment": "",  # 备注 - required: False
        "processInstanceId": "",  # 流程ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def task_view_using(self, process_definition_id, process_instance_id, task_def_key, task_id, checker=None):
    """
    接口名称：查询审批详情页面;    接口地址：/workflow/$VERSION$/task/taskview
    """
    r = RequestService.call_get(apis.get("task_view_using", None), params={
        "processDefinitionId": process_definition_id,  # 流程定义ID - required: True
        "processInstanceId": process_instance_id,  # 流程实例ID - required: True
        "taskDefKey": task_def_key,
        "taskId": task_id,  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_todo_task(self, dto, checker=None):
    """
    接口名称：queryTodoTaskList;    接口地址：/workflow/$VERSION$/task/todo/task；
    """
    r = RequestService.call_post(apis.get("query_todo_task", None), json={
        "queryDto": dto  # queryDto - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_todo_task1(self, dto, checker=None):
    """
    接口名称：queryTodoTaskListByUserIdAndSystemId
    接口地址：/workflow/$VERSION$/task/todotask
    """
    r = RequestService.call_get(apis.get("query_todo_task1", None), params={
        "tenantId": dto.get("tenantId", "type1"),
        "processDefinitionKey": dto.get("processDefinitionKey"),
        "taskName": dto.get("taskName"),
        "category": dto.get("category", "others"),
        "taskType": dto.get("taskType"),
        "taskStartTimeStart": dto.get("taskStartTimeStart"),
        "taskStartTimeEnd": dto.get("taskStartTimeEnd"),
        "dueDateStart": dto.get("dueDateStart"),
        "dueDateEnd": dto.get("dueDateEnd"),
        "startUserId": dto.get("startUserId"),
        "pager_name": dto.get("pager_name", "50"),
        "sort_by": dto.get("sort_by"),
        "order_by": dto.get("order_by"),
        "pageSize": dto.get("pageSize", 50),
        "pageIndex": dto.get("pageIndex", 1),
        "flag": dto.get("flag", "work"),
        "taskStartTimeFrom": dto.get("taskStartTimeFrom"),
        "taskStartTimeTo": dto.get("taskStartTimeTo"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_todo_task2(self, checker=None):
    """
    接口名称：按人员查询所有待办任务;    接口地址：/workflow/$VERSION$/task/todotask/dimissionid；
    """
    r = RequestService.call_get(apis.get("query_todo_task2", None), params={
        "dimissionId": "",  # 任务对象 - required: False
        "pageIndex": 1,  # 页码 - required: False
        "pageSize": 20,  # 页大小 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def transfer_assignee_using(self, checker=None):
    """
    接口名称：任务转办;    接口地址：/workflow/$VERSION$/task/transfer；
    """
    r = RequestService.call_post(apis.get("transfer_assignee_using", None), params={
        "comment": "",  # 备注 - required: False
        "taskId": "",  # 任务ID - required: True
        "transferAssignee": "",  # 处理人ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def transfer_assignee_cancel(self, task_id, comment, checker=None):
    """
    接口名称：任务转办取消;    接口地址：/workflow/$VERSION$/task/transfer/cancle；
    """
    r = RequestService.call_post(apis.get("transfer_assignee_cancel", None), params={
        "comment": comment,  # 备注 - required: False
        "taskId": task_id,  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def transfer_delegate_cancel(self, checker=None):
    """
    接口名称：任务转办委派取消;    接口地址：/workflow/$VERSION$/task/transferdelegate/cancle；
    """
    r = RequestService.call_post(apis.get("transfer_delegate_cancel", None), params={
        "comment": "",  # 备注 - required: False
        "executorId": "",  # 转办委派的ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def unclaim_using_p(self, task_id, checker=None):
    """
    接口名称：退回签收;    接口地址：/workflow/$VERSION$/task/unclaim；
    """
    r = RequestService.call_post(apis.get("unclaim_using_p", None), params={
        "taskId": task_id  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def upload_file_using(self, checker=None):
    """
    接口名称：上传附件;    接口地址：/workflow/$VERSION$/task/upload/{processInstanceId}/{taskId}；
    """
    r = RequestService.call_post(apis.get("upload_file_using", None), data={
        "file": ""  # file - required: True
    }, params={
        "description": ""  # 附件描述 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def urge_todo_using(self, checker=None):
    """
    接口名称：任务催办;    接口地址：/workflow/$VERSION$/task/urge；
    """
    r = RequestService.call_post(apis.get("urge_todo_using", None), json={
        "paramMap": ""  # 参数Map - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_historic_detail(self, process_instance_id, checker=None):
    """
    接口名称：查询流程历史表单数据;    接口地址：/workflow/$VERSION$/task/{processInstanceId}/history/formdata；
    """
    r = RequestService.call_get(apis.get("query_historic_detail", process_instance_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
