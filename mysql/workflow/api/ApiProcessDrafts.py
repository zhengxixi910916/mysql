from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "list_using_g": "/workflow/$VERSION$/proccessDraft/",  # 查询流程草稿
    "delete_using_d": "/workflow/$VERSION$/proccessDraft/",  # 删除流程草稿
    "get_by_business": "/workflow/$VERSION$/proccessDraft/businessKey/%s",  # 通过业务businessKey来查询对于的草稿
    "get_using_g": "/workflow/$VERSION$/proccessDraft/%s",  # 通过ID查询草稿
    "start_using_p": "/workflow/$VERSION$/proccessDraft/%s",  # 通过草稿启动流程
    "save_using_p": "/workflow/$VERSION$/proccessDraft/%s/%s",  # 保存流程草稿
})


def list_using_g(self, create_time, title_process_submit, tenant_id, page_index, page_size,
                 checker=None):
    """
    接口名称：查询流程草稿
    接口地址：/workflow/$VERSION$/proccessDraft/
    """
    r = RequestService.call_get(apis.get("list_using_g"), params={
        "category": "",  # 系统ID（问题、风险、任务、需求） - required: False
        "createTime": create_time,  # createTime - required: False
        "pageIndex": page_index,  # pageIndex - required: False
        "pageSize": page_size,  # pageSize - required: False
        "processDefinitionKey": "",  # 流程KEY - required: False
        "tenantId": tenant_id,  # tenantId - required: False
        "titleProcessSubmit": title_process_submit,  # titleProcessSubmit - required: False
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_using_d(self, ids, checker=None):
    """
    接口名称：删除流程草稿
    接口地址：/workflow/$VERSION$/proccessDraft/
    """
    r = RequestService.call_delete(apis.delete("delete_using_d"), params={
        "ids": ids  # ids - required: True
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_by_business(self, business_key, def_key, checker=None):
    """
    接口名称：通过业务businessKey来查询对于的草稿
    接口地址：/workflow/$VERSION$/proccessDraft/businessKey/{businessKey}
    """
    r = RequestService.call_get(apis.get("get_by_business", business_key), params={
        "processDefinitionKey": def_key  # processDefinitionKey - required: False
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_using_g(self, ids, checker=None):
    """
    接口名称：通过ID查询草稿
    接口地址：/workflow/$VERSION$/proccessDraft/{id}
    """
    r = RequestService.call_get(apis.get("get_using_g", ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def start_using_p(self, ids, checker=None):
    """
    接口名称：通过草稿启动流程
    接口地址：/workflow/$VERSION$/proccessDraft/{id}
    """
    r = RequestService.call_post(apis.post("start_using_p", ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def save_using_p(self, dto, category="ELTask", def_key="PPM_PLAN_APPROVE", checker=None):
    """
    接口名称：保存流程草稿
    接口地址：/workflow/$VERSION$/proccessDraft/{processDefinitionKey}/{category}
    """
    r = RequestService.call_post(apis.post("save_using_p", def_key, category), params={
        "title_process_submit": dto.get("title_process_submit", "计划发布流程-1"),
        "description_process_submit": dto.get("description_process_submit", "计划发布流程"),
        "dueDate": dto.get("dueDate", "2022-05-10"),
        "priority": dto.get("priority", "50"),
        "preparing_candidateUsers": dto.get("preparing_candidateUsers", "SYS_E39B20EA11E7A81AC85B767C89C1"),
        "attachmentId": dto.get("attachmentId", ""),
        "description": dto.get("description", "计划发布流程"),
        "title": dto.get("title", "计划发布流程-1"),
        "businessKey": dto.get("businessKey", ""),
        "bussinessFormDataJson": dto.get("bussinessFormDataJson", []),
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
